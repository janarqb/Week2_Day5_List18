def get_position(p, h):
    return next((p.index(i)+1 for i in p if i < h), len(p)+1)
 
ppl = [165, 163, 160, 160, 157, 157, 155, 154]
height = 162
print(get_position(sorted(ppl, reverse=True), height))