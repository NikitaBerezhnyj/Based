# Based

Based repository has [Ukrainian :ukraine:](#мова-програмування-based-ukraine) and [English :uk:](#programming-language-based-uk) localizations

# Мова програмування Based :ukraine:

<p align='center'>
  <img src='./VS Code Extintion/based-extantion/icon-based.png' alt='Based icon' style="width:50%">
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
  - [Власне IDE для Based](#власне-ide-для-based)
  - [Розширення для VS code](#розширення-для-vs-code)
- [Programming language Based :uk:](#programming-language-based-uk)
  - [Programming language Based](#programming-language-based)
    - [Installation](#installation)
      - [Initialization](#initialization)
      - [Denialization](#denialization)
    - [Syntax.](#syntax)
    - [Code examples](#code-examples)
    - [Interpreter commands](#interpreter-commands)
  - [A custom IDE for Based](#a-custom-ide-for-based)
  - [Extensions for VS code](#extensions-for-vs-code)

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
cd Based/'Programming Language'/src
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
cd Based/'Programming Language'/src
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
ініціалізація
```

3. Завершіть роботу інтерпретатора:

```python
вихід
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
деініціалізація
```

3. Завершіть роботу інтерпретатора:

```python
вихід
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
друк("Привіт, Світ!")

# Вивід змінної
змінна А = 10
друк(А)
```

**_Оголошення змінних_**

```python
# Цілочисельна змінна
змінна А = 10

# Дійсна змінна
змінна Б = 10.5

# Рядкова змінна
змінна В = "Рядок"

# Булева змінна
змінна Г = правда

```

**_Ввід користувача_**

```python
# Записується рядок
змінна А = ввід()

# Записується число
змінна Б = ввід_числа()
```

**_Оголошення масивів_**

```python
# Оголошення масиву цілих чисел
змінна А = [0, 1]

# Оголошення масиву дійсних чисел
змінна Б = [0.5, 1.001]

# Оголошення масиву рядків
змінна В = ["привіт", "світ"]

# Оголошення масиву булевих виразів
змінна Г = [правда, правда, брехня]

```

***Умови if (якщо), else if (інакше*якщо) та else (інакше)\_**

```python
# Умова якщо запис в один рядок
якщо А < 5 тоді; друк("А < 5")

# Умова якщо повний запис
якщо А < 5 тоді
    друк("А < 5")

# Умова якщо-інакше запис в один рядок
якщо А < 5 тоді; друк("А < 5")  інакше друк("А > 8")

# Умова якщо-інакше повний запис
якщо А < 5 тоді
    друк("А < 5")
інакше друк("А > 8")

# Умова якщо-інакше_якщо-інакше запис в один рядок
якщо А < 5 тоді; друк("А < 5") інакше_якщо А > 5 також А < 8 тоді; друк("А < 5 і А > 8") інакше друк("А > 8")

# Умова якщо-інакше_якщо-інакше повний запис
якщо А < 5 тоді
    друк("А < 5")
інакше_якщо А > 5 також А < 8 тоді
    друк("А < 5 і А > 8")
інакше друк("А > 8")
```

**_Оголошення циклу while (поки)_**

```python
# Приклад циклу while (поки) у варіанті для одного рядка
змінна Лічильник = 0
поки Лічильник < 10 тоді змінна Лічильник = Лічильник + 1; друк(Лічильник)

# Приклад циклу while (поки) в розписаному варіанті
змінна Лічильник = 0
поки Лічильник < 10 тоді
    змінна Лічильник = Лічильник + 1
    друк(Лічильник)
кінець
```

**_Оголошення циклу for (для)_**

```python
# Приклад циклу for (для) у варіанті для одного рядка
для Лічильника = 0 до 10 тоді друк(л)

# Приклад циклу for (для) в розписаному варіанті
для Лічильника = 0 до 10 тоді
    друк("Привіт, Світ!")
кінець
```

**_Оголошення функції_**

```python
# Найпростіші функції, що можна записати в один рядок записуються так:
функція Привіт_світ() -> друк("Привіт, світ!")

# Функції, що не можна записати в один рядок записуються так:
функція ПривітСвіт()
	змінна Рази = ввід_числа()
	друк(Рази)
	для Лічильник = 0 до Рази тоді
		друк("Привіт, Світ!")
	кінець
кінець
```

**_Робота з сторонніми модулями_**

*сторонній*файл.based\_

```python
функція СторонняФункція()
    друк("Стороння функція працює")
кінець
```

*виконавчий*файл.based\_

```python
отримати ("./сторонній_файл.based")

СторонняФункція()
```

_***Примітка!*** Шлях до файлу, який ми імпортуємо, потрібно вказувати залежно від того, де знаходиться інтерпретатор. Тобто якщо ви ініціалізували інтерпретатор і запускаєте його в теці з основним файлом, то потрібно прописувати шлях імпорту відносно основного файлу. Але якщо ви інтерпретатор не ініціалізували, то доведеться писати шлях не від основного файлу, а від файлу shell.py._

### Приклади коду

**_Міні гра Вгадай Число, в якій користувач вгадує число, яке програма загадала. Кількість спроб встановлюється користувачем._**

```python
функція Гра(КількістьСпроб, ВиграшнеЧисло)
    для спроба = 0 до КількістьСпроб тоді
        друк("Введіть будь ласка число від 1 до 10:")
        змінна КористувацькеЧисло = ввід_числа()
        якщо КористувацькеЧисло < ВиграшнеЧисло тоді
            друк("Переможне число більше")
        інакше_якщо КористувацькеЧисло > ВиграшнеЧисло тоді
            друк("Переможне число менше")
        інакше_якщо КористувацькеЧисло == ВиграшнеЧисло тоді
            друк("Ви виграли!")
            повернути 0
        інакше продовжувати
    кінець
    друк("Ви програли")
    друк("Виграшне число: ")
    друк(ВиграшнеЧисло)
кінець

друк("Скільки ви хочете спроб:")
змінна КількістьСпроб = ввід_числа()
Гра(КількістьСпроб, 4)
```

**_Максимально простий, консольний калькулятор, який виконує арифметичні операції. Користувач обирає операцію, вводить числа, і отримує результат. Програма запитує користувача, чи бажає він продовжити обчислення._**

```python
функція Калькулятор()
    друк("Введіть перше число: ")
    змінна А = ввід_числа()
    друк("Введіть дію (0 - додавання; 1 - віднімання; 2 - множення; 3 - ділення; 4 - степінь): ")
    змінна Дія = ввід_числа()
    друк("Введіть друге число: ")
    змінна Б = ввід_числа()

    якщо Дія == 0 тоді
        змінна Результат = А + Б
    інакше_якщо Дія == 1 тоді
        змінна Результат = А - Б
    інакше_якщо Дія == 2 тоді
        змінна Результат = А * Б
    інакше_якщо Дія == 3 тоді
        змінна Результат = А / Б
    інакше_якщо Дія == 4 тоді
        змінна Результат = А ^ Б
    інакше друк("Схоже я не знаю такої дії, вибачте")

    друк("Результат: ")
    друк(Результат)

    друк("Натисніть Enter щоб продовжити...")
    ввід()
    кінець

змінна ЧиПрацює = 1

поки ЧиПрацює > 0 тоді
    друк("------------------------------------------------------")
    друк("-----------------Простий Калькулятор------------------")
    друк("------------------------------------------------------")
    друк("-Для використання калькулятора виберіть одну з команд-")
    друк("------------------------------------------------------")
    друк("[0 - Обчислити вираз]")
    друк("[1 - Вихід]")
    друк("------------------------------------------------------")
    друк("")
    друк("Ваш вибір: ")
    змінна ВвідКористувача = ввід_числа()
    якщо ВвідКористувача == 0 тоді
        Калькулятор()
    інакше_якщо ВвідКористувача == 1 тоді
        змінна ЧиПрацює = 0
        повернути 0
    інакше друк("Не вірне число")
    друк("")
    кінець
```

### Команди інтерпретатора

- **_допомога_** - показує всі доступні команди для терміналу інтерпретатора та базовий синтаксис мови

- **_запуск_** - запускає файл .based (приклад використання: **_запуск("приклад.based")_**)

- **_цт_** - ця тека. Показує шлях до поточної теки

- **_лф_** - лист файлів. Показує вміст поточної теки

- **_зт_** - змінити теку. Змінює поточну теку

- **_сф_** - створити файл. Створює файл у поточній теці (приклад використання: **_сф приклад.txt_**, якщо розширення не вказане, то воно буде за замовчуванням встановлене, як .based)

- **_ст_** - створити теку. Створює теку у поточній (приклад використання: ***ст тестова*тека\_**)

- **_очистити_** - очищує термінал інтерпретатора

- **_вихід_** - закриває інтерпретатор

- **_версія_** - показує поточну версію Based, що встановлена на вашому ПК

- **_БАЗА_** - виводить основну інформацію про стан Based

---

**_[Дивитись код мови](./Programming%20Language/)_**

## Власне IDE для Based

**_NUB IDE_** - це інтегроване середовище розробки для мов програмування [NikLang](https://github.com/NikitaBerezhnyj/NikLang), [Udav](https://github.com/NikitaBerezhnyj/Udav) та [Based](https://github.com/NikitaBerezhnyj/Based). Воно надає зручний і функціональний інтерфейс для написання коду цими мовами.

Особливості:

- Підсвічування синтаксису для мов NikLang, Udav та Based
- Автоматичне доповнення коду
- Вбудований термінал з власними командами для керування IDE
- Інтуїтивний графічний інтерфейс на основі Tauri + React

**_NUB IDE_** створено з метою максимально спростити та прискорити розробку на мовах NikLang, Udav та Based. Воно поєднує сучасний дизайн, зручність використання та всі необхідні для продуктивної роботи інструменти.

Завантажити та дізнатися більше про NUB IDE ви можете за посиланням нижче

---

**_[Дивитись код IDE](https://github.com/NikitaBerezhnyj/NUB_IDE)_**

## Розширення для VS code

Розширення додає підтримку мови програмування Based у VS Code.

**_Функціональність_**

- Підсвічування синтаксису для файлів .based
- Автодоповнення ключових слів мови Based

**_Використання_**

Після встановлення розширення, VS Code автоматично розпізнаватиме файли .based і застосовуватиме до них підсвічування і автодоповнення.

**_Установка_**

На даний момент розширення не доступне в маркетплейсі VS Code, тож його можна встановити тільки клонувавши репозиторій та встановивши його локально. Для цього вам необхідно буде виконати наступні кроки:

1. Копіювати репозиторій на свій ПК через термінал

```bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Потім знайти теку VS code на вашому ПК
3. Скопіювати теку based-extension до теки з іншими розширеннями

**_Підтримувані мови:_** Based (.based)

**_Залежності:_** Не має

**_Версія:_** 1.0.0

---

**_[Дивитись код розширення](./VS%20Code%20Extintion/based-extantion/)_**

---

<!-- _________________________________________________________________ -->

# Programming language Based :uk:

<p align='center'>
  <img src='./VS Code Extintion/based-extantion/icon-based.png' alt='Based icon' style="width:50%">
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
  - [Власне IDE для Based](#власне-ide-для-based)
  - [Розширення для VS code](#розширення-для-vs-code)
- [Programming language Based :uk:](#programming-language-based-uk)
  - [Programming language Based](#programming-language-based)
    - [Installation](#installation)
      - [Initialization](#initialization)
      - [Denialization](#denialization)
    - [Syntax.](#syntax)
    - [Code examples](#code-examples)
    - [Interpreter commands](#interpreter-commands)
  - [A custom IDE for Based](#a-custom-ide-for-based)
  - [Extensions for VS code](#extensions-for-vs-code)

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
ініціалізація
```

3. Shut down the interpreter:

```python
вихід
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
деініціалізація
```

3. Shut down the interpreter:

```python
вихід
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
друк("Привіт, Світ!")

# Outputting a variable
змінна А = 10
друк(А)
```

**_Declaration of variables_**

```python
# Integer variable
змінна А = 10

# Float variable
змінна Б = 10.5

# String variable
змінна В = "Рядок"

# Boolean variable
змінна Г = правда

```

**_User input_**

```python
# The string is written
змінна А = ввід()

# The number is written
змінна Б = ввід_числа()
```

**_Оголошення масивів_**

```python
# Declaring an array of integers
змінна А = [0, 1]

# Declaring an array of real numbers
змінна Б = [0.5, 1.001]

# Declaring an array of strings
змінна В = ["привіт", "світ"]

# Declaring an array of Boolean expressions
змінна Г = [правда, правда, брехня]

```

**_If, else if, and else conditions_**

```python
# Condition if the record is in one line
якщо А < 5 тоді; друк("А < 5")

# Condition if full record
якщо А < 5 тоді
    друк("А < 5")

# If-else condition record in one line
якщо А < 5 тоді; друк("А < 5")  інакше друк("А > 8")

# If-else condition full record
якщо А < 5 тоді
    друк("А < 5")
інакше друк("А > 8")

# If-else_if-else record in one line
якщо А < 5 тоді; друк("А < 5") інакше_якщо А > 5 також А < 8 тоді; друк("А < 5 і А > 8") інакше друк("А > 8")

# Condition if_elif_else full record
якщо А < 5 тоді
    друк("А < 5")
інакше_якщо А > 5 також А < 8 тоді
    друк("А < 5 і А > 8")
інакше друк("А > 8")
```

**_Declaring a while loop_**

```python
# An example of a while loop in a single-line version
змінна Лічильник = 0
поки Лічильник < 10 тоді змінна Лічильник = Лічильник + 1; друк(Лічильник)

# An example of a while loop in a scheduled version
змінна Лічильник = 0
поки Лічильник < 10 тоді
    змінна Лічильник = Лічильник + 1
    друк(Лічильник)
кінець
```

**\*Declaring a for loop**

```python
# An example of a for loop in the version for one line
для Лічильника = 0 до 10 тоді друк(л)

# An example of a for loop in the painted version
для Лічильника = 0 до 10 тоді
    друк("Привіт, Світ!")
кінець
```

**_Declaring a function_**

```python
# The simplest functions that can be written in one line are written like this:
функція Привіт_світ() -> друк("Привіт, світ!")

# Functions that cannot be written in one line are written like this:
функція ПривітСвіт()
	змінна Рази = ввід_числа()
	друк(Рази)
	для Лічильник = 0 до Рази тоді
		друк("Привіт, Світ!")
	кінець
кінець
```

### Code examples

**_Guess the Number mini-game in which the user guesses the number that the program has guessed. The number of attempts is set by the user._**

```python
функція Гра(КількістьСпроб, ВиграшнеЧисло)
    для спроба = 0 до КількістьСпроб тоді
        друк("Введіть будь ласка число від 1 до 10:")
        змінна КористувацькеЧисло = ввід_числа()
        якщо КористувацькеЧисло < ВиграшнеЧисло тоді
            друк("Переможне число більше")
        інакше_якщо КористувацькеЧисло > ВиграшнеЧисло тоді
            друк("Переможне число менше")
        інакше_якщо КористувацькеЧисло == ВиграшнеЧисло тоді
            друк("Ви виграли!")
            повернути 0
        інакше продовжувати
    кінець
    друк("Ви програли")
    друк("Виграшне число: ")
    друк(ВиграшнеЧисло)
кінець

друк("Скільки ви хочете спроб:")
змінна КількістьСпроб = ввід_числа()
Гра(КількістьСпроб, 4)
```

**_The simplest possible console calculator that performs arithmetic operations. The user selects an operation, enters numbers, and gets the result. The program asks the user if he or she wants to continue the calculation._**

```python
функція Калькулятор()
    друк("Введіть перше число: ")
    змінна А = ввід_числа()
    друк("Введіть дію (0 - додавання; 1 - віднімання; 2 - множення; 3 - ділення; 4 - степінь): ")
    змінна Дія = ввід_числа()
    друк("Введіть друге число: ")
    змінна Б = ввід_числа()

    якщо Дія == 0 тоді
        змінна Результат = А + Б
    інакше_якщо Дія == 1 тоді
        змінна Результат = А - Б
    інакше_якщо Дія == 2 тоді
        змінна Результат = А * Б
    інакше_якщо Дія == 3 тоді
        змінна Результат = А / Б
    інакше_якщо Дія == 4 тоді
        змінна Результат = А ^ Б
    інакше друк("Схоже я не знаю такої дії, вибачте")

    друк("Результат: ")
    друк(Результат)

    друк("Натисніть Enter щоб продовжити...")
    ввід()
    кінець

змінна ЧиПрацює = 1

поки ЧиПрацює > 0 тоді
    друк("------------------------------------------------------")
    друк("-----------------Простий Калькулятор------------------")
    друк("------------------------------------------------------")
    друк("-Для використання калькулятора виберіть одну з команд-")
    друк("------------------------------------------------------")
    друк("[0 - Обчислити вираз]")
    друк("[1 - Вихід]")
    друк("------------------------------------------------------")
    друк("")
    друк("Ваш вибір: ")
    змінна ВвідКористувача = ввід_числа()
    якщо ВвідКористувача == 0 тоді
        Калькулятор()
    інакше_якщо ВвідКористувача == 1 тоді
        змінна ЧиПрацює = 0
        повернути 0
    інакше друк("Не вірне число")
    друк("")
    кінець
```

### Interpreter commands

- **_допомога_** - shows all available commands for the interpreter terminal and the basic syntax of the language

- **_запуск_** - runs the .based file (example of use: **_запуск("приклад.based")_**)

- **_цт_** - this folder. Shows the path to the current folder

- **_лф_** - a list of files. Shows the contents of the current folder

- **_зт_** - change folder. Changes the current folder

- **_сф_** - create file. Creates a file in the current folder (example of use: **_сф приклад.txt_**, if the extension is not specified, it will be set to .based by default)

- **_ст_** - create folder. Creates a folder in the current one (example of use: ***ст тестова*тека\_**)

- **_очистити_** - clears the interpreter terminal

- **_вихід_** - closes the interpreter

- **_версія_** - shows the current version of Based installed on your PC

- **_БАЗА_** - displays basic information about the state of the Based

---

**_[See the language code](./Programming%20Language/)_**

## A custom IDE for Based

NUB IDE is a modern integrated development environment for the programming languages [NikLang](https://github.com/NikitaBerezhnyj/NikLang), [Udav](https://github.com/NikitaBerezhnyj/Udav) and [Based](https://github.com/NikitaBerezhnyj/Based). It provides a user-friendly and functional interface for writing and debugging code.

Features:

- Syntax highlighting for Based, Udav, and NikLang languages

- Automatic code completion

- Built-in terminal with custom commands to control the IDE

- Supports cross-platform application development (Windows, Linux, MacOS)

- Quick and convenient project search

- Real-time code editing and debugging

- Intuitive graphical interface based on React

NUB IDE was created to simplify and speed up development in Based, Udav, and NikLang as much as possible. It combines modern design, ease of use, and all the tools you need to be productive.

You can download and learn more about NUB IDE [here](https://github.com/NikitaBerezhnyj/NUB_IDE)

---

**_[See the IDE code](https://github.com/NikitaBerezhnyj/NUB_IDE)_**

## Extensions for VS code

The extension adds support for the Based programming language to VS Code.

**_Features_**.

- Syntax highlighting for .based files
- Auto-completion of Based language keywords

**_Usage_**.

After installing the extension, VS Code will automatically recognize .based files and apply syntax highlighting and auto-completion to them.

**_Installation_**

At the moment, the extension is not available in the VS Code marketplace, so you can install it only by cloning the repository and installing it locally. To do this, you will need to follow these steps:

1. Copy the repository to your PC using the terminal

```bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Then find the VS code folder on your PC

3. Copy the based-extension folder to the folder with the other extensions

**_Supported languages:_** Based (.based)

**_Dependencies:_** None

**_Version:_** 1.0.0

---

**_[See the extension code](./VS%20Code%20Extintion/based-extantion/)_**
