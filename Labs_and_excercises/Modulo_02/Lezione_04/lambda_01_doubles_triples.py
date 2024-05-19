my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = lambda b: b ** 2
c = lambda d: d * d * d

list_square = list(map(a, my_list))
list_cube = list(map(c, my_list))

print('Original:', my_list)
print('Squared:',    list_square)
print('Cube:',       list_cube)