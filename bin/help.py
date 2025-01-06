import os
import sys

def help():
    bin_path = os.path.dirname(os.path.realpath(__file__))
    commands = [f[:-3] for f in os.listdir(bin_path) if f.endswith('.py') and f != 'registry.py']
    print("Available commands:")
    for command in commands:
        print(command)

def main(args):
    help()

if __name__ == "__main__":
    main(sys.argv[1:])
