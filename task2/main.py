# Завдання 2
# У вас є текстовий файл, який містить інформацію про котів. 
# Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.

import pathlib

def get_cats_info(path):
    """
    Retrieves information about cats from a text file.

    Args:
        path (str): The path to the text file.

    Returns:
        list: A list of dictionaries containing the cat's id, name, and age.

    Raises:
        FileNotFoundError: If the file is not found.
        Exception: If there is an error processing the file.
    """
    try:
        cats = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split the line by comma to get the cat's id, name, and age
                id, name, age = line.strip().split(',')
                # Create a dictionary with the cat's information and append it to the list
                cats.append({"id": id, "name": name, "age": age})
        return cats
    except FileNotFoundError:
        # If the file is not found, print an error message and return an empty list.
        print("Файл не знайдено.")
        return []
    except Exception as e:
        # If there is an error processing the file, print the error message and return an empty list.
        print(f"Помилка при обробці файлу: {e}")
        return []

# Приклад використання функції
if __name__ == "__main__":
    current_dir = pathlib.Path(__file__).parent
    path = current_dir / "cats.txt"
    cats_info = get_cats_info(path)
    print(cats_info)