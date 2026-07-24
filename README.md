# Counting Photons

> [!WARNING]
> **Work in progress.** These materials are being actively revised and will
> keep changing until the lectures begin (July 27, 2026). Feel free to look
> around — but expect things to move, and hold off on forking until the
> school starts.

**Quantum Light, Fock States, and Hands-on Photonic Quantum Computing**

Lecture materials by [Tim Thomay](https://github.com/laserlab) for the
ICTP-SAIFR school, IFT–UNESP São Paulo, July 27–29, 2026.

> This lecture introduces experimental quantum optics through the lens of
> photon statistics, from classical coherent and thermal light to
> non-classical states, with focus on Fock states and higher-order photon
> correlations. We will cover how such states are generated and how they are
> detected and characterized, including g⁽ⁿ⁾ measurements, Hanbury Brown–Twiss
> setups, and photon-number-resolving detectors. The interactive sessions will
> use a photonic quantum computing framework to let students design and run
> linear-optical experiments such as HOM interference and heralded Fock-state
> preparation.

## Schedule

| # | When | Notebook | Format |
|---|------|----------|--------|
| 0 | announced Monday | [00_Setup_GitHub_Codespaces](lectures/00_Setup_GitHub_Codespaces.ipynb) | standalone setup, do Monday evening (~20 min) |
| 1 | Mon Jul 27, 11:30 | [01_QuantumLight_PhotonStatistics](lectures/01_QuantumLight_PhotonStatistics.ipynb) | lecture |
| 2 | Mon Jul 27, 14:00 | [02_HandsOn_SimulatingPhotonStatistics](lectures/02_HandsOn_SimulatingPhotonStatistics.ipynb) | lecture · live demo |
| 3 | Tue Jul 28, 9:00 | [03_Correlations_Generation_Detection](lectures/03_Correlations_Generation_Detection.ipynb) | lecture |
| 4 | Tue Jul 28, 10:30 | [04_HandsOn_g2_HBT](lectures/04_HandsOn_g2_HBT.ipynb) | hands-on |
| 5 | Wed Jul 29, 10:30 | [05_Lab_HOM_Interference](lectures/05_Lab_HOM_Interference.ipynb) | lab |
| 6 | Wed Jul 29, 11:30 | [06_Lab_HeraldedFockStates](lectures/06_Lab_HeraldedFockStates.ipynb) | lab |


## Running the notebooks

**Recommended: GitHub Codespaces** (nothing to install)

1. Fork this repository (button top right).
2. On *your fork*: **Code ▸ Codespaces ▸ Create codespace on main**.
3. Wait for the container to build (~2 min, one time), open a notebook in
   `lectures/`, select the **Python 3 (ipykernel)** kernel (`/usr/local/bin/python`,
   not the bare `/bin/python3`), run.

**Alternative: Google Colab**

Open [colab.research.google.com](https://colab.research.google.com),
*File ▸ Open notebook ▸ GitHub*, paste your fork's URL, and pick a notebook.
The first code cell of every notebook installs the required packages.

**Alternative: your own machine**

```bash
git clone https://github.com/<your-username>/CountingPhotons
cd CountingPhotons
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements/requirements.txt
jupyter lab
```

(On macOS, after the one-time setup you can simply double-click
`start_lectures.command` — it launches JupyterLab from the bundled
environment and works fully offline.)

## References

All papers cited in the lectures are collected in
[references.bib](references.bib), with arXiv links where available. If you
want the PDFs locally, put them in a `references/` folder — it is
`.gitignore`d, so they never end up in the repository.

## Resources

- [Perceval documentation](https://perceval.quandela.net/docs/) — the photonic QC framework used in Lectures 5–6
- [QuTiP documentation](https://qutip.readthedocs.io/) — used in Lectures 2 and 4
- [QuantumOptics.jl](https://qojulia.org) — the Julia sibling of QuTiP, used in Helmut Ritsch's lectures at this school; concepts transfer 1:1
- [PHY386 — Computational Methods for Physicists](https://github.com/ubsuny/PHY386) — my UB course; self-paced Python/Jupyter/plotting basics if you want a gentler computational on-ramp
- [GitHub docs: forking](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [Getting started with Codespaces](https://docs.github.com/en/codespaces/getting-started/quickstart)

## License

Dual-licensed, following standard open-courseware practice:

- **Lecture content** © 2026 Tim Thomay — prose, the lecture plan, and
  course-generated figures: [CC BY 4.0](LICENSE)
- **Code** © 2026 Tim Thomay — the `.py` files (`lectures/sketches.py`,
  `data/make_timetags.py`), notebook code cells, and configuration
  (`.devcontainer/`, `requirements/`): [MIT](LICENSE-CODE)

Third-party photographs in `figures/` retain their own licenses, listed in
[figures/FIGURES_CREDITS.md](figures/FIGURES_CREDITS.md).

**Citing:** if you build on these materials in teaching or research, please
cite this repository (see [CITATION.cff](CITATION.cff) — GitHub renders it
as a "Cite this repository" button in the sidebar).
