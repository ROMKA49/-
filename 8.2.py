Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def If(s, n):
if n > len(s):
print(s.upper())
else:
print(s)
return 0;
s = str(input())
n = int(input())