#!/usr/bin/env python3
"""CLI entrypoint to launch Isaac Lab RSL-RL training."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch Isaac Lab training")
    parser.add_argument("--task", default="Isaac-Ant-v0", help="Isaac Lab task name")
    parser.add_argument("--num_envs", type=int, default=4096, help="Parallel env count")
    parser.add_argument("--headless", action="store_true", help="Run without display")
    parser.add_argument(
        "--isaaclab_root",
        default=os.environ.get("ISAACLAB_ROOT", "/workspace/IsaacLab"),
        help="Path to IsaacLab clone",
    )
    parser.add_argument(
        "--python_executable",
        default=sys.executable,
        help="Python executable used to run Isaac Lab train script",
    )
    parser.add_argument(
        "--extra_args",
        nargs=argparse.REMAINDER,
        help="Additional args forwarded to Isaac Lab train.py",
    )
    return parser.parse_args()


def build_command(args: argparse.Namespace) -> list[str]:
    train_script = (
        Path(args.isaaclab_root)
        / "scripts"
        / "reinforcement_learning"
        / "rsl_rl"
        / "train.py"
    )
    if not train_script.exists():
        raise FileNotFoundError(
            "Isaac Lab training script not found at "
            f"{train_script}. Set --isaaclab_root or ISAACLAB_ROOT correctly."
        )

    cmd = [
        args.python_executable,
        str(train_script),
        "--task",
        args.task,
        "--num_envs",
        str(args.num_envs),
    ]
    if args.headless:
        cmd.append("--headless")
    if args.extra_args:
        cmd.extend(args.extra_args)
    return cmd


def main() -> int:
    args = parse_args()
    cmd = build_command(args)
    print("Launching:", " ".join(cmd))
    completed = subprocess.run(cmd, check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
