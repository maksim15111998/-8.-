from logger import input_data, print_data, modify_data, select_and_delete_data

def interface():
    print("Добрый день! Это бот-помощник. \n"
           "Что Вы хотите сделать?\n"
           "1 - Записать данные \n"
           "2 - Вывести данные\n"
           "3 - Изменить данные \n"
           "4 - Удалить данные")
    command = int(input("Ваш выбор: "))

    while command < 1 or command > 4:
        command = int(input("Ошибка! Ваш выбор: "))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        modify_data()
    elif command == 4:
        select_and_delete_data()    

