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
            if ch == '\x1b':  # Start of an escape sequence
                seq = sys.stdin.read(2)
                ch += seq
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
    cursor_x, cursor_y = 0, 0
    for ch in get_input():
        if ch == '\n':
            buffer.append('\n')
            cursor_y += 1
            cursor_x = 0
        elif ch == '\x1b[A':  # Up arrow
            cursor_y = max(0, cursor_y - 1)
        elif ch == '\x1b[B':  # Down arrow
            cursor_y = min(len(buffer) - 1, cursor_y + 1)
        elif ch == '\x1b[C':  # Right arrow
            cursor_x = min(len(buffer[cursor_y]) - 1, cursor_x + 1)
        elif ch == '\x1b[D':  # Left arrow
            cursor_x = max(0, cursor_x - 1)
        else:
            buffer.append(ch)
            cursor_x += 1
        sys.stdout.write(ch)
        sys.stdout.flush()

    with open(file_path, 'w') as file:
        file.truncate(0)  # Clear the file's existing bytes
        file.writelines(buffer)

def main(args):
    if len(args) != 1:
        print("Usage: edit <filename>")
        return
    
    edit(args[0])

if __name__ == "__main__":
    main(sys.argv[1:])
