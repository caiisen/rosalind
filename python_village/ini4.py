a = 4514
b = 8662
if a % 2 != 1:
    a = a + 1
if b % 2 == 1:
    b = b + 1
j = 0
for i in range(a,b,2):
    j = j + i
print(j)