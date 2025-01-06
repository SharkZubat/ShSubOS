import shutil
import sys

def cp(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Copied {source} to {destination}")
    except FileNotFoundError:
        print(f"File {source} not found")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        cp(sys.argv[1], sys.argv[2])
    else:
        print("Usage: cp <source> <destination>")
