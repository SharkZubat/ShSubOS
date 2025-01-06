import os
import importlib

def load_commands():
    commands = {}
    bin_path = os.path.join(os.path.dirname(__file__), 'bin')
    for file in os.listdir(bin_path):
        if file.endswith('.py') and file != 'registry.py':
            command_name = file[:-3]
            module_name = f'bin.{command_name}'
            module = importlib.import_module(module_name)
            commands[command_name] = module
    return commands

if __name__ == "__main__":
    commands = load_commands()
    for command in commands:
        print(f"Loaded command: {command}")
