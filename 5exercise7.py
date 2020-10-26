import json
with open('file7.txt', 'r', encoding='UTF-8') as firms:
    a = firms.read().split()
print(a)

b = {a[i]: int(a[i+2])-int(a[i+3]) for i in range(0, len(a), 4)}
c = [b, {'average_profit': sum(b.values())/len(b)}]
print(c)

with open('file7.json', 'w') as fj_write:
    json.dump(c, fj_write)
