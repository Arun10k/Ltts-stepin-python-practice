my_tuple = 4,42,5,2,3,432,33,22,22,11,11

for ele in set(my_tuple):
    if my_tuple.count(ele) > 1:
        print(ele)
