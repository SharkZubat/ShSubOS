# boot/default.py
import bin.sh

def boot():
    print("Booting in default mode...")
    bin.sh.start_shell()

if __name__ == "__main__":
    boot()
