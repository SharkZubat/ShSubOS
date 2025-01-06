import os
import sys

def help():
    bin_path = os.path.dirname(os.path.realpath(__file__))
    commands = [f[:-3] for f in os.listdir(bin_path) if f.endswith('.py') and f not in ['registry.py', 'sh.py']]

    # Define usage for each command
    commands_usage = {
        "ls": "ls [path]",
        "cd": "cd <path>",
        "cp": "cp <source> <destination>",
        "mv": "mv <source> <destination>",
        "rm": "rm <path>",
        "help": "help",
        "echo": "echo [text]"
        # Add more commands and their usages here
    }

    print("Available commands:")
    for command in commands:
        usage = commands_usage.get(command, f"{command} [args]")
        print(f"{command}: {usage}")

def main(args):
    help()

if __name__ == "__main__":
    main(sys.argv[1:])
