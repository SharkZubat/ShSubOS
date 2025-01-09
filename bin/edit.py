import sys
import termios
import tty

def get_input():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch == '\x13':  # Ctrl+S
                break
            yield ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def edit(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    print("Type your text below. Press 'Ctrl+S' to save and exit.")
    
    buffer = []
    for ch in get_input():
        if ch == '\n':
            buffer.append(''.join(buffer) + '\n')
            buffer = []
        else:
            buffer.append(ch)
        sys.stdout.write(ch)
        sys.stdout.flush()

    with open(file_path, 'w') as file:
        file.writelines(lines + buffer)

def main(args):
    if len(args) != 1:
        print("Usage: edit <filename>")
        return
    
    edit(args[0])

if __name__ == "__main__":
    main(sys.argv[1:])
