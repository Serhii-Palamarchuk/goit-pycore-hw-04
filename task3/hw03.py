# Завдання 3
# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, 
# виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.

# Перед виконанням віртуальне середовище + colorama:
# python -m venv env
# .\.venv\Scripts\activate.bat
# pip install colorama


import sys
from pathlib import Path
from colorama import Fore, Style

def print_directory_contents(path, indent=""):
    """
    Recursively prints the contents of a directory.

    Args:
        path (Path): The path to the directory.
        indent (str, optional): The indentation string. Defaults to "".
    """
    try:
        # Check if the path exists
        if not path.exists():
            print(Fore.RED + "Вказаний шлях не існує." + Style.RESET_ALL)
            return

        # Check if the path is a directory
        if not path.is_dir():
            print(Fore.RED + "Вказаний шлях не є директорією." + Style.RESET_ALL)
            return
        
        # Print the directory name
        if not indent:
            print(Fore.BLUE + indent + "📦 " + path.name + Style.RESET_ALL)
        
        # Iterate over the items in the directory
        for item in path.iterdir():
            if item.is_dir():
                # Print the subdirectory name
                print(Fore.BLUE + indent + " ┣📂 " + item.name + Style.RESET_ALL)
                # Recursively print the contents of the subdirectory
                print_directory_contents(item, indent + " ┃ ")
            else:
                # Print the file name
                print(Fore.GREEN + indent + " ┣📜 " + item.name + Style.RESET_ALL)
    except Exception as e:
        # Print the error message
        print(Fore.RED + f"Помилка: {e}" + Style.RESET_ALL)


def main():
    """
    Entry point of the program.
    
    If a directory path is provided as a command-line argument, it prints the contents of the directory.
    Otherwise, it displays an error message.
    """
    # Check if a directory path is provided as a command-line argument
    if len(sys.argv) > 1:
        directory_path = Path(sys.argv[1])
        # Print the contents of the directory
        print_directory_contents(directory_path)
    else:
        # Display an error message if no directory path is provided
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії як аргумент." + Style.RESET_ALL)

if __name__ == "__main__":
    # main()
    print_directory_contents(Path('G:/My Drive/GoIT/Python/goit-pycore-hw-03'))

# Приклад використання: Якщо виконати скрипт та передати йому абсолютний шлях до директорії як параметр
# python hw03.py /шлях/до/вашої/директорії

# python hw03.py "G:/My Drive/GoIT/Python/goit-pycore-hw-04/task3"
# python hw03.py 'G:/My Drive/GoIT/Python/goit-pycore-hw-04/task3/.venv/Scripts'
# python hw03.py "G:/My Drive/GoIT/Python/goit-pycore-hw-04/task2"
# python hw03.py 'G:/My Drive/GoIT/Python/goit-pycore-hw-03'

