dict_1 = {"user": "Admin", "nickname": "qwert", "tean": ["Player1", "Player2"]} #нейзменный словарь
dict_2 = {"Book1": 50, "Book2": 20, "Book3": 15}

list_group = ["name1", "name2", "name3", "name4", "name5"]
v = 10
dict_4 = dict.fromkeys(list_group, v)
print(dict_4)
'''
a = dict_2["Book2"]
print(a)
'''
"""
dict_2["Book4"] = 70
dict_2.update({"Book5": 90})
dict_2.setdefault("Book6", 34)
#добавляем
"""
#keys, values, teb
"""
for elem in dict_2.values():
    print(elem)

print(dict_2)

for elem in dict_2.items():
    print(elem)

for elem in dict_2.keys():
    key = dict_2[elem]
    print(elem)
"""
"""
#-----Основные методы-------
keys_in_dict_2= dict_2.keys()
print(keys_in_dict_2)

c = dict_1.get("Book2", 0)
print(c)

c = dict_2.get("Book1", 0)
print(c)
"""
"""
dict_2 = {"Book1": 50, "Book2": 20, "Book3": 15}
dict_3 = {"Book4": 60, "Book5": 2}
dict_2.update(dict_3)
print(dict_2)

val = dict_2.pop("Book1") #pop удаляет а также хранит эл
print(val)
print(dict_2)

dict_2.clear()# удаляет навсегда всё
print(dict_2)
"""
'''
new_dict_1=dict_1.copy()
print(new_dict_1)
dict_1.clear()
print(new_dict_1)

val = dict_2.setdefault("Book4", 10)
print(dict_2)
'''