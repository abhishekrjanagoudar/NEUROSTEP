#!/usr/bin/env python3
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export policy scaffold")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--num_envs", type=int, default=1)
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--format", choices=["onnx", "torchscript"], default="onnx")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(
        "Export scaffold only. "
        f"headless={args.headless}, num_envs={args.num_envs}, checkpoint={args.checkpoint}, format={args.format}"
    )


if __name__ == "__main__":
    main()
