# NEUROSTEP

Humanoid locomotion RL research scaffold using NVIDIA Isaac Sim + Isaac Lab + RSL-RL.

## Repository Layout

```
configs/
envs/
rewards/
scripts/
checkpoints/
logs/
docs/
```

## Environment Setup

### Option A: Docker

```bash
docker build -t neurostep .
```

### Option B: Conda

```bash
conda env create -f environment.yml
conda activate neurostep
```

> Note: Isaac Lab itself is expected to be installed separately (or via Dockerfile), and exposed via `ISAACLAB_ROOT`.

## Validate End-to-End Pipeline with Stock Demo Task

Launch the stock Isaac Lab RSL-RL Ant task in headless mode:

```bash
python /home/runner/work/NEUROSTEP/NEUROSTEP/scripts/train.py --task Isaac-Ant-v0 --headless --num_envs 4096
```

If Isaac Lab is installed at a non-default path:

```bash
ISAACLAB_ROOT=/path/to/IsaacLab python /home/runner/work/NEUROSTEP/NEUROSTEP/scripts/train.py --task Isaac-Ant-v0 --headless --num_envs 4096
```
