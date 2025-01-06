import os

def boot_shsub_os():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("Booting ShSubOS...")
    try:
        with open("boot/bootmode", "r") as f:
            mode = f.read().strip()
            if mode == "def":
                import boot.default as default_boot
                default_boot.boot()
            else:
                print(f"Unknown boot mode: {mode}")
    except FileNotFoundError:
        print("boot/bootmode file not found. Booting in default mode.")
        import boot.default as default_boot
        default_boot.boot()

if __name__ == "__main__":
    boot_shsub_os()
