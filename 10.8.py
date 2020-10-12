Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = input()
l = s.split(' ')
m = 0
c = 0
for i in range(len(l)):
if len(l[i]) > m:
m = len(l[i])
c = i + 1
print (c)
print("type 'end' to exit ")
e=str(input())