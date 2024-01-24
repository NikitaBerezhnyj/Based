# Based

Based repository has [Ukrainian :ukraine:](#мова-програмування-based-ukraine) and [English :uk:](#programming-language-based-uk) localizations

# Мова програмування Based :ukraine:

<p align='center'>
  <img src='./VS Code Extintion/based-extantion/icon-based.png' alt='Based icon' style="width:50%">
</p>

***Мова програмування Based*** - це базована мова програмування з відкритим вихідним кодом, створена в Україні з метою написання ще більш базованого коду.

Головною метою Based є збільшення кількості коду українською мовою. Вона має всі необхідні базові конструкції, такі як: умовні оператори, цикли, функції тощо. Таким чином ви зможете навчатися та писати код державною мовою.

Для створення Based було взято за основу мову програмування Python та інші відкриті матеріали, які можна знайти [тут](https://github.com/davidcallanan/py-myopl-code).

***Оскільки мова є абсолютно базованою, то логічно, що код має писатися у базованому стилі PascalCase.***

***Швидкий перехід між розділами:***

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

___

## Мова програмування Based

### Інсталяція

Щоб запустити інтерпретатор Based, вам необхідно буде виконати один з наступних варіантів:

___1. Скомпілювати інтерпретатор___ (це дасть вам більше можливостей у майбутньому)

___2. Запустити інтерпретатор без компіляції___ (це також підійде, якщо ви просто хочете спробувати мову Based і не хочете встановлювати або компілювати файли)

***1. Компіляція інтерпретатора***

Компілювання інтерпретатора необхідно для отримання виконуваного файлу based. Для цього виконайте наступні кроки:

1. Клонуйте репозиторій з GitHub:

``` bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Перейдіть в теку з проектом:

``` bash
cd Based/'Programming Language'/src
```

3. Встановіть пакет pyinstaller:

``` bash
pip install pyinstaller
```

4. Запустіть компіляцію:

``` bash
pyinstaller -F -n based shell.py
```

Після завершення компіляції в теці з проектом буде створений виконуваний файл based. Після ініціалізації цей файл можна буде використовувати для запуску програм мовою Based з будь-якої теки.

***2. Запустити інтерпретатор без компіляції***

Щоб запустити інтерпретатор без компіляції, виконайте наступну команду в теці з проектом:

1. Клонуйте репозиторій з GitHub:

``` bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Перейдіть в теку з проектом:

``` bash
cd Based/'Programming Language'/src
```

3. Запуск інтерпретатора

``` bash
python shell.py
```

Ця команда запустить інтерпретатор Based в теці з проектом. Ви зможете написати і запустити програму, не компілюючи інтерпретатор.

#### Ініціалізація

Ініціалізація інтерпретатора Based необхідна для того, щоб можна було використовувати його з будь-якої теки на вашому комп'ютері. Для цього виконайте наступні дії:
1. Відкрийте скомпільований файл інтерпретатора

``` bash
./based
```

2. Використайте наступну команду:
   
``` python
ініціалізація
```

3. Завершіть роботу інтерпретатора:

``` python
вихід
```

Після ініціалізації інтерпретатора файл based буде скопійовано в теку з іншими утилітами, що дасть можливість використовувати його для запуску програм мовою Based з будь-якої теки.

#### Деніціалізація

Деініціалізація інтерпретатора Based необхідна, якщо ви більше не плануєте використовувати його. Для цього виконайте наступні кроки:

1. Відкрийте інтерпретатор

``` bash
based
```

2. Використайте наступну команду:
   
``` python
деініціалізація
```

3. Завершіть роботу інтерпретатора:

``` python
вихід
```

Це видалить Based з теки з утилітами, але залишить його у теці з проєктом, тому ви зможете використовувати його і потім, якщо забажаєте

### Синтаксис

Я намагався зробити синтаксис Based простим і зрозумілим для початківців, але при цьому потужним і гнучким для досвідчених розробників. Тож перейдімо до роботи з мовою.

***Створення коментарів***

``` python
# Це коментар, його інтерпретатор не бачить
```

***Вивід тексту на екран***

``` python
# Вивід звичайного тексту
друк("Привіт, Світ!")

# Вивід змінної
змінна А = 10
друк(А)
```

***Оголошення змінних***

``` python
# Цілочисельна змінна
змінна А = 10

# Дійсна змінна
змінна Б = 10.5

# Рядкова змінна
змінна В = "Рядок"

# Булева змінна
змінна Г = правда

```

***Ввід користувача***

``` python
# Записується рядок
змінна А = ввід()

# Записується число
змінна Б = ввід_числа()
```

***Оголошення масивів***

``` python
# Оголошення масиву цілих чисел
змінна А = [0, 1]

# Оголошення масиву дійсних чисел
змінна Б = [0.5, 1.001]

# Оголошення масиву рядків
змінна В = ["привіт", "світ"]

# Оголошення масиву булевих виразів
змінна Г = [правда, правда, брехня]

```

***Умови if (якщо), else if (інакше_якщо) та else (інакше)***

``` python
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
якщо А < 5 тоді; друк("А < 5") інакше_якщо А > 5 і А < 8 тоді; друк("А < 5 і А > 8") інакше друк("А > 8")

# Умова якщо-інакше_якщо-інакше повний запис
якщо А < 5 тоді 
    друк("А < 5") 
інакше_якщо А > 5 і А < 8 тоді 
    друк("А < 5 і А > 8") 
інакше друк("А > 8")
```

***Оголошення циклу while (поки)***

``` python
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

***Оголошення циклу for (для_кожного)***

``` python
# Приклад циклу for (для_кожного) у варіанті для одного рядка
для_кожного Лічильника = 0 до 10 тоді друк(л)

# Приклад циклу for (для_кожного) в розписаному варіанті
для_кожного Лічильника = 0 до 10 тоді
    друк("Привіт, Світ!")
кінець
```

***Оголошення функції***

``` python
# Найпростіші функції, що можна записати в один рядок записуються так:
функція Привіт_світ() -> друк("Привіт, світ!")

# Функції, що не можна записати в один рядок записуються так:
функція ПривітСвіт()
	змінна Рази = ввід_числа()
	друк(Рази)
	для_кожного Лічильник = 0 до Рази тоді
		друк("Привіт, Світ!")
	кінець
кінець
```

### Приклади коду

***Міні гра Вгадай Число, в якій користувач вгадує число, яке програма загадала. Кількість спроб встановлюється користувачем.***

``` python
функція Гра(КількістьСпроб, ВиграшнеЧисло)
    для_кожного спроба = 0 до КількістьСпроб тоді
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

***Максимально простий, консольний калькулятор, який виконує арифметичні операції. Користувач обирає операцію, вводить числа, і отримує результат. Програма запитує користувача, чи бажає він продовжити обчислення.***

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

- ***допомога*** - показує всі доступні команди для терміналу інтерпретатора та базовий синтаксис мови

- ***запуск*** - запускає файл .based (приклад використання: ***запуск("приклад.based")***)

- ***цт*** - ця тека. Показує шлях до поточної теки

- ***лф*** - лист файлів. Показує вміст поточної теки

- ***зт*** - змінити теку. Змінює поточну теку

- ***сф*** - створити файл. Створює файл у поточній теці (приклад використання: ***сф приклад.txt***, якщо розширення не вказане, то воно буде за замовчуванням встановлене, як .based)

- ***ст*** - створити теку. Створює теку у поточній (приклад використання: ***ст тестова_тека***)

- ***очистити*** - очищує термінал інтерпретатора

- ***вихід*** - закриває інтерпретатор

- ***версія*** - показує поточну версію Based, що встановлена на вашому ПК

- ***БАЗА*** - виводить основну інформацію про стан Based

___

***[Дивитись код мови](./Programming%20Language/)***

## Власне IDE для Based

Поки що не готове

___

***[Дивитись код IDE](./Based%20IDE/)***

## Розширення для VS code

Розширення додає підтримку мови програмування Based у VS Code.

***Функціональність***

- Підсвічування синтаксису для файлів .based
- Автодоповнення ключових слів мови Based

***Використання***

Після встановлення розширення, VS Code автоматично розпізнаватиме файли .based і застосовуватиме до них підсвічування і автодоповнення.

***Установка***

На даний момент розширення не доступне в маркетплейсі VS Code, тож його можна встановити тільки клонувавши репозиторій та встановивши його локально. Для цього вам необхідно буде виконати наступні кроки:

1. Копіювати репозиторій на свій ПК через термінал
```bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Потім знайти теку VS code на вашому ПК
   
3. Скопіювати теку based-extension до теки з іншими розширеннями

***Підтримувані мови:*** Based (.based)

***Залежності:*** Не має

***Версія:*** 1.0.0
___

***[Дивитись код розширення](./VS%20Code%20Extintion/based-extantion/)***

___












<!-- _________________________________________________________________ -->













# Programming language Based :uk:

<p align='center'>
  <img src='./VS Code Extintion/based-extantion/icon-based.png' alt='Based icon' style="width:50%">
</p>

The ***Based*** programming language is a basic open source programming language created in Ukraine with the aim of writing even more basic code.

The main goal of Based is to increase the amount of code in the Ukrainian language. It has all the necessary basic constructs, such as conditional statements, loops, functions, etc. This way, you can learn and write code in the national language.

To create Based, we used the Python programming language and other open source materials that can be found [here] (https://github.com/davidcallanan/py-myopl-code).

***Since the language is absolutely basic, it is logical that the code should be written in the basic PascalCase style.

***Quick transition between sections:***

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

___

## Programming language Based

### Installation

To start the Based interpreter, you will need to do one of the following:

___1. Compile the interpreter___ (this will give you more options in the future)

___2. Run the interpreter without compiling___ (this is also suitable if you just want to try the Based language and do not want to install or compile files)

***1. Compile the interpreter***.

Compiling the interpreter is necessary to get the based executable. To do this, follow these steps:

1. Clone the repository from GitHub:

``` bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Change to the project folder:

``` bash
cd Based/'Programming Language'/src
```

3. Install the package pyinstaller:

``` bash
pip install pyinstaller
```

4. Run the compilation:

``` bash
pyinstaller -F -n based shell.py
```

After compilation is complete, the based executable file will be created in the project folder. After initialization, this file can be used to run programs in the Based language from any folder.

***2. Run the interpreter without compilation***

To run the interpreter without compiling, run the following command in the project folder:

1. Clone the repository from GitHub:

``` bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Change to the project folder:

``` bash
cd Based/'Programming Language'/src
```

3. Run the interpreter

``` bash
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

``` python
ініціалізація
```

3. Shut down the interpreter:

``` python
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

``` python
деініціалізація
```

3. Shut down the interpreter:

``` python
вихід
```

This will remove Based from the utilities folder, but leave it in the project folder, so you can use it later if you want to.

### Syntax.

I've tried to make the Based syntax simple and easy to understand for beginners, but powerful and flexible for advanced developers. So let's get down to business with the language.

***Creating comments***

``` python
# This is a comment, the interpreter does not see it
```

***Display text on the screen***

``` python
# Plain text output
друк("Привіт, Світ!")

# Outputting a variable
змінна А = 10
друк(А)
```

***Declaration of variables***

``` python
# Integer variable
змінна А = 10

# Float variable
змінна Б = 10.5

# String variable
змінна В = "Рядок"

# Boolean variable
змінна Г = правда

```

***User input***

``` python
# The string is written
змінна А = ввід()

# The number is written
змінна Б = ввід_числа()
```

***Оголошення масивів***

``` python
# Declaring an array of integers
змінна А = [0, 1]

# Declaring an array of real numbers
змінна Б = [0.5, 1.001]

# Declaring an array of strings
змінна В = ["привіт", "світ"]

# Declaring an array of Boolean expressions
змінна Г = [правда, правда, брехня]

```

***If, else if, and else conditions***

``` python
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
якщо А < 5 тоді; друк("А < 5") інакше_якщо А > 5 і А < 8 тоді; друк("А < 5 і А > 8") інакше друк("А > 8")

# Condition if_elif_else full record
якщо А < 5 тоді 
    друк("А < 5") 
інакше_якщо А > 5 і А < 8 тоді 
    друк("А < 5 і А > 8") 
інакше друк("А > 8")
```

***Declaring a while loop***

``` python
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

***Declaring a for loop**

``` python
# An example of a for loop in the version for one line
для_кожного Лічильника = 0 до 10 тоді друк(л)

# An example of a for loop in the painted version
для_кожного Лічильника = 0 до 10 тоді
    друк("Привіт, Світ!")
кінець
```

***Declaring a function***

``` python
# The simplest functions that can be written in one line are written like this:
функція Привіт_світ() -> друк("Привіт, світ!")

# Functions that cannot be written in one line are written like this:
функція ПривітСвіт()
	змінна Рази = ввід_числа()
	друк(Рази)
	для_кожного Лічильник = 0 до Рази тоді
		друк("Привіт, Світ!")
	кінець
кінець
```

### Code examples

***Guess the Number mini-game in which the user guesses the number that the program has guessed. The number of attempts is set by the user.***

``` python
функція Гра(КількістьСпроб, ВиграшнеЧисло)
    для_кожного спроба = 0 до КількістьСпроб тоді
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

***The simplest possible console calculator that performs arithmetic operations. The user selects an operation, enters numbers, and gets the result. The program asks the user if he or she wants to continue the calculation.***

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

- ***допомога*** - shows all available commands for the interpreter terminal and the basic syntax of the language

- ***запуск*** - runs the .based file (example of use: ***запуск("приклад.based")***)

- ***цт*** - this folder. Shows the path to the current folder

- ***лф*** - a list of files. Shows the contents of the current folder

- ***зт*** - change folder. Changes the current folder

- ***сф*** - create file. Creates a file in the current folder (example of use: ***сф приклад.txt***, if the extension is not specified, it will be set to .based by default)

- ***ст*** - create folder. Creates a folder in the current one (example of use: ***ст тестова_тека***)

- ***очистити*** - clears the interpreter terminal

- ***вихід*** - closes the interpreter

- ***версія*** - shows the current version of Based installed on your PC

- ***БАЗА*** - displays basic information about the state of the Based

___

***[Дивитись код мови](./Programming%20Language/)***

## A custom IDE for Based

Not ready yet

___

***[See the IDE code](./Based%20IDE/)***

## Extensions for VS code

The extension adds support for the Based programming language to VS Code.

***Features***.

- Syntax highlighting for .based files
- Auto-completion of Based language keywords

***Usage***.

After installing the extension, VS Code will automatically recognize .based files and apply syntax highlighting and auto-completion to them.

***Installation***

At the moment, the extension is not available in the VS Code marketplace, so you can install it only by cloning the repository and installing it locally. To do this, you will need to follow these steps:

1. Copy the repository to your PC using the terminal

```bash
git clone https://github.com/NikitaBerezhnyj/Based.git
```

2. Then find the VS code folder on your PC

3. Copy the based-extension folder to the folder with the other extensions

***Supported languages:*** Based (.based)

***Dependencies:*** None

***Version:*** 1.0.0
___

***[See the extension code](./VS%20Code%20Extintion/based-extantion/)***