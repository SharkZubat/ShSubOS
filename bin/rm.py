import os
import sys

def rm(path):
    try:
        os.remove(path)
        print(f"Removed {path}")
    except FileNotFoundError:
        print(f"File {path} not found")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        rm(sys.argv[1])
    else:
        print("Usage: rm <path>")
