Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
if 'привет' in l:
l.remove('привет')
print(l)
else:
l.append('привет')
if l.count(4)>1:
l.clear()
print(l)
print("type 'end' to exit ")
e=str(input())
