Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "У лукоморья 123 дуб зеленый 456"
if 'я' in s:
print(f'1) В этой строке буква "я" встречается на {s.index("я")} позиции.')
else:
print('1) В этой строке нет буквы "я"')
print(f'2) В этой строке буква "у" встречается {s.count("у")} раз(a).')
if s.isalpha() == False:
print(f'3) Эта строка состоит не только из букв, в верхрнем регистре она выглядит так: {s.upper()}')
else:
print('3) Строка состоит только из букв')
if len(s) > 4:
print(f'4) Длина строки: {len(s)}, в нижнем регистре она выглядит так: {s.lower()}')
print(f'5) О{s[1:]}')