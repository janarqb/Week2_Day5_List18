num = [2, 4, 6, 7, 99, 101]
min = 0 
for i in range (len(num)):
    if num[i] % 2 == 1:
        min = num[i]
for i in range(len(num)):
    if num[i] % 2 == 1:
        if num[i] < min:
           min = num[i]
if min != 0:
    print(min)
else:
    print(0)
