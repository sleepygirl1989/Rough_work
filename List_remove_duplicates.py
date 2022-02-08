def list_without_duplicates(list_value):
    list_without_duplicate =[]
    for i in list_value:
        if i not in list_without_duplicate:
            list_without_duplicate.append(i)
    return list_without_duplicate

print(list_without_duplicates([1,4,5,7,5,6,8,9,1]))