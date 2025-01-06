import os

def ls(path='.'):
    for item in os.listdir(path):
        print(item)

def main(args):
    path = args[0] if args else '.'
    ls(path)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
