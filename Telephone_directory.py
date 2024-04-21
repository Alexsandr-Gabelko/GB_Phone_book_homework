# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной.
# Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

# Поиск
def wallpaper_search(dt, search_data):
    array = []
    with open ('telephone_book.txt', 'r') as file:
        print('Список телефонных номеров')
        for data in file:
            listRes = list(data.split(' '))
            if listRes[dt-1] == search_data:
                array.append(listRes)
    if not array:
        print('Такого абонента нет в справочнике!')            
    else:
        for res in array:
            print(*res, sep=", ")  
         

# Меню поиска
def search_menu():
    data = ''
    while data != 1 or data != 2:
        print('По каким параметрам произаодить поиск')
        print('1 - По фамилии')
        print('2 - По имени')
        # print('3 - По отчеству')
        data = (input('Введите идентификатор - '))
        if data == '1':
            search_data = (input('Введите фамилию - '))
            dt = 1
            wallpaper_search(dt, search_data)
            return
        elif data == '2':
            dt = 2
            search_data = (input('Введите имя - '))
            wallpaper_search(dt, search_data)
            return
        else:
            print('Введен неверный идентификатор')
    return        

# Вывести весь список
def entire_directory():
    with open ('telephone_book.txt', 'r') as file:
        print('Список телефонных номеров')
        for list in file:
            print(list)
        print(' ')    
    return        

# Добавить новую запись в справочник
def add_new_contact(cont):
    contact_str = ''
    with open ('telephone_book.txt', 'a', encoding='utf-8') as file:
        contact_str = ' '.join(cont)
        file.write(contact_str + '\n')
    print('В телефонную книгу добавлена запись: ', contact_str, '\n')    
    return    

# Эспортировать данные
def data_export():
    with open ('telephone_book.txt', 'r') as file:
        with open ('export.txt', 'a', encoding='utf-8') as export:
            print('Экспорт данных в файл export.txt')
            for data in file:
                export.write(data) # + '\n')
    print('Экспорт данных в файл export.txt выполнен')
    return

# Скопировать  по номеру сироки
def copy_by_line_numbery(number):
    i = 0
    with open ('telephone_book.txt', 'r') as file:
        for data in file:
            i += 1
            if number == i:
                with open ('export.txt', 'a', encoding='utf-8') as export:
                    export.write(data)
                print(f'Строка с номером {number} скопирована в файл export.txt')
                return 
        print('Такой строки нет в файле')
        return        
            
# Главное меню
def main():
    menu = ''
    while menu != '0':
        print('Какое действие вы хотите выполнить ?')
        print('1 - Найти данные в справочнике')
        print('2 - Добавить данные в справочник')
        print('3 - Экспортировать данные из справочника')
        print('4 - Вывести весь справочник')
        print('5 - Скопировать данные справочника по номеру строки')
        print('0 - Выйти из программы')
        print(' ')
        menu = (input('Введите идентификатор - '))
        print(' ')
        if menu == '1':
            search_menu()
        elif menu == '2':
            first_name = input('Фамилия: ')
            second_name = input('Имя: ')
            pater_name =  input('Отчество: ')
            phone_number = input('Номер телефона :')
            contact = [first_name, second_name, pater_name, phone_number]
            add_new_contact(contact)
        elif menu == '3':
            data_export()
        elif menu == '4': 
            entire_directory()
        elif menu == '5':
            line_number = input('Введите номер строки для копирования данных из справочника - ')
            copy_by_line_numbery(int(line_number))    
        elif menu == '0':
            break     
        else:
            print("Данной команды нет, введите другую")    
            print(' ')
        
main()