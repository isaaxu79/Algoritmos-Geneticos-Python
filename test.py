ga = {0: [1,1,1]}
print(ga)
for i in range(5):
    var = i+4
    print(var)
    if var == 6:
        ga.update({var:[[0,2],0]})
    else:
        ga.update({var:[[1,1],0]})

print(ga)
ga.pop(7)
print(ga)
ex = ga.get(6)
print(ex)