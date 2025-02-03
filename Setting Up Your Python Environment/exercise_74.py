# Save as optional_args.py:
import argparse

parser = argparse.ArgumentParser(description="Greet the user.")
parser.add_argument("--name", type=str, default="User", help="The name of the user")
args = parser.parse_args()
print(f"Hello, {args.name}!")
