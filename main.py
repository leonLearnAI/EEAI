"""CLI entry point for running EEAI architecture experiments."""

import argparse

from controller import run_architecture
from src.architectures.choice1_chained import print_choice1_summary


def build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(
		description="Run EEAI architecture experiments from the command line."
	)
	parser.add_argument(
		"--arch",
		choices=["choice1", "choice2"],
		default="choice1",
		help="Architecture to run.",
	)
	parser.add_argument(
		"--model",
		choices=["rf", "lr"],
		default="rf",
		help="Model family to use.",
	)
	parser.add_argument(
		"--export",
		default="",
		help="Optional CSV export path for summarized metrics.",
	)
	return parser


def main():
	parser = build_parser()
	args = parser.parse_args()

	print(f"Starting run: arch={args.arch}, model={args.model}")
	export_path = args.export if args.export else None
	result = run_architecture(
		arch=args.arch,
		model_name=args.model,
		export_path=export_path,
	)

	if args.arch == "choice1" and isinstance(result, dict) and "type2" in result:
		print_choice1_summary(result)
	else:
		print(result)

	print("Run finished.")


if __name__ == "__main__":
	main()
