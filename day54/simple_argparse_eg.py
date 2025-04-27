import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="A simple argument parser example")

# Define arguments
parser.add_argument("name", type=str, help="Your name")
parser.add_argument("age", type=int, help="Your age")

# Parse the arguments
args = parser.parse_args()

# Use the parsed arguments
print(f"Hello {args.name}, you are {args.age} years old!")
