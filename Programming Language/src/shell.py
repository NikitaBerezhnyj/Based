import os
import sys
import base
import based
import readline
import shell_commands as sc

is_worked = True
version = 0.1

# Основні команди для інтерпретатора
def process_command():
    global is_worked, version
    while is_worked:
        text = input('БАЗА >> ')

        # Пропуск пустого рядка в інтерпретаторі
        if text == '':
            continue

        # Ініціалізація База
        if text == "ІНІЦІАЛІЗАЦІЯ" or text == "init":
            sc.init()
            continue

        # Деініціалізація База
        if text == "ДЕІНІЦІАЛІЗАЦІЯ" or text == "uninit":
            sc.deinit()
            continue

        # Допомога з переліком синтаксису та командами
        if text == "ДОПОМОГА" or text == "help":
            sc.help()
            continue

        # Версія База
        if text == "ВЕРСІЯ" or text == "version":
            sc.version_check(version)
            continue

        # Показати цю теку
        if text == "ЦТ" or text == "pwd":
            sc.this_dir()
            continue

        # Показати вміст теки
        if text == "ВТ" or text == "ls":
            sc.list_files()
            continue

        # Змінити теку
        words = text.split()
        if words[0] == "ЗТ" or words[0] == "cd":
            directory = words[1]
            sc.change_dir(directory)
            continue

        # Створити файл
        words = text.split()
        if words[0] == "СФ" or words[0] == "touch":
            filename = words[1]
            sc.create_file(filename)
            continue

        # Створити теку
        words = text.split()
        if words[0] == "СТ" or words == "mkdir":
            foldername = words[1]
            sc.create_dir(foldername)
            continue

        # Очистити термінал
        if text == "ОЧИСТИТИ" or text == "clear":
            sc.clear()
            continue

        # Вихід з терміналу База
        if text == "ВИХІД" or text == "exit":
            is_worked = False
            break

        # Маленька великодка
        if text == "БАЗА":
            base.fill_terminal(version)
            continue

        if text.strip() == "":
            continue

        result, error = based.run('Командний рядок Based', text)

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))

# Основна функція для запуску інтерпретатора
def main():
	global is_worked, version
	argc = len(sys.argv)

	# Запуск стандартного інтерпретатора
	if argc < 2:
		process_command()
	# Запуск файлів якщо вказано шлях до файлу
	elif argc == 2:
		file_to_run = sys.argv[1]
		run_command = 'ЗАПУСК("' + file_to_run + '")'
		result, error = based.run(file_to_run, run_command)
		if error:
		    print(error.as_string())
		elif result:
		    if len(result.elements) == 1:
		        print(repr(result.elements[0]))
		    else:
		        print(repr(result))
	# Занадто багато параметрів при запуску
	else:
		print("ПОМИЛКА: Занадто багато параметрів.")
		print("usage: based [шлях_до_файлу.based]")
		print("Для використання коду, виконуйте його у інтерпретаторі або запускайте скрипт з одним параметром (шлях до файлу)")

# Запуск функції main при старті програми
if __name__ == "__main__":
    main()