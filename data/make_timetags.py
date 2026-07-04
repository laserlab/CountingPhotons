"""Generate simulated Hanbury Brown-Twiss time-tag data for Lecture 4.

Three "mystery" light sources (A, B, C) are simulated hitting a 50:50
beamsplitter with a single-photon detector in each output arm.  For each
source the script saves the photon arrival times ("time tags") recorded by
the two detectors, exactly the kind of raw data a time-tagging module
(e.g. a TimeTagger or HydraHarp) produces in a real HBT measurement.

The three sources are one of each (order shuffled by the random seed, so
reading this file does not spoil the exercise):

* coherent  -- ideal laser: homogeneous Poisson process, g2(0) = 1
* thermal   -- chaotic light: doubly stochastic Poisson process driven by
               a complex Gaussian field with coherence time TAU_C,
               g2(0) = 2 decaying to 1 over TAU_C
* emitter   -- single quantum emitter: one photon per excitation cycle
               (exponential re-excitation + exponential emission delay),
               g2(0) = 0 recovering to 1 over the cycle time

Output files
------------
data/source_A_timetags.npz, ..._B_..., ..._C_...
    Each contains:
    t1 : uint64 array, detector-1 arrival times [ns]
    t2 : uint64 array, detector-2 arrival times [ns]
    duration_ns : uint64 scalar, total measurement time [ns]

Usage
-----
    python data/make_timetags.py

Reproducible: uses a fixed seed (2026).  Change SEED for a different
source-to-letter assignment.
"""

import numpy as np

# --------------------------------------------------------------------------
# Simulation parameters
# --------------------------------------------------------------------------
SEED = 2026
DURATION = 10.0          # total measurement time [s]
RATE_DETECTED = 25e3     # target detected count rate, both detectors [1/s]

TAU_C = 2.0e-6           # thermal light: field coherence time [s]
TAU_EXC = 1.0e-6         # emitter: mean re-excitation time [s]
TAU_EM = 1.0e-6          # emitter: excited-state lifetime [s]

DARK_RATE = 200.0        # dark counts per detector [1/s]
JITTER = 1.0e-9          # detector timing jitter, 1 sigma [s]


def coherent_arrivals(rng: np.random.Generator,
                      rate: float, duration: float) -> np.ndarray:
    """Arrival times of a homogeneous Poisson process.

    Parameters
    ----------
    rng : numpy random generator
    rate : mean photon rate [1/s]
    duration : total time [s]

    Returns
    -------
    ndarray of arrival times [s], sorted
    """
    n = rng.poisson(rate * duration)
    return np.sort(rng.uniform(0.0, duration, n))


def thermal_arrivals(rng: np.random.Generator,
                     rate: float, duration: float,
                     tau_c: float) -> np.ndarray:
    """Arrival times of single-mode chaotic (thermal) light.

    The complex field E(t) is a discrete Ornstein-Uhlenbeck (AR(1))
    process sampled on a grid much finer than the coherence time, so the
    intensity I = |E|^2 is exponentially distributed (single-mode thermal
    statistics) with correlation time tau_c.  Photons are then generated
    as a Poisson process with the fluctuating rate ~ I(t) (a Cox
    process), which yields g2(0) = 2.

    Parameters
    ----------
    rng : numpy random generator
    rate : mean photon rate [1/s]
    duration : total time [s]
    tau_c : field coherence time [s]

    Returns
    -------
    ndarray of arrival times [s], sorted
    """
    dt = tau_c / 20.0                       # time grid resolution [s]
    n_steps = int(duration / dt)
    # AR(1) recursion for the complex field: E_k = a E_{k-1} + s * noise
    a = np.exp(-dt / tau_c)
    s = np.sqrt((1.0 - a**2) / 2.0)         # unit-variance stationary field
    noise = rng.normal(size=(n_steps, 2)).view(np.complex128).ravel()
    field = np.empty(n_steps, dtype=np.complex128)
    field[0] = (rng.normal() + 1j * rng.normal()) / np.sqrt(2.0)
    for k in range(1, n_steps):
        field[k] = a * field[k - 1] + s * noise[k]
    intensity = np.abs(field) ** 2          # mean 1, exponential distribution
    # Poisson clicks in each grid step with instantaneous rate*I
    mean_counts = rate * dt * intensity
    counts = rng.poisson(mean_counts)
    # place each click uniformly inside its grid step
    step_index = np.repeat(np.arange(n_steps), counts)
    times = (step_index + rng.uniform(size=step_index.size)) * dt
    return np.sort(times)


def emitter_arrivals(rng: np.random.Generator,
                     duration: float,
                     tau_exc: float, tau_em: float) -> np.ndarray:
    """Emission times of a single two-level emitter.

    After each photon the emitter must be re-excited (exponential waiting
    time tau_exc) and then decays radiatively (exponential lifetime
    tau_em): consecutive photons are separated by the *sum* of the two,
    so two photons can never be emitted at the same instant -> g2(0) = 0.

    Parameters
    ----------
    rng : numpy random generator
    duration : total time [s]
    tau_exc : mean re-excitation time [s]
    tau_em : excited-state lifetime [s]

    Returns
    -------
    ndarray of emission times [s], sorted
    """
    mean_cycle = tau_exc + tau_em
    n_est = int(1.5 * duration / mean_cycle) + 100   # safe overshoot
    gaps = (rng.exponential(tau_exc, n_est)
            + rng.exponential(tau_em, n_est))
    times = np.cumsum(gaps)
    return times[times < duration]


def detect_hbt(rng: np.random.Generator, photons: np.ndarray,
               efficiency: float, duration: float) -> tuple:
    """Send photons through a 50:50 beamsplitter onto two lossy detectors.

    Each photon is detected with probability `efficiency` and then routed
    to detector 1 or 2 with probability 1/2 each.  Dark counts and
    Gaussian timing jitter are added, times are clipped to the
    measurement window and returned in nanoseconds.

    Parameters
    ----------
    rng : numpy random generator
    photons : photon arrival times at the beamsplitter [s]
    efficiency : total detection probability per photon (0..1)
    duration : total time [s]

    Returns
    -------
    (t1, t2) : uint64 arrays of detected time tags [ns], sorted
    """
    detected = photons[rng.uniform(size=photons.size) < efficiency]
    to_det1 = rng.uniform(size=detected.size) < 0.5
    streams = []
    for mask in (to_det1, ~to_det1):
        t = detected[mask]
        # dark counts: uncorrelated Poisson background
        n_dark = rng.poisson(DARK_RATE * duration)
        t = np.concatenate([t, rng.uniform(0.0, duration, n_dark)])
        # timing jitter
        t = t + rng.normal(0.0, JITTER, t.size)
        t = t[(t >= 0.0) & (t < duration)]
        streams.append(np.sort((t * 1e9).astype(np.uint64)))
    return streams[0], streams[1]


def main() -> None:
    rng = np.random.default_rng(SEED)

    # The emitter is rate-limited by its excitation cycle: it emits
    # 1/(TAU_EXC+TAU_EM) photons/s and we thin with the detection
    # efficiency needed to land at RATE_DETECTED.  The classical sources
    # get the same efficiency treatment for fairness (loss does not
    # change their statistics).
    emitter_emission_rate = 1.0 / (TAU_EXC + TAU_EM)      # [1/s]
    efficiency = RATE_DETECTED / emitter_emission_rate     # ~5 %
    source_rate = RATE_DETECTED / efficiency               # photons at BS [1/s]

    sources = {
        "coherent": lambda: coherent_arrivals(rng, source_rate, DURATION),
        "thermal": lambda: thermal_arrivals(rng, source_rate, DURATION,
                                            TAU_C),
        "emitter": lambda: emitter_arrivals(rng, DURATION, TAU_EXC, TAU_EM),
    }

    # shuffle so that file names do not reveal the physics
    kinds = list(sources)
    rng.shuffle(kinds)

    for letter, kind in zip("ABC", kinds):
        photons = sources[kind]()
        t1, t2 = detect_hbt(rng, photons, efficiency, DURATION)
        np.savez_compressed(
            f"data/source_{letter}_timetags.npz",
            t1=t1, t2=t2,
            duration_ns=np.uint64(DURATION * 1e9),
        )
        print(f"source_{letter}: {t1.size + t2.size:7d} tags "
              f"({(t1.size + t2.size) / DURATION / 1e3:.1f} kcps)")


if __name__ == "__main__":
    main()
