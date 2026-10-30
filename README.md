# from-static-unet

**Diffusion from scratch.** A small DDPM U-Net on MNIST and Fashion-MNIST: how does a model turn pure noise into an image?

**Status:** not started.

## Question

How does a model turn pure noise into an image, and what does its noise space look like?

## Plan

- **Architecture:** a small U-Net with a timestep embedding, trained as DDPM (1000 noise steps, cosine schedule), with DDIM sampling for speed.
- **Data:** MNIST first, then Fashion-MNIST.

## Experiments

- Strips showing an image emerging step by step.
- Class-conditional generation with classifier-free guidance.
- Interpolation between two noise seeds.

## Done when

- Samples are clearly recognizable, and the README shows the denoising trajectory figure.

Plus the general checklist:

Apply this checklist with the project-specific requirements and exceptions in
[CLAUDE.md](CLAUDE.md#project-specific-scope).

- `just quick` runs end to end on CPU in under 5 minutes, as a smoke test.
- The full run fits on one consumer GPU (8–12 GB VRAM) and auto-detects cuda, mps or cpu.
- Each run saves weights, `metrics.json` and its plots to `runs/<run-name>/`.
- This README shows the headline result with plots, compares against baselines, and states negative results plainly.
- Tests cover data generators, tensor shapes and one tiny overfit check.

## Quickstart

Needs [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/). Everything else, Python 3.12 included, comes from uv.

```sh
just setup              # uv sync, then install the pre-commit hooks
just quick              # CPU smoke test, under 5 minutes
just train              # full run; flags pass through, e.g. --run-name wd1.0-seed0
just analyze <run>      # baselines, probes, interventions and plots
just cloud <sweep>      # the same runs on Modal, one GPU each; see .agents/instructions/cloud.md
just test               # pytest
just check              # ruff and basedpyright, as in CI
```

Copy `.env.example` to `.env` (gitignored) for `HF_TOKEN` and `HF_USER`.

## Layout

```
from-static-unet/
├── README.md                goal, plan, results with plots
├── CLAUDE.md                instructions for coding agents; AGENTS.md points here
├── .agents/                 instructions/ (Python formatting, commits) and plans/
├── pyproject.toml           metadata, dependencies, tool settings
├── uv.lock                  committed lockfile
├── .python-version          pinned by uv
├── justfile                 every routine command
├── .pre-commit-config.yaml
├── .github/workflows/ci.yml
├── src/from_static_unet/
│   └── model.py, data.py, analysis.py, utils.py
├── train.py                 CLI; --quick runs the CPU smoke test
├── predict.py               load weights and run inference
├── analyze.py               baselines, probes, interventions, plots
├── cloud.py                 the same runs on Modal, one GPU per run
├── figures/                 README figures: LaTeX sources, data and built PNGs
├── notebooks/               marimo notebooks for exploration
├── tests/
└── runs/                    outputs, gitignored
```

## Results

_No results yet._ The headline result with plots, the comparison against baselines, and any negative results go here.

## Sources

- Ho et al. 2020, DDPM
- Song et al. 2020, DDIM

## License

MIT
