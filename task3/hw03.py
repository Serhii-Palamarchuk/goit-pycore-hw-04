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
    try:
        if not path.exists():
            print(Fore.RED + "Вказаний шлях не існує." + Style.RESET_ALL)
            return

        if not path.is_dir():
            print(Fore.RED + "Вказаний шлях не є директорією." + Style.RESET_ALL)
            return
        
        if not indent:
            print(Fore.BLUE + indent + "📦 " + path.name + Style.RESET_ALL)
        for item in path.iterdir():
            if item.is_dir():
                print(Fore.BLUE + indent + " ┣📂 " + item.name + Style.RESET_ALL)
                print_directory_contents(item, indent + " ┃ ")
            else:
                print(Fore.GREEN + indent + " ┣📜 " + item.name + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}" + Style.RESET_ALL)


def main():
    if len(sys.argv) > 1:
        directory_path = Path(sys.argv[1])
        print_directory_contents(directory_path)
    else:
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

