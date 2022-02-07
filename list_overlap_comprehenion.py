import random


random_list_first = [random.randrange(1, 10) for i in range(10)]
random_list_second = [random.randrange(1, 10) for i in range(10)]
result = [i for i in random_list_first if i in random_list_second]

def list_overlap_comprehension(random_list_first,random_list_second):
    common_list =[]
    for i in random_list_first:


        if i in random_list_second:
            common_list.append(i)




    return common_list


print(random_list_first)
print(random_list_second)
print(result)
print(list_overlap_comprehension(random_list_first,random_list_second))