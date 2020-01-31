ga = {0: [1,1,1]}
print(ga)
for i in range(5):
    var = i+4
    print(var)
    ga.update({var:[[1,1],0]})

print(ga)