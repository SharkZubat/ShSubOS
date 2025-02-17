import shutil
import sys

def cp(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Copied {source} to {destination}")
    except FileNotFoundError:
        print(f"File {source} not found")

def main(args):
    if len(args) > 1:
        cp(args[0], args[1])
    else:
        print("Usage: cp <source> <destination>")

if __name__ == "__main__":
    main(sys.argv[1:])
