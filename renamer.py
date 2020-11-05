import os

print("Введите полное название директории:")
path = input()#'''C:\\Users\\Артур\\Documents\\работа''' #введите полное название директории

file_list = os.listdir(path)

print("Введите строку, которую нужно вписать в название")
a = input()
print("Введите строчку, которую нужно удалить из названия")
b = input()

for file in file_list:
    os.rename(path + '\\' + file, path + '\\' + file.replace(b,a))