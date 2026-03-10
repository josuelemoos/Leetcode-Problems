l1 = [2,7,11,15]
var = 9
res = []

i = 0


for y in l1:
    j = 0
    for x in l1:
        soma = y + x
        if soma == var and i != j:
            res.append(i)
            res.append(j)
            break
            #return soma
        j = j+1
    if soma == var and i != j:
        break
    i = i+1

print(res)