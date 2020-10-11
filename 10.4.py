Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import randint
a=randint(1,10)
q=int(input("Угадайте целое число от 1 до 10:"))
while q!=a:
if q<a:
print("Ваше число меньше, чем задумал компьютер")
elif q>a:
print("Ваше число больше, чем задумал компьютер")
else:
print("Вы угадали")
q = int(input("повторите"))
print("type 'end' to exit ")
e=str(input())