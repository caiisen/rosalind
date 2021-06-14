n = 28
k = 5
month = 1
newborn = []
reproductive = []
while month == 1:
    newborn.append(1)
    reproductive.append(0)
    month = month + 1
while month <= n:
    reproductive.append(newborn[month - 2] + reproductive[month - 2])
    newborn.append(reproductive[month - 2] * k)
    month = month + 1
print(newborn[-1] + reproductive[-1])