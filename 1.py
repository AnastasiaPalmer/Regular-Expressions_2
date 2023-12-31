import re

"""
"Подивіться, як працюють прості шаблони та квантифікатори. Відкрийте пісочницю - https://regex101.com/. 

Розв'яжіть такі завдання для тексту нижче:",
 "1 Знайдіть усі натуральні числа (можливо, оточені літерами);",
 "2 Знайдіть усі «слова», написані капсом (тобто великими літерами), можливо всередині справжніх слів (аааБББввв);",
 "3 Знайдіть слова, в яких є українська літера, за якою може бути цифра;",
 "4 Знайдіть усі слова, що починаються з української або латинської великої літери (\\b – межа слова);",
 "5 Знайдіть слова, які починаються на голосну (\\b - межа слова);",
 "6 Знайдіть усі натуральні числа, що не знаходяться всередині або на межі слова;",
 "7 Знайдіть рядки, в яких є символ * ;",
 "8 Знайдіть рядки, в яких є дужки, що відкриваються і потім закриваються в кінці;",
 "9 Виділіть одним весь шматок змісту (наприкінці прикладу, разом із тегами);",
 "10 Виділіть одним лише текстову частину змісту, без тегів;",
 "11 Знайдіть порожні рядки."
"""

text = """Регулярні вирази є схожим, але набагато сильнішим інструментом.
для пошуку рядків, їх перевірки на відповідність якомусь шаблону та іншій подібній
роботі. Англомовна назва цього інструменту – Regular Expressions або просто RegExp.
Строго кажучи, регулярні вирази – спеціальна мова для опису шаблонів рядків.

АААА аааа АаАаАаАа 123 123 12345 11223344
А1Б2В3 АА11 ББ22ВВ 33ГГ44

Тест! Ще! Даєш! ЇЇ

QwertyЙцукен

+-,/[](), *** (***), a*(b+[c+d])*e/f+g-h

!!""\"####$$$$$%%%%%&&&'''(((((!!!))***++++,,,,,-----..// :::;;;;<<<<<===>>>?????
@@@@@[[[[\\\]]]]]]^^^__``````{{{{|||||}}}}}~~~~~

<a href="#10">10: CamelCase -> under_score</a>;
<a href="#11">11: Видалення повторів</a>;
<a href="#12">12: Близькі слова</a>;
<a href="#13">13: Форматування великих чисел</a>;
<a href="#14">14: Розділити текст на пропозиції</a>;
<a href="#15">15: Форматування номера телефону</a>;
<a href="#16">16: Пошук e-mailів — 2</a>;"""

# усі натуральні числа
print("1) All natural numbers: ", re.findall("[a-zA-Zа-яА-Я]*[0-9]+[a-zA-Zа-яА-Я]*", text))

# усі «слова», написані капсом
print("2) All CAPS WORDS: ", re.findall("\w?[A-ZА-Я]{2}\w?", text))

# слова, в яких є українська літера, за якою може бути цифра
print("3) Ua words: ", re.findall("[А-Яа-яіїєІЇЄ]+[0-9]?", text))

# усі слова, що починаються з української або латинської великої літери
print("4) Ua and En Words: ", re.findall(r"[A-ZА-ЯІЇЄ]\w+", text))

# Знайдіть слова, які починаються на голосну
print("5) Starts with vowel letter: ", re.findall(r"\b[AEIOUYaeiouyАаУуЕеІіЇїЄєИиЮюЯя]+\w+", text))

# Знайдіть усі натуральні числа, що не знаходяться всередині або на межі слова
print("6) Numbers with no words: ", re.findall(r"\b[0-9]+", text))

# Знайдіть рядки, в яких є символ *
print("7) Lines with *: ", re.findall(r".*[*].*", text))

# рядки, в яких є дужки, що відкриваються і потім закриваються в кінці
print("8) Lines with *: ", re.findall(r".*[(].*[)].*", text))

# Виділіть одним весь шматок змісту (наприкінці прикладу, разом із тегами)
print("9) Shmatok: ", re.findall("<a.*>", text))

# Виділіть одним лише текстову частину змісту, без тегів
print("10) Plain text: ", re.findall(r"<a[^>]*>([^<]+)<", text))

# Знайдіть порожні рядки
print("11) Plain text: ", re.findall("\n\n", text))  # "^$"

