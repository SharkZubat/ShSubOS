import os
import subprocess
import sys

def main(args):
    if len(args) < 1:
        print("Usage: shs <script.shs>")
        return

    script_path = args[0]
    if not os.path.isfile(script_path):
        print(f"Error: {script_path} does not exist.")
        return

    try:
        subprocess.run(['bash', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while executing {script_path}: {e}")

if __name__ == "__main__":
    main(sys.argv[1:])
