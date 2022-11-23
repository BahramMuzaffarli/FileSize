l1 = [[5,7,8],
      [3,5,6],
      [4,2,1]]

l1_0 = l1[0]
l1_1 = l1[1]
l1_2 = l1[2]
print(l1_0)
print(l1_1)
print(l1_2)

Sum_all = int(l1[0][0] + l1[0][1] + l1[0][2] + l1[1][0] + l1[1][1] + l1[1][2] + l1[2][0] + l1[2][1] + l1[2][2])
print(Sum_all)

Column_all = [(l1[0][0] + l1[1][0] + l1[2][0]), (l1[0][1] + l1[1][1] + l1[2][1]) , (l1[0][2] + l1[1][2] + l1[2][2])]
print(Column_all)

Row_all = [(l1[0][0] + l1[0][1] + l1[0][2]), (l1[1][0] + l1[1][1] + l1[1][2]), (l1[2][0] + l1[2][1] + l1[2][2]) ]
print(Row_all)

for el1 in l1_0:
    print(el1)
for el2 in l1_1:
    print(el2)
for el3 in l1_2:
    print(el3)

print(el1 + el2 + el3)
