import sys
import termios
import tty
import os

def get_input():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch == '\x13':  # Ctrl+S
                return
            yield ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def edit(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    cursor_x, cursor_y = 0, 0
    buffer = lines.copy()

    while True:
        os.system('clear')
        for line in buffer:
            print(line, end='')

        print(f"\033[{cursor_y+1};{cursor_x+1}H", end='')  # Move cursor

        ch = next(get_input())
        if ch == '\x13':  # Ctrl+S
            break

        if ch == '\x1b[A':  # Up arrow
            cursor_y = max(0, cursor_y - 1)
        elif ch == '\x1b[B':  # Down arrow
            cursor_y = min(len(buffer) - 1, cursor_y + 1)
        elif ch == '\x1b[C':  # Right arrow
            cursor_x = min(len(buffer[cursor_y]) - 1, cursor_x + 1)
        elif ch == '\x1b[D':  # Left arrow
            cursor_x = max(0, cursor_x - 1)
        elif ch == '\n':
            buffer.insert(cursor_y + 1, '')
            cursor_y += 1
            cursor_x = 0
        elif ch == '\x7f':  # Backspace
            if cursor_x > 0:
                buffer[cursor_y] = buffer[cursor_y][:cursor_x-1] + buffer[cursor_y][cursor_x:]
                cursor_x -= 1
            elif cursor_y > 0:
                cursor_x = len(buffer[cursor_y-1])
                buffer[cursor_y-1] += buffer.pop(cursor_y)
                cursor_y -= 1
        else:
            buffer[cursor_y] = buffer[cursor_y][:cursor_x] + ch + buffer[cursor_y][cursor_x:]
            cursor_x += 1

    with open(file_path, 'w') as file:
        file.writelines(buffer)

def main(args):
    if len(args) != 1:
        print("Usage: edit <filename>")
        return

    edit(args[0])

if __name__ == "__main__":
    main(sys.argv[1:])
