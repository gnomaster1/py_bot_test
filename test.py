
with open('goats.txt','r') as file:
    col = file.readlines()


i = 0
color = []
goats = []
res = {}
val = 0
while col[i].strip() != "GOATS":
    color.append(col[i].strip())
    i += 1
i +=1

while i < len(col):
    goats.append(col[i].strip())
    i += 1
for i in goats:
    res[i] = res.get(i,0) + 1
with open('a.txt', 'w') as output:
    for k,v in res.items():
        val += v
        per = (7/val* 100)
        if v > per:
            print(k, file=output)







# for i in col:
#     a = i.strip().split()
#     #print(a)
#     if a[0] == 'GOATS':
#         color.append(a[0])
#         break
# goats.append(a)
#
# print(color)
# print(goats)