import os

def ls(path='.'):
    for item in os.listdir(path):
        print(item)

if __name__ == "__main__":
    ls()
