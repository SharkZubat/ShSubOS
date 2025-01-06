import os

def cd(path):
    try:
        os.chdir(path)
        print(f"Changed directory to {path}")
    except FileNotFoundError:
        print(f"Directory {path} not found")

def main(args):
    if args:
        cd(args[0])
    else:
        print("Usage: cd <path>")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
