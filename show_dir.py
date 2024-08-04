import sys
from pathlib import Path
from colorama import Fore

def show_dir(path: Path, level = 0):
    if not path.exists():
        print('Directory not found')
        return

    if not path.is_dir():
        print('Path is not a directory')
        return

    for item in path.iterdir():
        if (item.is_file()):
            print(f'{Fore.GREEN}{' ' * 4 * level}{item.name}')
        else:
            print(f'{Fore.BLUE}{' ' * 4 * level}{item.name}/')
            show_dir(item, level + 1)

def main():
    dir_path = sys.argv[1]

    show_dir(Path(dir_path))

if __name__ == '__main__':
    main()
