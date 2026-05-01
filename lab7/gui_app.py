# БЛОК 1: ИМПОРТЫ
import customtkinter as ctk
from tkinter import messagebox, filedialog
# messagebox - для всплывающих диалоговых окон с сообщениями
# filedialog - для диалогов выбора файлов и папок

# Импортируем функции из нашего пакета rare_package
# Эти функции содержат всю логику лабораторных работ
from rare_package import (
    unpack_recursive,  # из lab4 - рекурсивная распаковка
    unpack_iterative,  # из lab4 - итеративная распаковка
    sequence_recursive,  # из lab4 - рекурсивная последовательность
    sequence_iterative,  # из lab4 - итеративная последовательность
    get_file_reader,  # из lab5 - замыкание для чтения файла
    log_c,  # из lab5 - декоратор логирования
    generate_primes  # из lab6 - генератор простых чисел
)
# БЛОК 2: НАСТРОЙКА ВНЕШНЕГО ВИДА (глобальные настройки)

# Устанавливаем тему оформления
ctk.set_appearance_mode("dark")

# Устанавливаем цветовую схему
ctk.set_default_color_theme("blue")

# БЛОК 3: ГЛАВНЫЙ КЛАСС ПРИЛОЖЕНИЯ
class LabApp(ctk.CTk):
    # Главный класс приложения.
    # Наследуется от ctk.CTk - главного окна CustomTkinter.
    # CTk - это аналог tkinter.Tk, но с современным дизайном


    def __init__(self):
        # Конструктор класса. Вызывается при создании объекта LabApp.
        # Здесь инициализируются все компоненты интерфейса.

        # 3.1: ИНИЦИАЛИЗАЦИЯ РОДИТЕЛЬСКОГО КЛАССА
        # Вызываем конструктор родительского класса (ctk.CTk)
        # Это создаёт главное окно приложения
        super().__init__()

        # 3.2: НАСТРОЙКА ОСНОВНЫХ ПАРАМЕТРОВ ОКНА
        # Устанавливаем заголовок окна (отображается в строке заголовка)
        self.title("Лабораторные работы №4-6")

        # Устанавливаем размер окна: ширина 900 пикселей, высота 700 пикселей
        self.geometry("900x700")

        # Запрещаем изменение размера окна
        self.resizable(False, False)

        # 3.3: ПЕРЕМЕННЫЕ СОСТОЯНИЯ
        # current_module - хранит имя текущей активной лабораторной работы
        # По умолчанию установлена "lab4"
        self.current_module = "lab4"

        # 3.4: ВЫЗОВ МЕТОДА НАСТРОЙКИ ИНТЕРФЕЙСА
        # Вызываем метод, который создаёт все виджеты интерфейса
        self.setup_ui()

    def setup_ui(self):
        # Метод для создания всех элементов интерфейса.
        # Разбит на логические блоки для удобства чтения.

        # 3.4.1: ВЕРХНЯЯ ЧАСТЬ - ВКЛАДКИ (TABVIEW)
        # Создаём виджет с вкладками
        # self - родительский виджет (главное окно)
        # width=850 - ширина вкладок
        # height=100 - высота вкладок
        self.tabview = ctk.CTkTabview(self, width=850, height=100)

        # Размещаем вкладки в окне:
        # pady=10 - отступ сверху и снизу 10 пикселей
        # padx=10 - отступ слева и справа 10 пикселей
        # fill="x" - растягивать по горизонтали
        self.tabview.pack(pady=10, padx=10, fill="x")

        # Добавляем три вкладки с названиями
        # Метод add() создаёт вкладку и возвращает ссылку на неё
        tab4 = self.tabview.add("Лаба №4 - Рекурсия")  # Вкладка для лабораторной №4
        tab5 = self.tabview.add("Лаба №5 - Замыкания")  # Вкладка для лабораторной №5
        tab6 = self.tabview.add("Лаба №6 - Простые числа")  # Вкладка для лабораторной №6

        # 3.4.2: НАПОЛНЕНИЕ КАЖДОЙ ВКЛАДКИ
        # Вызываем методы, которые добавляют виджеты в каждую вкладку
        # Передаём вкладку (tab4, tab5, tab6) как родительский виджет
        self.setup_lab4_tab(tab4)  # Наполняем вкладку лабораторной №4
        self.setup_lab5_tab(tab5)  # Наполняем вкладку лабораторной №5
        self.setup_lab6_tab(tab6)  # Наполняем вкладку лабораторной №6

        # 3.4.3: НИЖНЯЯ ЧАСТЬ - ОБЛАСТЬ ВЫВОДА РЕЗУЛЬТАТА
        # Создаём рамку (контейнер) для области результатов
        # self - родитель (главное окно)
        self.result_frame = ctk.CTkFrame(self)

        # Размещаем рамку:
        # pady=10 - отступ сверху/снизу 10px
        # padx=10 - отступ слева/справа 10px
        # fill="both" - растягивать и по горизонтали, и по вертикали
        # expand=True - разрешить расширение при изменении размера окна
        self.result_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Создаём текстовую метку (заголовок) для области результатов
        # font - настройка шрифта: ("Название шрифта", размер, "жирный")
        self.result_label = ctk.CTkLabel(
            self.result_frame,
            text="Результат:",
            font=("Arial", 16, "bold")
        )

        # Размещаем метку:
        # pady=5 - отступ 5px сверху/снизу
        # padx=10 - отступ 10px слева/справа
        # anchor="w" - привязка к западу (west = левому краю)
        self.result_label.pack(pady=5, padx=10, anchor="w")

        # Создаём текстовое поле для вывода результатов
        # height=300 - высота в пикселях
        # font=("Consolas", 12) - моноширинный шрифт (как в консоли)
        self.result_text = ctk.CTkTextbox(
            self.result_frame,
            height=300,
            font=("Consolas", 12)
        )

        # Размещаем текстовое поле:
        # fill="both" - растягивать в обе стороны
        # expand=True - разрешить расширение
        self.result_text.pack(pady=5, padx=10, fill="both", expand=True)

    def setup_lab4_tab(self, parent):
        # Настройка интерфейса для лабораторной работы №4.
        # Аргументы: parent - виджет-родитель (вкладка tab4)

        # 3.4.2.1: ВЫПАДАЮЩИЙ СПИСОК ДЛЯ ВЫБОРА ПРОГРАММЫ

        # Создаём выпадающий список (OptionMenu)
        # parent - вкладка, в которой будет список
        # values - список возможных значений
        # command - функция, вызываемая при изменении выбора
        self.lab4_choice = ctk.CTkOptionMenu(
            parent,
            values=[
                "Распаковка (рекурсия)",  # Вариант 1
                "Распаковка (итеративно)",  # Вариант 2
                "Последовательность w_i (рекурсия)",  # Вариант 3
                "Последовательность w_i (итеративно)"  # Вариант 4
            ],
            command=self.on_lab4_change  # Колбэк при смене выбора
        )

        # Размещаем выпадающий список
        self.lab4_choice.pack(pady=10, padx=10)

        # 3.4.2.2: МЕТКА ДЛЯ ПОЛЯ ВВОДА
        # Создаём текстовую метку-подсказку для поля ввода
        self.lab4_input_label = ctk.CTkLabel(
            parent,
            text="Входные данные:"
        )
        self.lab4_input_label.pack(pady=5, padx=10)

        # 3.4.2.3: ТЕКСТОВОЕ ПОЛЕ ДЛЯ ВВОДА ДАННЫХ
        # CTkTextbox - многострочное текстовое поле
        # height=100 - высота 100 пикселей
        self.lab4_input = ctk.CTkTextbox(parent, height=100)
        self.lab4_input.pack(pady=5, padx=10, fill="x")

        # Устанавливаем пример ввода по умолчанию
        self.lab4_input.insert("1.0", "[None, [1, ({2, 3}, {'foo': 'bar'})]]")

        # 3.4.2.4: КНОПКА ВЫПОЛНЕНИЯ
        # Создаём кнопку
        # command - функция, вызываемая при нажатии
        self.lab4_btn = ctk.CTkButton(
            parent,
            text="Выполнить",
            command=self.run_lab4  # Колбэк при нажатии
        )
        self.lab4_btn.pack(pady=10)

    def setup_lab5_tab(self, parent):
        # Настройка интерфейса для лабораторной работы №5.
        # Аргументы: parent - виджет-родитель (вкладка tab5)

        # 3.4.2.5: ВЫПАДАЮЩИЙ СПИСОК ДЛЯ ЛАБЫ 5
        self.lab5_choice = ctk.CTkOptionMenu(
            parent,
            values=[
                "Чтение файла (замыкание)",  # Программа 1
                "Декоратор логирования"  # Программа 2
            ],
            command=self.on_lab5_change  # Колбэк при смене выбора
        )
        self.lab5_choice.pack(pady=10, padx=10)


        # 3.4.2.6: КОНТЕЙНЕР ДЛЯ ВЫБОРА ФАЙЛА
        # Создаём рамку для группировки элементов выбора файла
        self.file_frame = ctk.CTkFrame(parent)
        self.file_frame.pack(pady=5, padx=10, fill="x")

        # Поле для ввода пути к файлу
        # placeholder_text - текст-подсказка внутри поля
        self.file_entry = ctk.CTkEntry(
            self.file_frame,
            placeholder_text="Имя файла"
        )

        # Размещаем поле ввода:
        # side="left" - слева от родительского контейнера
        # fill="x" - растягивать по горизонтали
        # expand=True - разрешить расширение
        # padx=(0, 10) - отступ справа 10px
        self.file_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        # Кнопка "Обзор" для открытия диалога выбора файла
        # width=60 - ширина кнопки
        self.browse_btn = ctk.CTkButton(
            self.file_frame,
            text="Обзор",
            width=60,
            command=self.browse_file  # Колбэк при нажатии
        )
        self.browse_btn.pack(side="right")


        # 3.4.2.7: КНОПКА ВЫПОЛНЕНИЯ ДЛЯ ЛАБЫ 5

        self.lab5_btn = ctk.CTkButton(
            parent,
            text="Выполнить",
            command=self.run_lab5
        )
        self.lab5_btn.pack(pady=10)

        # По умолчанию показываем контейнер для выбора файла
        # (потому что первая программа - чтение файла)
        self.file_frame.pack()

    def setup_lab6_tab(self, parent):
        # Настройка интерфейса для лабораторной работы №6.
        # Аргументы: parent - виджет-родитель (вкладка tab6)

        # 3.4.2.8: КОНТЕЙНЕР ДЛЯ ГРАНИЦ ДИАПАЗОНА
        # Создаём рамку для полей ввода границ
        range_frame = ctk.CTkFrame(parent)
        range_frame.pack(pady=10, padx=10, fill="x")

        # Метка "Нижняя граница:"
        ctk.CTkLabel(range_frame, text="Нижняя граница:").pack(side="left", padx=5)

        # Поле ввода для нижней границы
        # width=100 - ширина 100 пикселей
        self.start_entry = ctk.CTkEntry(range_frame, width=100)
        self.start_entry.pack(side="left", padx=5)

        # Метка "Верхняя граница:"
        ctk.CTkLabel(range_frame, text="Верхняя граница:").pack(side="left", padx=5)

        # Поле ввода для верхней границы
        self.end_entry = ctk.CTkEntry(range_frame, width=100)
        self.end_entry.pack(side="left", padx=5)

        # 3.4.2.9: КНОПКА ВЫПОЛНЕНИЯ ДЛЯ ЛАБЫ 6
        self.lab6_btn = ctk.CTkButton(
            parent,
            text="Найти простые числа",
            command=self.run_lab6
        )
        self.lab6_btn.pack(pady=20)


    # БЛОК 4: ОБРАБОТЧИКИ СОБЫТИЙ


    def run_lab4(self):
        # Запуск выбранной функции из лабораторной работы №4.
        # Этапы:
        #1. Получить выбранный пункт из выпадающего списка
        #2. Получить введённые пользователем данные
        #3. Очистить поле результата
        #4. Вызвать нужную функцию
        #5. Вывести результат или ошибку

        # 4.1: ПОЛУЧЕНИЕ ДАННЫХ ОТ ПОЛЬЗОВАТЕЛЯ
        # get() возвращает текущий выбранный пункт (строку)
        choice = self.lab4_choice.get()

        # Получаем текст из текстового поля
        # "1.0" - начало текста (строка 1, символ 0)
        # "end-1c" - конец текста минус 1 символ (убираем лишний перенос)
        input_data = self.lab4_input.get("1.0", "end-1c")

        # 4.2: ОЧИСТКА ПОЛЯ РЕЗУЛЬТАТА
        # delete удаляет текст из текстового поля
        # "1.0" - от начала
        # "end" - до конца
        self.result_text.delete("1.0", "end")

        # 4.3: ОБРАБОТКА ПОЛЬЗОВАТЕЛЬСКОГО ВЫБОРА
        try:
            # Проверяем, что выбрал пользователь
            if choice == "Распаковка (рекурсия)":
                # eval() преобразует строку в Python-объект
                # Например: "[1, [2, 3]]" -> [1, [2, 3]]
                data = eval(input_data)
                result = unpack_recursive(data)
                self.result_text.insert("1.0", f"Результат распаковки (рекурсия):\n{result}")

            elif choice == "Распаковка (итеративно)":
                data = eval(input_data)
                result = unpack_iterative(data)
                self.result_text.insert("1.0", f"Результат распаковки (итеративно):\n{result}")

            elif choice == "Последовательность w_i (рекурсия)":
                # Для последовательности нужен номер члена (целое число)
                i = int(input_data)
                result = sequence_recursive(i)
                self.result_text.insert("1.0", f"w_{i} = {result}")

            elif choice == "Последовательность w_i (итеративно)":
                i = int(input_data)
                result = sequence_iterative(i)
                self.result_text.insert("1.0", f"w_{i} = {result}")

        except Exception as e:
            # При любой ошибке выводим сообщение в поле результата
            self.result_text.insert("1.0", f"Ошибка:\n{str(e)}")

    def run_lab5(self):
        # Запуск выбранной функции из лабораторной работы №5.


        # Получаем выбор пользователя
        choice = self.lab5_choice.get()

        # Очищаем поле результата
        self.result_text.delete("1.0", "end")

        try:
            if choice == "Чтение файла (замыкание)":
                # Получаем путь к файлу
                filename = self.file_entry.get()

                # Проверяем, что файл выбран
                if not filename:
                    # messagebox - всплывающее окно с сообщением
                    # showerror - показывает окно с ошибкой
                    messagebox.showerror("Ошибка", "Выберите файл!")
                    return

                # Создаём замыкание для чтения файла
                reader = get_file_reader(filename)

                # Читаем все строки
                lines = []
                while True:
                    line = reader()
                    if line is None:  # Конец файла
                        break
                    lines.append(line)

                # Форматируем вывод с номерами строк
                if lines:
                    # enumerate создаёт пары (индекс, строка)
                    result = "\n".join(f"{i + 1}. {line}" for i, line in enumerate(lines))
                    self.result_text.insert("1.0", f"Содержимое файла '{filename}':\n{result}")
                else:
                    self.result_text.insert("1.0", f"Файл '{filename}' пуст")

            elif choice == "Декоратор логирования":
                # Демонстрация работы декоратора

                # Создаём функцию с декоратором
                @log_c
                def example_func(x, y):
                    return x * y

                # Вызываем функцию
                result = example_func(5, 3)

                # Выводим результат
                self.result_text.insert("1.0",
                                        "Декоратор отработал.\n"
                                        "Проверьте консоль для просмотра логов.\n"
                                        f"Результат example_func(5, 3) = {result}\n"
                                        )

        except FileNotFoundError:
            self.result_text.insert("1.0", "Ошибка: файл не найден")
        except Exception as e:
            self.result_text.insert("1.0", f"Ошибка:\n{str(e)}")

    def run_lab6(self):
        # Запуск генератора простых чисел (лабораторная №6).
        # Очищаем поле результата
        self.result_text.delete("1.0", "end")

        try:
            # Получаем границы диапазона и преобразуем в целые числа
            start = int(self.start_entry.get())
            end = int(self.end_entry.get())

            # Проверяем корректность границ
            if start > end:
                self.result_text.insert(
                    "1.0",
                    f"Ошибка: нижняя граница ({start}) больше верхней ({end})"
                )
                return

            # Вызываем функцию генерации простых чисел
            primes = generate_primes(start, end)

            # Выводим результат
            if not primes:
                self.result_text.insert(
                    "1.0",
                    f"Простых чисел в диапазоне [{start}, {end}] не найдено"
                )
            else:
                self.result_text.insert(
                    "1.0",
                    f"Простые числа в диапазоне [{start}, {end}]:\n"
                    f"{primes}\n\n"
                    f"Всего найдено: {len(primes)}"
                )

        except ValueError:
            # Ошибка при преобразовании в число (пользователь ввёл буквы)
            self.result_text.insert("1.0", "Ошибка: введите целые числа!")
        except Exception as e:
            self.result_text.insert("1.0", f"Ошибка:\n{str(e)}")

    def browse_file(self):
        # Открыть диалог выбора файла.
        # Вызывается при нажатии кнопки "Обзор".
        # filedialog.askopenfilename() открывает стандартный диалог Windows
        # title - заголовок окна
        # filetypes - фильтр типов файлов
        filename = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[
                ("Текстовые файлы", "*.txt"),  # Показываем только .txt
                ("Все файлы", "*.*")  # Или все файлы
            ]
        )

        # Если пользователь выбрал файл (не нажал "Отмена")
        if filename:
            # Очищаем поле ввода
            self.file_entry.delete(0, "end")
            # Вставляем путь к выбранному файлу
            self.file_entry.insert(0, filename)

    def on_lab4_change(self, choice):
        # Обработка изменения выбора в лабораторной №4.
        # Аргументы: choice - строка с выбранным пунктом меню
        # Меняем текст подсказки в зависимости от выбора
        if "Распаковка" in choice:
            # Если выбрана распаковка - ожидаем Python-выражение
            self.lab4_input_label.configure(text="Входные данные (Python-выражение):")
            # Очищаем и вставляем пример
            self.lab4_input.delete("1.0", "end")
            self.lab4_input.insert("1.0", "[None, [1, ({2, 3}, {'foo': 'bar'})]]")
        else:
            # Если выбрана последовательность - ожидаем число
            self.lab4_input_label.configure(text="Номер члена последовательности (целое число):")
            # Очищаем и вставляем пример
            self.lab4_input.delete("1.0", "end")
            self.lab4_input.insert("1.0", "5")

    def on_lab5_change(self, choice):
        # Обработка изменения выбора в лабораторной №5.
        # Аргументы: choice - строка с выбранным пунктом меню
        # Если выбрано чтение файла - показываем панель выбора файла
        if choice == "Чтение файла (замыкание)":
            # pack() - отобразить виджет
            self.file_frame.pack()
        else:
            # Если выбран декоратор - скрываем панель выбора файла
            # pack_forget() - убрать виджет из интерфейса
            self.file_frame.pack_forget()

# БЛОК 5: ТОЧКА ВХОДА В ПРОГРАММУ

if __name__ == "__main__":
    # Этот блок выполняется ТОЛЬКО при прямом запуске файла.
    # Если файл импортируется как модуль, этот код не выполняется.

    # Создаём экземпляр нашего приложения
    app = LabApp()

    # Запускаем главный цикл обработки событий
    # Без этого окно закроется сразу после открытия
    app.mainloop()