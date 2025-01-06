import os
import sys

def rm(path):
    try:
        os.remove(path)
        print(f"Removed {path}")
    except FileNotFoundError:
        print(f"File {path} not found")

def main(args):
    if args:
        rm(args[0])
    else:
        print("Usage: rm <path>")

if __name__ == "__main__":
    main(sys.argv[1:])
