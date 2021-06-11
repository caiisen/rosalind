n = 28
k = 5
list = [1,1]
for i in range(2,n):
    list.append(list[i-1] + list[i-2]*k)
print(list[-1])