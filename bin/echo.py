# bin/echo.py
def echo(args):
    print(" ".join(args))

def main(args):
    echo(args)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
