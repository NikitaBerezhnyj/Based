# Based

Based repository has [Ukrainian :ukraine:](#мова-програмування-based-ukraine) and [English :uk:](#programming-language-based-uk) localizations

# Мова програмування Based :ukraine:

<p align='center'>
  <img src='./icon.png' alt='Based icon' style="width:50%">
</p>

**_Мова програмування Based_** - це проста й незамислувата мова програмування з відкритим вихідним кодом, створена шляхом модифікації коду іншого навчального проекту під назвою [py-myopl-code](https://github.com/davidcallanan/py-myopl-code).

Її синтаксис навмисно зроблено максимально простим і лаконічним, без зайвих складнощів. Мета Based - повернутись до витоків програмування, та згадати як це програмувати без фреймворків та бібліотек, використовуючи тільки стандартні конструкції умовних операторів, циклів та простеньких функцій.

**_Через свою базовість та данину минулому, код на Based традиційно пишеться в стилі UPPERCASE._**

**_Швидкий перехід між розділами:_**

- [Based](#based)
- [Мова програмування Based :ukraine:](#мова-програмування-based-ukraine)
  - [Мова програмування Based](#мова-програмування-based)
    - [Інсталяція](#інсталяція)
      - [Ініціалізація](#ініціалізація)
      - [Деніціалізація](#деніціалізація)
    - [Синтаксис](#синтаксис)
    - [Приклади коду](#приклади-коду)
    - [Команди інтерпретатора](#команди-інтерпретатора)
  - [Корисні посилання](#корисні-посилання)
- [Programming language Based :uk:](#programming-language-based-uk)
  - [Programming language Based](#programming-language-based)
    - [Installation](#installation)
      - [Initialization](#initialization)
      - [Denialization](#denialization)
    - [Syntax.](#syntax)
    - [Code examples](#code-examples)
    - [Interpreter commands](#interpreter-commands)
  - [Useful links](#useful-links)

---

## Мова програмування Based

### Інсталяція

Щоб запустити інтерпретатор Based, вам необхідно буде виконати один з наступних варіантів:

**_1. Скомпілювати інтерпретатор_** (це дасть вам більше можливостей у майбутньому)

**_2. Запустити інтерпретатор без компіляції_** (це також підійде, якщо ви просто хочете спробувати мову Based і не хочете встановлювати або компілювати файли)

**_1. Компіляція інтерпретатора_**

Компілювання інтерпретатора необхідно для отримання виконуваного файлу based. Для цього виконайте наступні кроки:

1. Клонуйте репозиторій з GitHub:

```bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Перейдіть в теку з проектом:

```bash
cd Based/src
```

3. Встановіть пакет pyinstaller:

```bash
pip install pyinstaller
```

4. Запустіть компіляцію:

```bash
pyinstaller -F -n based shell.py
```

Після завершення компіляції в теці з проектом буде створений виконуваний файл based. Після ініціалізації цей файл можна буде використовувати для запуску програм мовою Based з будь-якої теки.

**_2. Запустити інтерпретатор без компіляції_**

Щоб запустити інтерпретатор без компіляції, виконайте наступну команду в теці з проектом:

1. Клонуйте репозиторій з GitHub:

```bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Перейдіть в теку з проектом:

```bash
cd Based/src
```

3. Запуск інтерпретатора

```bash
python shell.py
```

Ця команда запустить інтерпретатор Based в теці з проектом. Ви зможете написати і запустити програму, не компілюючи інтерпретатор.

#### Ініціалізація

Ініціалізація інтерпретатора Based необхідна для того, щоб можна було використовувати його з будь-якої теки на вашому комп'ютері. Для цього виконайте наступні дії:

1. Відкрийте скомпільований файл інтерпретатора

```bash
./based
```

2. Використайте наступну команду:

```python
ІНІЦІАЛІЗАЦІЯ
```

3. Завершіть роботу інтерпретатора:

```python
ВИХІД
```

Після ініціалізації інтерпретатора файл based буде скопійовано в теку з іншими утилітами, що дасть можливість використовувати його для запуску програм мовою Based з будь-якої теки.

#### Деніціалізація

Деініціалізація інтерпретатора Based необхідна, якщо ви більше не плануєте використовувати його. Для цього виконайте наступні кроки:

1. Відкрийте інтерпретатор

```bash
based
```

2. Використайте наступну команду:

```python
ДЕІНІЦІАЛІЗАЦІЯ
```

3. Завершіть роботу інтерпретатора:

```python
ВИХІД
```

Це видалить Based з теки з утилітами, але залишить його у теці з проєктом, тому ви зможете використовувати його і потім, якщо забажаєте

### Синтаксис

Я намагався зробити синтаксис Based простим і зрозумілим для початківців, але при цьому потужним і гнучким для досвідчених розробників. Тож перейдімо до роботи з мовою.

**_Створення коментарів_**

```python
# Це коментар, його інтерпретатор не бачить
```

**_Вивід тексту на екран_**

```python
# Вивід звичайного тексту
ДРУК("Привіт, Світ!")

# Вивід змінної
ЗМІННА А = 10
ДРУК(А)
```

**_Оголошення змінних_**

```python
# Цілочисельна змінна
ЗМІННА А = 10

# Дійсна змінна
ЗМІННА Б = 10.5

# Рядкова змінна
ЗМІННА В = "Рядок"

# Булева змінна
ЗМІННА Г = правда

```

**_Ввід користувача_**

```python
# Записується рядок
ЗМІННА А = ВВІД()

# Записується число
ЗМІННА Б = ввід_числа()
```

**_Оголошення масивів_**

```python
# Оголошення масиву цілих чисел
ЗМІННА А = [0, 1]

# Оголошення масиву дійсних чисел
ЗМІННА Б = [0.5, 1.001]

# Оголошення масиву рядків
ЗМІННА В = ["привіт", "світ"]

# Оголошення масиву булевих виразів
ЗМІННА Г = [правда, правда, брехня]

```

**\*Умови if (ЯКЩО), else if (ІНАКШЕ_ЯКЩО) та else (ІНАКШЕ)\_**

```python
# Умова ЯКЩО запис в один рядок
ЯКЩО А < 5 ТОДІ; ДРУК("А < 5")

# Умова ЯКЩО повний запис
ЯКЩО А < 5 ТОДІ
    ДРУК("А < 5")

# Умова ЯКЩО-ІНАКШЕ запис в один рядок
ЯКЩО А < 5 ТОДІ; ДРУК("А < 5") ІНАКШЕ ДРУК("А > 8")

# Умова ЯКЩО-ІНАКШЕ повний запис
ЯКЩО А < 5 ТОДІ
    ДРУК("А < 5")
ІНАКШЕ ДРУК("А > 8")

# Умова ЯКЩО-ІНАКШЕ_ЯКЩО-ІНАКШЕ запис в один рядок
ЯКЩО А < 5 ТОДІ; ДРУК("А < 5") ІНАКШЕ_ЯКЩО А > 5 також А < 8 ТОДІ; ДРУК("А < 5 і А > 8") ІНАКШЕ ДРУК("А > 8")

# Умова ЯКЩО-ІНАКШЕ_ЯКЩО-ІНАКШЕ повний запис
ЯКЩО А < 5 ТОДІ
    ДРУК("А < 5")
ІНАКШЕ_ЯКЩО А > 5 також А < 8 ТОДІ
    ДРУК("А < 5 і А > 8")
ІНАКШЕ ДРУК("А > 8")
```

**_Оголошення циклу while (ПОКИ)_**

```python
# Приклад циклу while (ПОКИ) у варіанті для одного рядка
ЗМІННА Лічильник = 0
ПОКИ Лічильник < 10 ТОДІ ЗМІННА Лічильник = Лічильник + 1; ДРУК(Лічильник)

# Приклад циклу while (ПОКИ) в розписаному варіанті
ЗМІННА Лічильник = 0
ПОКИ Лічильник < 10 ТОДІ
    ЗМІННА Лічильник = Лічильник + 1
    ДРУК(Лічильник)
КІНЕЦЬ
```

**_Оголошення циклу for (ДЛЯ)_**

```python
# Приклад циклу for (ДЛЯ) у варіанті для одного рядка
ДЛЯ Лічильника = 0 ДО 10 ТОДІ ДРУК(л)

# Приклад циклу for (ДЛЯ) в розписаному варіанті
ДЛЯ Лічильника = 0 ДО 10 ТОДІ
    ДРУК("Привіт, Світ!")
КІНЕЦЬ
```

**_Оголошення функції_**

```python
# Найпростіші функції, що можна записати в один рядок записуються так:
ФУНКЦІЯ Привіт_світ() -> ДРУК("Привіт, світ!")

# Функції, що не можна записати в один рядок записуються так:
ФУНКЦІЯ ПривітСвіт()
	ЗМІННА Рази = ввід_числа()
	ДРУК(Рази)
	ДЛЯ Лічильник = 0 ДО Рази ТОДІ
		ДРУК("Привіт, Світ!")
	КІНЕЦЬ
КІНЕЦЬ
```

**_Робота з сторонніми модулями_**

**сторонній_файл.based**

```python
ФУНКЦІЯ СторонняФункція()
    ДРУК("Стороння функція працює")
КІНЕЦЬ
```

**виконавчий_файл.based**

```python
отримати ("./сторонній_файл.based")

СторонняФункція()
```

**_Примітка!_** Шлях до файлу, який ми імпортуємо, потрібно вказувати залежно від файлу, що запускається, тобто якщо файли знаходяться в одній теці, то потрібно вказати просто "./назва*файлу.based", або "./назва*теки/назва_файлу.based", якщо файл лежить у іншій теці.

### Приклади коду

**_Міні гра Вгадай Число, в якій користувач вгадує число, яке програма загадала. Кількість спроб встановлюється користувачем._**

```python
ФУНКЦІЯ Гра(КількістьСпроб, ВиграшнеЧисло)
    ДЛЯ спроба = 0 ДО КількістьСпроб ТОДІ
        ДРУК("Введіть будь ласка число від 1 до 10:")
        ЗМІННА КористувацькеЧисло = ввід_числа()
        ЯКЩО КористувацькеЧисло < ВиграшнеЧисло ТОДІ
            ДРУК("Переможне число більше")
        ІНАКШЕ_ЯКЩО КористувацькеЧисло > ВиграшнеЧисло ТОДІ
            ДРУК("Переможне число менше")
        ІНАКШЕ_ЯКЩО КористувацькеЧисло == ВиграшнеЧисло ТОДІ
            ДРУК("Ви виграли!")
            ПОВЕРНУТИ 0
        ІНАКШЕ ПРОДОВЖУВАТИ
    КІНЕЦЬ
    ДРУК("Ви програли")
    ДРУК("Виграшне число: ")
    ДРУК(ВиграшнеЧисло)
КІНЕЦЬ

ДРУК("Скільки ви хочете спроб:")
ЗМІННА КількістьСпроб = ввід_числа()
Гра(КількістьСпроб, 4)
```

**_Максимально простий, консольний калькулятор, який виконує арифметичні операції. Користувач обирає операцію, вводить числа, і отримує результат. Програма запитує користувача, чи бажає він продовжити обчислення._**

```python
ФУНКЦІЯ Калькулятор()
    ДРУК("Введіть перше число: ")
    ЗМІННА А = ввід_числа()
    ДРУК("Введіть дію (0 - додавання; 1 - віднімання; 2 - множення; 3 - ділення; 4 - степінь): ")
    ЗМІННА Дія = ввід_числа()
    ДРУК("Введіть друге число: ")
    ЗМІННА Б = ввід_числа()

    ЯКЩО Дія == 0 ТОДІ
        ЗМІННА Результат = А + Б
    ІНАКШЕ_ЯКЩО Дія == 1 ТОДІ
        ЗМІННА Результат = А - Б
    ІНАКШЕ_ЯКЩО Дія == 2 ТОДІ
        ЗМІННА Результат = А * Б
    ІНАКШЕ_ЯКЩО Дія == 3 ТОДІ
        ЗМІННА Результат = А / Б
    ІНАКШЕ_ЯКЩО Дія == 4 ТОДІ
        ЗМІННА Результат = А ^ Б
    ІНАКШЕ ДРУК("Схоже я не знаю такої дії, вибачте")

    ДРУК("Результат: ")
    ДРУК(Результат)

    ДРУК("Натисніть Enter щоб продовжити...")
    ВВІД()
    КІНЕЦЬ

ЗМІННА ЧиПрацює = 1

ПОКИ ЧиПрацює > 0 ТОДІ
    ДРУК("------------------------------------------------------")
    ДРУК("-----------------Простий Калькулятор------------------")
    ДРУК("------------------------------------------------------")
    ДРУК("-Для використання калькулятора виберіть одну з команд-")
    ДРУК("------------------------------------------------------")
    ДРУК("[0 - Обчислити вираз]")
    ДРУК("[1 - Вихід]")
    ДРУК("------------------------------------------------------")
    ДРУК("")
    ДРУК("Ваш вибір: ")
    ЗМІННА ВвідКористувача = ввід_числа()
    ЯКЩО ВвідКористувача == 0 ТОДІ
        Калькулятор()
    ІНАКШЕ_ЯКЩО ВвідКористувача == 1 ТОДІ
        ЗМІННА ЧиПрацює = 0
        ПОВЕРНУТИ 0
    ІНАКШЕ ДРУК("Не вірне число")
    ДРУК("")
    КІНЕЦЬ
```

### Команди інтерпретатора

- **_ДОПОМОГА_** - показує всі доступні команди для терміналу інтерпретатора та базовий синтаксис мови

- **_ЗАПУСК_** - запускає файл .based (приклад використання: **_ЗАПУСК("приклад.based")_**)

- **_ЦТ_** - ця тека. Показує шлях до поточної теки

- **_ЛФ_** - лист файлів. Показує вміст поточної теки

- **_ЗТ_** - змінити теку. Змінює поточну теку

- **_СФ_** - створити файл. Створює файл у поточній теці (приклад використання: **_СФ приклад.txt_**, якщо розширення не вказане, то воно буде за замовчуванням встановлене, як .based)

- **_СТ_** - створити теку. Створює теку у поточній (приклад використання: ***СТ тестова*тека\_**)

- **_ОЧИСТИТИ_** - очищує термінал інтерпретатора

- **_ВИХІД_** - закриває інтерпретатор

- **_ВЕРСІЯ_** - показує поточну версію Based, що встановлена на вашому ПК

- **_БАЗА_** - виводить основну інформацію про стан Based

## Корисні посилання

**_Власне IDE:_** [https://github.com/NikitaBerezhnyj/NUB_IDE](https://github.com/NikitaBerezhnyj/NUB_IDE)

**_Розширення для VS code:_** [https://github.com/NikitaBerezhnyj/Based_Language_Support_for_VS_Code](https://github.com/NikitaBerezhnyj/Based_Language_Support_for_VS_Code)

**_Документація по проєкту:_** [https://nub-project-docs.netlify.app](https://nub-project-docs.netlify.app)

---

# Programming language Based :uk:

<p align='center'>
  <img src='./icon.png' alt='Based icon' style="width:50%">
</p>

**_Programming language Based_** is a simple and uncomplicated open source programming language created by modifying the code of another educational project called [py-myopl-code] (https://github.com/davidcallanan/py-myopl-code).

Its syntax is deliberately made as simple and concise as possible, without unnecessary complexity. The goal of Based is to return to the roots of programming and to remember how to program without frameworks and libraries, using only standard constructs of conditional statements, loops, and simple functions.

**_Due to its basic nature and tribute to the past, code in Based is traditionally written in the PascalCase style._**

**_Quick transition between sections:_**

- [Based](#based)
- [Мова програмування Based :ukraine:](#мова-програмування-based-ukraine)
  - [Мова програмування Based](#мова-програмування-based)
    - [Інсталяція](#інсталяція)
      - [Ініціалізація](#ініціалізація)
      - [Деніціалізація](#деніціалізація)
    - [Синтаксис](#синтаксис)
    - [Приклади коду](#приклади-коду)
    - [Команди інтерпретатора](#команди-інтерпретатора)
  - [Корисні посилання](#корисні-посилання)
- [Programming language Based :uk:](#programming-language-based-uk)
  - [Programming language Based](#programming-language-based)
    - [Installation](#installation)
      - [Initialization](#initialization)
      - [Denialization](#denialization)
    - [Syntax.](#syntax)
    - [Code examples](#code-examples)
    - [Interpreter commands](#interpreter-commands)
  - [Useful links](#useful-links)

---

## Programming language Based

### Installation

To start the Based interpreter, you will need to do one of the following:

**_1. Compile the interpreter_** (this will give you more options in the future)

**_2. Run the interpreter without compiling_** (this is also suitable if you just want to try the Based language and do not want to install or compile files)

**_1. Compile the interpreter_**.

Compiling the interpreter is necessary to get the based executable. To do this, follow these steps:

1. Clone the repository from GitHub:

```bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Change to the project folder:

```bash
cd Based/'Programming Language'/src
```

3. Install the package pyinstaller:

```bash
pip install pyinstaller
```

4. Run the compilation:

```bash
pyinstaller -F -n based shell.py
```

After compilation is complete, the based executable file will be created in the project folder. After initialization, this file can be used to run programs in the Based language from any folder.

**_2. Run the interpreter without compilation_**

To run the interpreter without compiling, run the following command in the project folder:

1. Clone the repository from GitHub:

```bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Change to the project folder:

```bash
cd Based/'Programming Language'/src
```

3. Run the interpreter

```bash
python shell.py
```

This command will start the Based interpreter in the project folder. You can write and run the program without compiling the interpreter.

#### Initialization

Initializing the Based interpreter is necessary to be able to use it from any folder on your computer. To do this, do the following:

1. Open the compiled interpreter file

```bash
./based
```

2. Use the following command:

```python
ІНІЦІАЛІЗАЦІЯ
```

3. Shut down the interpreter:

```python
ВИХІД
```

After the interpreter is initialized, the based file will be copied to the folder with other utilities, which will make it possible to use it to run programs in the Based language from any folder.

#### Denialization

You need to deinitialize the Based interpreter if you no longer plan to use it. To do this, follow these steps:

1. Open the interpreter

```bash
based
```

2. Use the following command:

```python
ДЕІНІЦІАЛІЗАЦІЯ
```

3. Shut down the interpreter:

```python
ВИХІД
```

This will remove Based from the utilities folder, but leave it in the project folder, so you can use it later if you want to.

### Syntax.

I've tried to make the Based syntax simple and easy to understand for beginners, but powerful and flexible for advanced developers. So let's get down to business with the language.

**_Creating comments_**

```python
# This is a comment, the interpreter does not see it
```

**_Display text on the screen_**

```python
# Plain text output
ДРУК("Привіт, Світ!")

# Outputting a variable
ЗМІННА А = 10
ДРУК(А)
```

**_Declaration of variables_**

```python
# Integer variable
ЗМІННА А = 10

# Float variable
ЗМІННА Б = 10.5

# String variable
ЗМІННА В = "Рядок"

# Boolean variable
ЗМІННА Г = правда

```

**_User input_**

```python
# The string is written
ЗМІННА А = ВВІД()

# The number is written
ЗМІННА Б = ввід_числа()
```

**_Оголошення масивів_**

```python
# Declaring an array of integers
ЗМІННА А = [0, 1]

# Declaring an array of real numbers
ЗМІННА Б = [0.5, 1.001]

# Declaring an array of strings
ЗМІННА В = ["привіт", "світ"]

# Declaring an array of Boolean expressions
ЗМІННА Г = [правда, правда, брехня]

```

**_If, else if, and else conditions_**

```python
# Condition if the record is in one line
ЯКЩО А < 5 ТОДІ; ДРУК("А < 5")

# Condition if full record
ЯКЩО А < 5 ТОДІ
    ДРУК("А < 5")

# If-else condition record in one line
ЯКЩО А < 5 ТОДІ; ДРУК("А < 5")  ІНАКШЕ ДРУК("А > 8")

# If-else condition full record
ЯКЩО А < 5 ТОДІ
    ДРУК("А < 5")
ІНАКШЕ ДРУК("А > 8")

# If-else_if-else record in one line
ЯКЩО А < 5 ТОДІ; ДРУК("А < 5") ІНАКШЕ_ЯКЩО А > 5 також А < 8 ТОДІ; ДРУК("А < 5 і А > 8") ІНАКШЕ ДРУК("А > 8")

# Condition if_elif_else full record
ЯКЩО А < 5 ТОДІ
    ДРУК("А < 5")
ІНАКШЕ_ЯКЩО А > 5 також А < 8 ТОДІ
    ДРУК("А < 5 і А > 8")
ІНАКШЕ ДРУК("А > 8")
```

**_Declaring a while loop_**

```python
# An example of a while loop in a single-line version
ЗМІННА Лічильник = 0
ПОКИ Лічильник < 10 ТОДІ ЗМІННА Лічильник = Лічильник + 1; ДРУК(Лічильник)

# An example of a while loop in a scheduled version
ЗМІННА Лічильник = 0
ПОКИ Лічильник < 10 ТОДІ
    ЗМІННА Лічильник = Лічильник + 1
    ДРУК(Лічильник)
КІНЕЦЬ
```

**\*Declaring a for loop**

```python
# An example of a for loop in the version for one line
ДЛЯ Лічильника = 0 ДО 10 ТОДІ ДРУК(л)

# An example of a for loop in the painted version
ДЛЯ Лічильника = 0 ДО 10 ТОДІ
    ДРУК("Привіт, Світ!")
КІНЕЦЬ
```

**_Declaring a function_**

```python
# The simplest functions that can be written in one line are written like this:
ФУНКЦІЯ Привіт_світ() -> ДРУК("Привіт, світ!")

# Functions that cannot be written in one line are written like this:
ФУНКЦІЯ ПривітСвіт()
	ЗМІННА Рази = ввід_числа()
	ДРУК(Рази)
	ДЛЯ Лічильник = 0 ДО Рази ТОДІ
		ДРУК("Привіт, Світ!")
	КІНЕЦЬ
КІНЕЦЬ
```

### Code examples

**_Guess the Number mini-game in which the user guesses the number that the program has guessed. The number of attempts is set by the user._**

```python
ФУНКЦІЯ Гра(КількістьСпроб, ВиграшнеЧисло)
    ДЛЯ спроба = 0 ДО КількістьСпроб ТОДІ
        ДРУК("Введіть будь ласка число від 1 до 10:")
        ЗМІННА КористувацькеЧисло = ввід_числа()
        ЯКЩО КористувацькеЧисло < ВиграшнеЧисло ТОДІ
            ДРУК("Переможне число більше")
        ІНАКШЕ_ЯКЩО КористувацькеЧисло > ВиграшнеЧисло ТОДІ
            ДРУК("Переможне число менше")
        ІНАКШЕ_ЯКЩО КористувацькеЧисло == ВиграшнеЧисло ТОДІ
            ДРУК("Ви виграли!")
            ПОВЕРНУТИ 0
        ІНАКШЕ ПРОДОВЖУВАТИ
    КІНЕЦЬ
    ДРУК("Ви програли")
    ДРУК("Виграшне число: ")
    ДРУК(ВиграшнеЧисло)
КІНЕЦЬ

ДРУК("Скільки ви хочете спроб:")
ЗМІННА КількістьСпроб = ввід_числа()
Гра(КількістьСпроб, 4)
```

**_The simplest possible console calculator that performs arithmetic operations. The user selects an operation, enters numbers, and gets the result. The program asks the user if he or she wants to continue the calculation._**

```python
ФУНКЦІЯ Калькулятор()
    ДРУК("Введіть перше число: ")
    ЗМІННА А = ввід_числа()
    ДРУК("Введіть дію (0 - додавання; 1 - віднімання; 2 - множення; 3 - ділення; 4 - степінь): ")
    ЗМІННА Дія = ввід_числа()
    ДРУК("Введіть друге число: ")
    ЗМІННА Б = ввід_числа()

    ЯКЩО Дія == 0 ТОДІ
        ЗМІННА Результат = А + Б
    ІНАКШЕ_ЯКЩО Дія == 1 ТОДІ
        ЗМІННА Результат = А - Б
    ІНАКШЕ_ЯКЩО Дія == 2 ТОДІ
        ЗМІННА Результат = А * Б
    ІНАКШЕ_ЯКЩО Дія == 3 ТОДІ
        ЗМІННА Результат = А / Б
    ІНАКШЕ_ЯКЩО Дія == 4 ТОДІ
        ЗМІННА Результат = А ^ Б
    ІНАКШЕ ДРУК("Схоже я не знаю такої дії, вибачте")

    ДРУК("Результат: ")
    ДРУК(Результат)

    ДРУК("Натисніть Enter щоб продовжити...")
    ВВІД()
    КІНЕЦЬ

ЗМІННА ЧиПрацює = 1

ПОКИ ЧиПрацює > 0 ТОДІ
    ДРУК("------------------------------------------------------")
    ДРУК("-----------------Простий Калькулятор------------------")
    ДРУК("------------------------------------------------------")
    ДРУК("-Для використання калькулятора виберіть одну з команд-")
    ДРУК("------------------------------------------------------")
    ДРУК("[0 - Обчислити вираз]")
    ДРУК("[1 - Вихід]")
    ДРУК("------------------------------------------------------")
    ДРУК("")
    ДРУК("Ваш вибір: ")
    ЗМІННА ВвідКористувача = ввід_числа()
    ЯКЩО ВвідКористувача == 0 ТОДІ
        Калькулятор()
    ІНАКШЕ_ЯКЩО ВвідКористувача == 1 ТОДІ
        ЗМІННА ЧиПрацює = 0
        ПОВЕРНУТИ 0
    ІНАКШЕ ДРУК("Не вірне число")
    ДРУК("")
    КІНЕЦЬ
```

### Interpreter commands

- **_ДОПОМОГА_** - shows all available commands for the interpreter terminal and the basic syntax of the language

- **_ЗАПУСК_** - runs the .based file (example of use: **_ЗАПУСК("приклад.based")_**)

- **_ЦТ_** - this folder. Shows the path to the current folder

- **_ЛФ_** - a list of files. Shows the contents of the current folder

- **_ЗТ_** - change folder. Changes the current folder

- **_СФ_** - create file. Creates a file in the current folder (example of use: **_СФ приклад.txt_**, if the extension is not specified, it will be set to .based by default)

- **_ст_** - create folder. Creates a folder in the current one (example of use: ***СТ тестова*тека\_**)

- **_ОЧИСТИТИ_** - clears the interpreter terminal

- **_ВИХІД_** - closes the interpreter

- **_ВЕРСІЯ_** - shows the current version of Based installed on your PC

- **_БАЗА_** - displays basic information about the state of the Based

## Useful links

**_Custom IDE:_** [https://github.com/NikitaBerezhnyj/NUB_IDE](https://github.com/NikitaBerezhnyj/NUB_IDE)

**_Extensions for VS code:_** [https://github.com/NikitaBerezhnyj/Based_Language_Support_for_VS_Code](https://github.com/NikitaBerezhnyj/Based_Language_Support_for_VS_Code)

**_Project documentation:_** [https://nub-project-docs.netlify.app](https://nub-project-docs.netlify.app)
