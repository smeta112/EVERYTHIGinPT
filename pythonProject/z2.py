dict_1 = {"B1": 50, "B2": 20, "B3": 15, "B4": 90, "B5": 10, "B6": 45}


def get_min_value(dict):
    a = min(dict_1.values())
    for key, value in dict.items():
        if value== a:
            return key

result = get_min_value(dict_1)
print(result)
