

def count_unic_el(lst):
    dict_1 = {}
    for el in lst:
        dict_1[el] = dict_1.get(el, 0) + 1
    return dict_1

list_1 = [1, 2, 3, 4, 6, 6, 6, 4, 4, 2, 3, 4]
result = count_unic_el(list_1)

print(result)