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


# Добавить новую запись в справочник
def add_new_contact(cont):
    contact_str = ''
    with open ('telephone_book.txt', 'a', encoding='utf-8') as file:
    # with open ('telephone_book.txt', 'a') as file:    
        contact_str = ' '.join(cont)
        file.write(contact_str + '\n')
    print('В телефонную книгу добавлена запись: ', contact_str, '\n')    
    return    

# Главное меню
def main():
    menu = ''
    while menu != 'q':
        print('Какое действие вы хотите выполнить ?')
        print('1 - Найти данные в справочнике')
        print('2 - Добавить данные в справочник')
        print('3 - Удалить данные из справочника')
        print('4 - Вывести весь справочник')
        print('q - Выйти из программы')
        print(' ')
        menu = (input('Введите идентификатор - '))
        print(' ')
        if menu == '1':
            print(menu)
            #search_menu()
        elif menu == '2':
            first_name = input('Фамилия: ')
            second_name = input('Имя: ')
            pater_name =  input('Отчество: ')
            phone_number = input('Номер телефона :')
            contact = [first_name, second_name, pater_name, phone_number]
            add_new_contact(contact)
        elif menu == '3':
            print(menu)
        elif menu == '4': 
            print(menu)       
            #entire_directory()
        elif menu == 'q':
            break     
        else:
            print("Данной команды нет, введите другую")    
            print(' ')
        
main()