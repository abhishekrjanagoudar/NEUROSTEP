from dataclasses import asdict, dataclass
import argparse


@dataclass
class WalkTaskConfig:
    task_name: str = "walk"
    headless: bool = True
    num_envs: int = 512


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Walk task config preview")
    parser.add_argument("--headless", action="store_true", help="Run headless")
    parser.add_argument("--num_envs", type=int, default=WalkTaskConfig.num_envs)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = WalkTaskConfig(headless=args.headless, num_envs=args.num_envs)
    print(asdict(cfg))


if __name__ == "__main__":
    main()
