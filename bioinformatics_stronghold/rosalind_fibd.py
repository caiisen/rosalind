n = 90
m = 16
month = 1
newborn = []
reproductive = []
die = []
while month == 1:
    newborn.append(1)
    reproductive.append(0)
    die.append(0)
    month = month + 1
while month <= m:
    reproductive.append(newborn[month - 2] + reproductive[month - 2])
    newborn.append(reproductive[month - 2])
    die.append(0)
    month = month + 1
while month > m and month <= n:
    die.append(newborn[month - m - 1])
    reproductive.append(newborn[month - 2] + reproductive[month - 2] - die[month - 1])
    newborn.append(reproductive[month - 2])
    month = month + 1
print(newborn[-1] + reproductive[-1])

