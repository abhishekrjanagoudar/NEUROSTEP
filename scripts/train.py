#!/usr/bin/env python3
"""CLI entrypoint to launch Isaac Lab training."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch Isaac Lab training")
    parser.add_argument("--task", default="Isaac-Ant-v0", help="Isaac Lab task name")
    parser.add_argument("--num_envs", type=int, default=512, help="Parallel env count")
    parser.add_argument("--headless", action="store_true", help="Run without display")
    parser.add_argument(
        "--rl_library",
        default="skrl",
        help="Isaac Lab RL launcher subdirectory (for example: skrl or rsl_rl)",
    )
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
        / args.rl_library
        / "train.py"
    )
    if not train_script.exists():
        raise FileNotFoundError(
            f"Isaac Lab training script for --rl_library '{args.rl_library}' was not found at "
            f"{train_script}. Set --rl_library to a valid launcher subdirectory or update "
            "--isaaclab_root/ISAACLAB_ROOT."
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
    try:
        cmd = build_command(args)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print("Launching:", " ".join(cmd))
    completed = subprocess.run(cmd, check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
