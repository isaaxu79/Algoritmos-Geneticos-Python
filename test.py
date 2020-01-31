# ga = {0: [1,1,1]}
# print(ga)
# for i in range(5):
#     var = i+4
#     print(var)
#     if var == 6:
#         ga.update({var:[[0,2],0]})
#     else:
#         ga.update({var:[[1,1],0]})

# ht = [1,2,3] == [1,1,3]
# # print(ht)
# tienda = {1:[7,3,10], 2:[6,3,8], 3:[4,5,3], 4:[10,5,4], 5:[12,10,2], 6:[3,8,6], 7:[5,8,1], 8:[8,9,2], 9:[9,12,0], 10:[12,12,2]}

# population = { 0:[[tienda[2],tienda[4]],0], 1:[[tienda[2],tienda[8]],0], 2:[[tienda[10],tienda[1]],0], 3:[[tienda[5],tienda[2]],0] }
# population[0][0][0] = tienda[1]


# print(population[0][0][1])
import random

print(random.randrange(2))

for _ in range(11):
    print(random.randrange(10))