s = [1,2,3,2,3,3]
max = s[0]
max_count = s.count(max)
for el in s:
   if s.count(el)>max_count:
     max = el
     max_count = s.count(el)
print(max)