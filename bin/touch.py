import os

def touch(args):
    for file_path in args:
        with open(file_path, 'a'):
            os.utime(file_path, None)

def main(args):
    if not args:
        print("Usage: touch <filename>")
        return
    
    touch(args)
    for file_path in args:
        print(f"Updated timestamp of {file_path}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
