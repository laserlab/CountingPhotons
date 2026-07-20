# Lecture Plan — Counting Photons

ICTP-SAIFR school, IFT–UNESP São Paulo · July 27–29, 2026 · Tim Thomay

**Audience:** physics graduate students. Quantum mechanics is assumed
(operators, Hilbert spaces, harmonic oscillator); quantum *optics* is not.
Basic programming skills are assumed; all code is heavily commented and every
hands-on notebook starts from a worked example before asking for student code.

**Format:** 6 × 1 h. Monday is a pure lecture day (the 14:00 hour is a
live-coding demo — no student laptops needed); interactive work starts
Tuesday 10:30, after students do the 20-minute setup notebook on Monday
evening (the only evening task of the week). Wednesday is a single 2 h
simulation lab. All materials are Jupyter notebooks that run in GitHub
Codespaces (preferred) or Google Colab. Every exercise doubles as take-home
material: submissions have **no deadline** and are reviewed after the
school.

---

## 0 — Setup (standalone, ~20 min; announced during Monday's lectures)

`lectures/00_Setup_GitHub_Codespaces.ipynb`

**Goal:** every student has a working environment by Tuesday 10:30 (the
first interactive session). Announced at the end of both Monday lectures;
done Monday evening — the only evening task of the week. Also points
students to PHY386 (github.com/ubsuny/PHY386) for self-paced Python/Jupyter
basics.

- Create a GitHub account, fork `CountingPhotons`, launch a Codespace
- Run a test cell that imports QuTiP and Perceval and prints a success banner
- The Colab fallback path, step by step
- How work will be submitted (fork → `submissions/<username>/` → push);
  the one git workflow diagram they need
- Troubleshooting section (kernel not found, Codespace build fails, etc.)

---

## 1 — Counting Photons: What is Quantum Light? (lecture, Mon 11:30)

`lectures/01_QuantumLight_PhotonStatistics.ipynb`

**Learning objectives** — students can:
1. explain why photon-number statistics distinguish sources of identical
   average intensity;
2. write down and recognize P(n) for coherent, thermal, and Fock states at
   any brightness;
3. compute and interpret the Mandel Q parameter;
4. estimate shot noise in real measurements and explain LIGO's squeezed-
   vacuum injection qualitatively.

**Timing (60 min):**
- 0–7 · History: the reluctant photon, 1900–1926 (Planck → Einstein 1905 →
  Taylor's feeble-light fringes → Millikan → Compton → the word "photon").
- 7–12 · Motivation: three sources, same power, different physics; the click
  stream as the raw datum.
- 12–22 · Field quantization in one pass: mode = oscillator, quadratures,
  zero-point fluctuations; Fock / coherent / thermal states; Arecchi 1965.
- 22–30 · The fingerprints: P(n) at equal n̄; P(n) across brightness
  (n̄ = 0.2 / 4 / 25 — why faint-light statistics are hard to distinguish);
  phase-space triptych (Wigner functions, negativity as non-classicality).
- 30–38 · Variance and Mandel Q; Einstein's 1909 fluctuation formula
  (wave + particle terms); classical bound Q ≥ 0.
- 38–50 · Shot noise: definition (Poisson, Schottky), real-world numbers,
  the 22-decade scaling figure; **LIGO case study**: Δφ = 1/√N̄, why
  200 kW; Caves 1981 — vacuum enters the dark port; schematic noise
  budget (two quadratures of the same vacuum, SQL, frequency-dependent
  squeezing); squeezed-vacuum Wigner + even-photon P(n) → bridge to SPDC.
  Teaser: three itching questions handed to the afternoon demo.
- 50–55 · Click streams; where the states live in the lab (incl. black
  holes as the only exactly thermal source).
- 55–60 · Check-your-understanding (6 questions) + buffer.

**Key figures (all generated in-notebook):** P(n) comparison at n̄ = 4;
P(n) across three brightness regimes; Wigner triptych; variance vs mean;
"same scene at three light levels" shot-noise strips; vacuum vs squeezed
vacuum; negative-binomial multimode washout; three click streams.

---

## 2 — Simulating Photon Statistics (lecture with live demo, Mon 14:00)

`lectures/02_HandsOn_SimulatingPhotonStatistics.ipynb`

**Learning objectives** — students can:
1. build coherent/thermal/Fock states in QuTiP and extract P(n), ⟨n⟩, Δn²;
2. Monte-Carlo sample detector clicks and estimate statistics *with bootstrap
   error bars*;
3. show numerically what loss does to sub-Poissonian light;
4. plot Wigner functions and compare non-classicality witnesses.

**Timing (60 min):**
Format: live coding on screen, students predict outcomes — no laptops.
The same notebook is the students' self-paced practice material afterwards.

- 0–8 · Worked example: `coherent()`, `thermal_dm()`, `fock()`; P(n) from
  the density-matrix diagonal.
- 8–45 · Exercises as demos (audience predicts before each run):
  - E1: reproduce the equal-n̄ fingerprint figure
  - E2: `mandel_Q` function + self-checks
  - E3: sample 10 000 clicks, estimate Q from data, bootstrap error bar;
    when is Q < 0 certified at 95% confidence?
  - E4: Wigner functions of five states — which witness fires for which?
  - Demo (from L1 overflow): "a Fock state is squeezed, right?" —
    quadrature-noise bars, |4⟩ vs thermal n̄=4 identical second moments,
    witness table; "why doesn't LIGO use Fock states?" — |0⟩/|1⟩/|2⟩
    Wigner triptych, phase vs number certainty, Heisenberg limit vs loss
  - Demo: multimode washout — negative binomial, Q = n̄/M, why daylight
    looks Poissonian (+ black-hole aside); feeds directly into:
  - E5: laser near threshold as coherent/thermal mixture — Q(p), Arecchi
  - E5 addendum: ASE = thermal light over M modes, Q = n̄/M — why a fiber
    amplifier's light passes for Poissonian until filtered
- 45–52 · Stretch: binomial-thinning loss model on |4⟩, Q(η) = −η;
  discussion: why loss "classicalizes".
- 52–58 · **Case study: three quantum rulers** — squeezing (prefactor,
  robust, deployed [Tse2019, Lough2021, Ganapathy2023]), number states
  (Heisenberg scaling, voided by loss [HollandBurnett1993, Afek2010,
  Demkowicz2012]), HOM visibility (change the observable, attosecond
  delays with no phase stabilization [Lyons2018]); the pick-your-
  failure-mode decision table.
- 58–60 · Announce the setup notebook 00: tonight, ~20 min, the week's only
  evening task — needed for tomorrow's hands-on sessions.

---

## 3 — Correlations: g⁽²⁾, HBT, and How We Make & Catch Photons (lecture, Tue 9:00)

`lectures/03_Correlations_Generation_Detection.ipynb`

**Learning objectives** — students can:
1. define g⁽²⁾(τ), prove the classical bound g⁽²⁾(0) ≥ 1, state the quantum
   values;
2. explain the HBT geometry (dead time, normalization, error bars) and its
   stellar-interferometry origin;
3. compare sources and detectors by the figures of merit that matter.

**Timing (60 min):**
- 0–5 · Warm-up quiz (4 questions from Monday).
- 5–15 · **History: the 1956 HBT scandal** — radio-astronomy origins, the
  tabletop experiment, Brannen & Ferguson's failed replication ("major
  revision of quantum mechanics"), Purcell's resolution; aftermath timeline
  (Narrabri → Glauber 1963 → Kimble 1977 → Grangier 1986 → today).
- 15–27 · g⁽²⁾(τ): definition, normal ordering; two-line Cauchy–Schwarz
  proof of g⁽²⁾ ≥ 1; quantum values 2 / 1 / 1−1/n; the 1/2 single-photon
  certificate; g⁽²⁾ = 1 + Q/n̄ and why faint-light physics measures g⁽²⁾
  (loss invariance!).
- 27–35 · Shapes in time: bunching decay, antibunching recovery; **driven
  two-level atom: the dip rings at the Rabi frequency** — dip shape as free
  spectroscopy; open-systems dictionary (the dip = optical Bloch/Lindblad
  dynamics after a quantum jump); **one emitter → N emitters**:
  g⁽²⁾(0) = 2(1−1/N) + g⁽²⁾₁(0)/N interpolates antibunching → chaotic light,
  with the independence caveat as the hand-off to the cooperative-emission
  lectures.
- 35–42 · HBT in practice: geometry, accidental normalization, start–stop
  vs streaming taggers, Poisson error bars; **stellar version**: van
  Cittert–Zernike, the Sirius baseline estimate.
- 42–46 · Higher orders: g⁽ᵏ⁾ table, thermal k!, why g⁽³⁾ separates noisy
  |1⟩ from clean |2⟩.
- 46–53 · Generation: the four-row source table; worked example — why the
  attenuated laser fails QKD (photon-number splitting); SPDC + heralding
  teaser; quantum-dot state of the art.
- 53–58 · Detection: SPAD/SNSPD/TES table; efficiency, dark counts,
  afterpulsing, jitter; **simulated TES pulse-height spectrum** — photon
  counting as calorimetry; **from clicks to P(n)**: click-detector POVM
  (one SPAD can only see "≥1"), multiplexed quasi-PNR [Achilles2003] with
  the P(k|n) formula and a simulated C(k) figure — loss and saturation
  distort but don't destroy the fingerprints, and the distortion inverts.
- 58–60 · Bridge: "you get three mystery click streams after the break."

---

## 4 — Hands-on: g⁽²⁾ from Click Data (Tue 10:30)

`lectures/04_HandsOn_g2_HBT.ipynb`

**Learning objectives** — students can:
1. compute g⁽²⁾(τ) from raw time tags via a coincidence histogram;
2. classify unknown sources with quantitative evidence and error bars;
3. quantify background degradation of an antibunching dip;
4. fit correlation times and interpret them as source physics.

**Timing (60 min):**
- 0–10 · The dataset (three unlabeled HBT recordings); worked example:
  coincidence histogram + normalization for source A.
- 10–40 · Exercises:
  - E1: g⁽²⁾(τ) for all three sources, g⁽²⁾(0) table
  - E2: the verdict — identity + evidence (binning vs dark counts discussion)
  - E3: add background, watch the g⁽²⁾(0) < 0.5 certificate fail; compare
    with the analytic background model
  - E4: fit τ_c and τ_r with Poisson error bars (`curve_fit`); why the
    antibunching recovery constant is NOT the cycle duration
  - Stretch: **reconstruct P(n) from click statistics** — simulate an
    8-bin multiplexed detector, build the P(k|n) matrix, invert with
    `nnls`; watch the inversion fail gracefully at η = 0.3
- 40–50 · Cross-check in QuTiP: operator g⁽²⁾(0) vs time-tag estimates.
- 50–60 · Live walkthrough of the submission flow (2 min, on screen);
  finishing exercises + submitting = take-home, no deadline.

**Provided:** `data/make_timetags.py` (seeded, committed) generates the
datasets; students may re-generate with different parameters.

---

## 5 — Lab: Hong–Ou–Mandel Interference in Perceval (Wed 10:30)

`lectures/05_Lab_HOM_Interference.ipynb`

**Learning objectives** — students can:
1. build and sample linear-optical circuits in Perceval;
2. distinguish single-photon (first-order) from two-photon (HOM)
   interference experimentally;
3. simulate a HOM dip and extract its visibility;
4. demonstrate NOON-state super-resolution.

**Timing (60 min):**
- 0–12 · Perceval crash course (run-along): `BasicState`, `Circuit`, `BS`,
  `Processor`, `probs()` vs `sample_count()`; one photon on a beamsplitter.
- 12–20 · **Taylor 1909 on a chip**: single-photon MZI fringes — one photon
  interferes with itself, and classical waves explain it perfectly.
- 20–30 · The HOM effect: |1,1⟩ on a 50:50 BS, amplitude cancellation,
  photon bunching — no classical explanation.
- 30–52 · Exercises:
  - E1: coincidences vs reflectivity, (1−2R)² overlay
  - E2: the HOM dip via source indistinguishability; Gaussian delay mapping;
    visibility
  - E3: two-photon interference has no phase (wiggle test) — contrast with
    the MZI fringe; **interlude**: number–phase complementarity — why
    photon-counting experiments need no phase stabilization (stability
    table: MZI vs HBT vs HOM vs homodyne), and the visibility fine print
    (V = indistinguishability, V > 1/2 as the quantum certificate,
    raw vs corrected)
  - E4: NOON state in the MZI — coincidence fringe at 2φ, super-resolution;
    link back to LIGO squeezing
- 52–60 · Wrap-up: HOM 1987 as sub-picosecond metrology [Hong1987]; dip
  visibility as *the* source benchmark; HOM as the engine of photonic QC.

---

## 6 — Lab: Heralded Fock-State Preparation (Wed 11:30)

`lectures/06_Lab_HeraldedFockStates.ipynb`

**Learning objectives** — students can:
1. simulate a two-mode SPDC source and herald Fock states from it;
2. show that one arm alone is thermal (entanglement seen from one side);
3. characterize heralded states via P(n) and g⁽²⁾(0) and optimize under loss;
4. explain what boson sampling is and why distinguishability switches it off.

**Timing (60 min):**
- 0–8 · From lecture 1's squeezed vacuum to the two-mode squeezed vacuum:
  Σ λⁿ|n,n⟩ in Perceval; pair correlation sanity check.
- 8–14 · E0 (warm-up): the signal marginal is thermal — numerically verify
  Bose–Einstein + g⁽²⁾ = 2 (Tuesday's quiz, closed).
- 14–22 · Worked: ideal PNR herald → perfect |1⟩; why it's too good to be
  true (idler loss, click detectors).
- 22–24 · Loss = beamsplitter to an unwatched mode; lossy herald worked
  example (multi-pair contamination appears).
- 24–42 · **Design challenge** (small groups): click-detector herald,
  η_i = 0.6, knob = λ; plot brightness, purity, FOM; optimal λ; group
  competition with g⁽²⁾(0) < 0.1 constraint; better-detector variant.
- 42–48 · Worked finale: PNR herald on n = 2 → |2⟩ with g⁽²⁾(0) = 1/2
  [Cooper2013].
- 48–56 · **Boson sampling in sixty seconds**: KLM 2001 → Aaronson–Arkhipov
  2011 → Jiuzhang 2020; live demo — 2 photons in a random 4-mode circuit,
  indistinguishable vs distinguishable output distributions
  ("distinguishability is the off-switch").
- 56–60 · Wrap-up: the three-day toolbox table; reading pointers; final
  submission push; FOM winners announced at the discussion session.

---

## Notebook conventions

- Every notebook: title/session header → learning objectives → guarded
  install cell (no-op in Codespaces, installs on Colab) → content.
- Written for physics grad students with *basic* programming background:
  every code cell is commented, no clever one-liners, NumPy-style docstrings
  with units on all helper functions.
- Hands-on notebooks: worked example first, then `# YOUR CODE HERE` cells
  with expected-output hints and graceful self-check cells; sample solutions
  at the bottom of each notebook ("no peeking during the session").
- Plots: labeled axes with units, `figsize=(6,4)`, viridis/cividis.
- Citations: `[Author Year]` inline, resolved in `references.bib`
  (arXiv version where one exists). Local PDFs live in the `.gitignore`d
  `references/` folder.
