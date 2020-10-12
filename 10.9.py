Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = input()
l = []
m = 0
for i in range(len(s)):
if s[i] in '1234567890':
print(s[i])
l.append(int(s[i]))
print (l)
for i in range(len(l)):
if l[i] > m:
m = l[i]
print (m)
print (sum(l))
print(len(l))