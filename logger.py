from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '))
    if var == 1:
       with open("data_first_variant.csv", "a", encoding="utf-8") as file:
           file.write( f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n') 



def print_data():
    print("1 файл: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end ="")
    print()
    print("2 файл: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i !='\n':
                print(i, end="")

def modify_data():
    with open("data_first_variant.csv", "r+", encoding="utf-8") as file:
        data = file.readlines()
        print("Доступные данные из файла 'data_first_variant.csv':")
        for i, line in enumerate(data):
             print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно изменить: "))
        if selection>0 and selection<= len(data):
            new_data = input("Введите новые данные: ")
            data[selection-1] = new_data + '\n'
            file.seek(0)
            file.writelines(data)
            file.truncate()
        else:
            print("Некорретный номер данных.")
    print ()
    with open("data_second_variant.csv", "r+", encoding="utf-8") as file:
        data = file.readlines()
        print("Доступные данные из файла 'data_second_variant.csv':")
        for i, line in enumerate(data):
             print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно изменить: "))
        if selection>0 and selection<= len(data):
            new_data = input("Введите новые данные: ")
            data[selection-1] = new_data + '\n'
            file.seek(0)
            file.writelines(data)
            file.truncate()
        else:
            print("Некорретный номер данных.")

def select_and_delete_data():
        with open("data_first_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
        print("Доступные данные из файла 'data_first_variant.csv' (введите 0 чтобы перейти к следующему файлу):")
        for i, line in enumerate(data):
            print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно удалить: "))
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:
            for i, line in enumerate(data):
                if i+1 != selection:
                    file.write(line)

    
        with open("data_second_variant.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
        print("Доступные данные из файла 'data_second_variant.csv' (введите 0 чтобы выйти):")
        for i, line in enumerate(data):
            print(f"{i+1}. {line.strip()}")
        selection = int(input("Введите номер данных, которые нужно удалить: "))
        with open("data_second_variant.csv", "w", encoding="utf-8") as file:
            for i, line in enumerate(data):
                if i+1 != selection:
                    file.write(line)
            
