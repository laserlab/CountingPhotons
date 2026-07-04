# Lecture Plan — Counting Photons

ICTP-SAIFR school, IFT–UNESP São Paulo · July 27–29, 2026 · Tim Thomay

**Audience:** physics graduate students. Quantum mechanics is assumed
(operators, Hilbert spaces, harmonic oscillator); quantum *optics* is not.
Basic programming skills are assumed; all code is heavily commented and every
hands-on notebook starts from a worked example before asking for student code.

**Format:** 6 × 1 h. Each day pairs a lecture with a hands-on session;
Wednesday is a single 2 h simulation lab. All materials are Jupyter notebooks
that run in GitHub Codespaces (preferred) or Google Colab.

---

## 0 — Setup (at home, before the school, ~20 min)

`lectures/00_Setup_GitHub_Codespaces.ipynb`

**Goal:** every student arrives Monday with a working environment.

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
1. explain why photon-number statistics distinguish light sources that have
   identical average intensity;
2. write down P(n) for coherent, thermal, and Fock states;
3. compute and interpret the Mandel Q parameter.

**Timing (60 min):**
- 0–10 · Motivation: three lasers pointers walk into a bar — same brightness,
  different physics. What a photon counter actually records (click streams).
- 10–25 · The quantized field mode in one slide chain: â, â†, n̂; Fock states
  |n⟩ as the number basis; coherent states |α⟩ as the "most classical" states;
  thermal states as the maximum-entropy mixed state.
- 25–40 · Photon number distributions: Poisson vs Bose–Einstein vs δₙ,ₘ —
  live plots at equal ⟨n⟩; photon-number variance; Mandel Q; sub-Poissonian
  light as a non-classicality witness (no classical intensity distribution
  can do Q < 0).
- 40–50 · Where each lives in the lab: laser, filtered lamp / rotating ground
  glass, single emitters. First look at real click data.
- 50–60 · Check-your-understanding questions + buffer.

**Key figures (all generated in-notebook):** P(n) comparison at ⟨n⟩ = 4;
variance vs mean for the three families; Mandel Q vs mean thermal/coherent.

---

## 2 — Hands-on: Simulating Photon Statistics (hands-on, Mon 14:00)

`lectures/02_HandsOn_SimulatingPhotonStatistics.ipynb`

**Learning objectives** — students can:
1. build coherent/thermal/Fock states in QuTiP and extract P(n), ⟨n⟩, Δn²;
2. Monte-Carlo sample detector clicks from a photon-number distribution;
3. show numerically what optical loss does to sub-Poissonian statistics.

**Timing (60 min):**
- 0–10 · Everyone running: Codespace check, fork check (00 notebook is the
  reference). Helpers circulate.
- 10–20 · Worked example: `coherent(N, alpha)`, `thermal_dm(N, nbar)`,
  `fock(N, n)`; extracting P(n) from the density matrix diagonal.
- 20–45 · Exercises (in pairs):
  - E1: reproduce the equal-⟨n⟩ P(n) figure from Lecture 1
  - E2: Mandel Q function + test on all three states
  - E3: sample 10 000 "clicks" from P(n), recompute Q from the sample —
    statistics of estimating statistics
- 45–60 · Stretch: beamsplitter loss model (Fock state through transmission
  η) — watch Q rise toward 0; discussion of why loss "classicalizes".

---

## 3 — Correlations: g⁽²⁾, HBT, and How We Make & Catch Photons (lecture, Tue 9:00)

`lectures/03_Correlations_Generation_Detection.ipynb`

**Learning objectives** — students can:
1. define g⁽²⁾(τ) and state its value at τ=0 for coherent, thermal, Fock;
2. explain why the HBT beamsplitter geometry measures g⁽²⁾ despite detector
   dead time;
3. compare single-photon sources (attenuated laser, heralded SPDC, quantum
   emitters) and detectors (SPAD, SNSPD, TES) by the numbers that matter.

**Timing (60 min):**
- 0–10 · Recap via quiz; the limit of P(n): it says nothing about *time*.
- 10–25 · Intensity correlations: classical g⁽²⁾ ≥ 1 (Cauchy–Schwarz), quantum
  g⁽²⁾(0) = 1 − 1/n for |n⟩; bunching vs antibunching; g⁽²⁾(τ) shapes.
- 25–35 · Hanbury Brown & Twiss: from stellar diameters (1956) to the
  workhorse of single-photon characterization; why one detector + dead time
  fails and a 50:50 beamsplitter + start–stop coincidences works; higher-order
  g⁽ⁿ⁾ and multiplexed HBT.
- 35–48 · Generation: attenuated laser is *still Poissonian* (the g⁽²⁾ proof);
  SPDC pairs + heralding; quantum dots and color centers; source figures of
  merit (purity, indistinguishability, brightness).
- 48–58 · Detection: SPAD, SNSPD, TES; click vs photon-number-resolving;
  efficiency / dark counts / jitter / dead time table; PNR by multiplexing.
- 58–60 · Bridge to the afternoon: "you get three mystery click streams."

---

## 4 — Hands-on: g⁽²⁾ from Click Data (Tue 10:30)

`lectures/04_HandsOn_g2_HBT.ipynb`

**Learning objectives** — students can:
1. compute g⁽²⁾(τ) from raw time tags via a coincidence histogram;
2. classify unknown sources by their photon statistics;
3. quantify how background counts degrade an antibunching dip.

**Timing (60 min):**
- 0–10 · The dataset: `data/source_A/B/C_timetags.npz` — HBT time tags
  (detector 1 & 2 arrival times) from three unlabeled simulated sources.
  Worked example: coincidence histogram for source A.
- 10–40 · Exercises:
  - E1: g⁽²⁾(τ) for all three sources; normalize by the uncorrelated rate
  - E2: identify which is coherent / thermal / single-emitter, with evidence
  - E3: g⁽²⁾(0) vs background-count fraction — when does a single-photon
    source stop looking "single" (g⁽²⁾(0) < 0.5 criterion)?
- 40–50 · Cross-check in QuTiP: g⁽²⁾(0) = ⟨â†â†ââ⟩/⟨â†â⟩² for the matching
  states — theory vs "measured" estimate on one plot.
- 50–60 · First submission: push completed notebook to
  `submissions/<username>/` (walkthrough on screen).

**Provided:** `data/make_timetags.py` (seeded, committed) generates the
datasets; students may re-generate with different parameters.

---

## 5 — Lab: Hong–Ou–Mandel Interference in Perceval (Wed 10:30)

`lectures/05_Lab_HOM_Interference.ipynb`

**Learning objectives** — students can:
1. build and sample a linear-optical circuit in Perceval;
2. predict and verify the two-photon output distribution of a 50:50
   beamsplitter (|2,0⟩ + |0,2⟩, no coincidences);
3. simulate a HOM dip and extract its visibility.

**Timing (60 min):**
- 0–15 · Perceval crash course (worked, run-along): `BasicState`, `Circuit`,
  `BS`/`PS`, `Processor` + sampling; single photon on a beamsplitter first.
- 15–30 · The HOM effect: send |1,1⟩ into a 50:50 BS; where did the
  coincidences go? The two-amplitude cancellation, drawn and simulated.
- 30–50 · Exercises:
  - E1: coincidence probability vs beamsplitter reflectivity (analytic
    (R−T)² overlay)
  - E2: HOM dip — coincidences vs photon distinguishability (delay); dip
    visibility; partially distinguishable photons
- 50–60 · Why this matters: HOM visibility as *the* source-quality benchmark;
  two-photon gates in photonic QC rest on this interference.

---

## 6 — Lab: Heralded Fock-State Preparation (Wed 11:30)

`lectures/06_Lab_HeraldedFockStates.ipynb`

**Learning objectives** — students can:
1. simulate a two-mode SPDC-like source and herald Fock states from it;
2. characterize a heralded state via P(n) and g⁽²⁾(0);
3. optimize a heralded source under loss with a quantitative figure of merit.

**Timing (60 min):**
- 0–10 · From lecture 3 to code: two-mode squeezed vacuum Σ λⁿ|n,n⟩; detect
  n photons in the idler ⇒ project the signal onto |n⟩.
- 10–25 · Worked example: heralded single photon — P(n|herald), heralded
  g⁽²⁾(0), heralding rate vs squeezing parameter (the brightness/purity
  trade-off: higher pump ⇒ more multi-pair events).
- 25–45 · Mini-challenge (small groups): add idler loss + a click (non-PNR)
  herald detector; maximize (heralding efficiency × single-photon purity);
  leaderboard of best figures of merit.
- 45–55 · PNR heralding: with a number-resolving idler detector, herald
  |2⟩ — verify with g⁽²⁾(0) = 1/2.
- 55–60 · Wrap-up: from these parts (sources + BS + PNR detection) to boson
  sampling and measurement-based photonic QC; reading pointers; final push
  of student work.

---

## Notebook conventions

- Every notebook: title/session header → learning objectives → guarded
  install cell (no-op in Codespaces, installs on Colab) → content.
- Written for physics grad students with *basic* programming background:
  every code cell is commented, no clever one-liners, NumPy-style docstrings
  with units on all helper functions.
- Hands-on notebooks: worked example first, then `# YOUR CODE HERE` cells
  with expected-output hints and light asserts; stretch goals at the end.
- Plots: labeled axes with units, `figsize=(6,4)`, viridis/cividis.
- Citations: `[Author Year]` inline, resolved in `references.bib`
  (arXiv version where one exists). Local PDFs live in the `.gitignore`d
  `references/` folder.
