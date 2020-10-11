Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = [3, 6, 7, 4, -5, 4, 3, -1]
if sum(l) > 2:
print (len(l))
a = max(l)
b = min(l)
if abs(a-b) >= 10:
l.sort()
print (l)
else:
print("разность меньше 10")
print("type 'end' to exit ")
e=str(input())