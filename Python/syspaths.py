import sys


def ShowSysPaths():
    """
        Show the paths that python can access.
    """
    paths = sys.path
    for item in paths:
        print(item)


if __name__ == '__main__':
    ShowSysPaths()
