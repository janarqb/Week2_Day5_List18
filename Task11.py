i = [100, 200, -5, -100, 89]
min = 1000
for item in range(len(i)):
    s=int(i[item])
    if (s<min)and(s>0):
        min = s
print(min)