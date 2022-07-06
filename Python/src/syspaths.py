import sys


def ShowSysPaths():
    """
        Prints the paths python can access.
    """
    paths = sys.path
    for item in paths:
        print(item)


if __name__ == '__main__':
    ShowSysPaths()
