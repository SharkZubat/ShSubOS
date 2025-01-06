# bin/echo.py
# This script will handle the 'echo' command.

def echo(args):
    print(" ".join(args))

if __name__ == "__main__":
    import sys
    echo(sys.argv[1:])
