Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = [-8, 8, 6.0, 5, 'строка', -3.1]
s = 0
for i in l:
if type(i) == int:
s = s + i
elif type(i) == float:
s = s + i
print (s)
print("type 'end' to exit ")
e=str(input())