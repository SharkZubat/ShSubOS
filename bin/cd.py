import os

def cd(path):
    try:
        os.chdir(path)
        print(f"Changed directory to {path}")
    except FileNotFoundError:
        print(f"Directory {path} not found")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        cd(sys.argv[1])
    else:
        print("Usage: cd <path>")
