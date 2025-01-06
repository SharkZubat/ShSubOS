import shutil
import sys

def mv(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved {source} to {destination}")
    except FileNotFoundError:
        print(f"File {source} not found")

def main(args):
    if len(args) > 1:
        mv(args[0], args[1])
    else:
        print("Usage: mv <source> <destination>")

if __name__ == "__main__":
    main(sys.argv[1:])
