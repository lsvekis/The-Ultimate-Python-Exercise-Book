# Save as flag_example.py:
import argparse

parser = argparse.ArgumentParser(description="A flag example.")
parser.add_argument("--verbose", action="store_true", help="Increase output verbosity")
args = parser.parse_args()
if args.verbose:
print("Verbose mode is on.")
else:
print("Verbose mode is off.")
