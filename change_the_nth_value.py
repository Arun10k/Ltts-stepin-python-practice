my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
for i in range(len(my_list)-1):
    my_list[i] = my_list[i+1]

print(my_list)