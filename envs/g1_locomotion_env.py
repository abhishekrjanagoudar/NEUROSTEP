import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="G1 locomotion env scaffold")
    parser.add_argument("--headless", action="store_true", help="Run headless")
    parser.add_argument("--num_envs", type=int, default=4096)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(
        "G1 locomotion env scaffold only. "
        f"headless={args.headless}, num_envs={args.num_envs}"
    )


if __name__ == "__main__":
    main()
