a = int((input("введите 1 число:")))
b = int(input("введите 2 число:"))

try:
    res = a/b
    print(res)
except ZeroDivisionError:
    print("А НА НУЛЬ НЕ ДЕЛИТСЯ:)")