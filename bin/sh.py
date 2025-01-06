import bin.registry
import readline

def start_shell():
    print("Welcome to ShSubOS Shell!")
    commands = bin.registry.load_commands()
    while True:
        try:
            command = input("shsubos> ")
            if command == "exit":
                break
            else:
                execute_command(command, commands)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting shell.")
            break

def execute_command(command, commands):
    args = command.split()
    if not args:
        return
    cmd = args[0]
    if cmd in commands:
        commands[cmd].main(args[1:])
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    start_shell()
