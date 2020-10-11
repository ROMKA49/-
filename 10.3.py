Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = []
n = int(input())
for i in range(n):
a = int(input())
l.append(a)
if n % 2 != 0:
print ("поменять нельзя")
else:
print(l[n // 2 :] + l[0: n // 2])
print("type 'end' to exit ")
e=str(input())