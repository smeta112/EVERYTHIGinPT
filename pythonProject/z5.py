dict_1 = {"B1": 90, "B2": 20, "B3": 15, "B4": 90, "B5": 10, "B6": 45}

#append
def get_max_value(dict):
    a = max(dict_1.values())
    list_for_keys = []
    for key, value in dict.items():
        if value== a:
            list_for_keys.append(key)
    return list_for_keys


result = get_max_value(dict_1)
print(result)