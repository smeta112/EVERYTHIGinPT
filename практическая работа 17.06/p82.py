try:
    file = open("file.txt", "r")
    print("файл есть")
except FileNotFoundError:
    print(" ФАЙЛА НЕ СУЩЕСТВУЕТ")
    exit()