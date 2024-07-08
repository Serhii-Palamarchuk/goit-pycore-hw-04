# Завдання 1
# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. 
# Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

import pathlib

def total_salary(path):
	"""
	Calculate the total salary and average salary from a file.

	Args:
		path (str): The path to the file containing salary data.

	Returns:
		tuple: A tuple containing the total salary and average salary.

	Raises:
		FileNotFoundError: If the file specified by the path is not found.
		Exception: If there is an error processing the file.

	"""
	try:
		with open(path, 'r', encoding='utf-8') as file:
			# Read each line in the file and extract the salary
			salaries = [int(line.split(',')[1]) for line in file]
			
			# Calculate the total salary
			total = sum(salaries)
			
			# Calculate the average salary
			average = total / len(salaries) if salaries else 0
			
			# Return the total and average salary
			return total, average
	except FileNotFoundError:
		# Handle the case when the file is not found
		print("Файл не знайдено.")
		return 0, 0
	except Exception as e:
		# Handle any other exceptions that occur during file processing
		print(f"Помилка при обробці файлу: {e}")
		return 0, 0

# Приклад використання функції
if __name__ == "__main__":
	current_dir = pathlib.Path(__file__).parent
	path = current_dir / "salaries.txt"
	total, average = total_salary(path)
	print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")