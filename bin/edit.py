import sys

def edit(args):
    if len(args) < 2:
        print("Usage: edit <filename> <text>")
        return

    file_path = args[0]
    text = " ".join(args[1:])

    with open(file_path, 'a') as file:
        file.write(text + "\n")

def main(args):
    edit(args)

if __name__ == "__main__":
    main(sys.argv[1:])
