Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import randint
n = 3
m = 5
l=[[randint(1, 9) for i in range(n)] for i in range(m)]
for i in l:
print()
for j in i:
print (j, end=" ")
c = 0
ind = 0
for i in range(n):
for j in range(i):
cn = l[i].count(l[i][j])
if cn > c:
c = cn
ind = i
print()
print (c)
print (ind+1)
print("type 'end' to exit ")
e=str(input())