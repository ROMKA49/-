Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = int(input())
s = 0
while a != 0:
q = a % 10
if q % 2 == 1:
s = s + q*q
a = a // 10
print (s)
print("type 'end' to exit ")
e=str(input())