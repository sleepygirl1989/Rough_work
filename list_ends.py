import random

random_list= [random.randrange(1, 10) for i in range(10)]

def list_ends(random_list):
    n=len(random_list)

    list_end=[random_list[0],random_list[n-1]]
    return list_end

print(random_list)
print(list_ends(random_list))