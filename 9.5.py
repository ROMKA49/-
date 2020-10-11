Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import choice
l = ['самовар', 'весна', 'лето']
s=choice(l)
b=choice(s)
a = s.index(b)
print(s[0:a] +'?' +s[a+1:len(s)])
print ("введите букву")
q = str(input())
if b==q:
print ("правильно!")
else:
print ("не правильно!")
print("type 'end' to exit ")
e=str(input())
