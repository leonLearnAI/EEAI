"""CLI entry point for running EEAI architecture experiments."""

import argparse

from controller import run_architecture


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
	return parser


def main():
	pass
