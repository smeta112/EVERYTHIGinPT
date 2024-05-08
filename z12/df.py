
list1=["pyton", "c++", "java"]

tuple_1 = ("pyton", "c++", "java")
tuple_2= (1, 3, 23, 6, 78)

print(len(tuple_2)) # сколько
sorted_tuple_2 = sorted(tuple_2) # со списком
print(sorted_tuple_2)#по возрастанию
#print(f"List size: {list1.__sizeof__()}")
#print(f"Typle size: {tuple_1.__sizeof__()}")
print(tuple_1[0:4])
print(tuple_1[:4])
print(tuple_1[2:])
print(tuple_2[::2])

count_el= tuple_2.count(1)
print(count_el)

index_el =tuple_2.index(1) #номер
print(index_el)

is_seven = 7 in tuple_2 #есть ль
print(is_seven)

new_tuple = tuple_1 + tuple_2
print(new_tuple)