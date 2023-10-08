# Задача №49. Решение в группах Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

from csv import DictWriter, DictReader
from os.path import exists


def edit_record(num_e):
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
        print(num_e, res[num_e])
        print('Введите новые данные контакта:')
        obj = get_info()
        obj1 = {'Фамилия': obj[0], 'Имя': obj[1], 'Номер': obj[2]}
        res.pop(num_e)
        res.insert(num_e, obj1)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        for el in res:
            f_n_writer.writerow(el)


def delete_record(num_d):
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        res.pop(num_d)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        for el in res:
            f_n_writer.writerow(el)


def search_info(file_name):
    l_name = input('Введите фамилию: ')
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_info = list(f_n_reader)
        count = 0
        position_record = []
        for i in range(len(phone_info)):
            for k, v in phone_info[i].items():
                if v == l_name:
                    print(i, phone_info[i])
                    count += 1
                    position_record.append(i)
    if count == 0:
        print('По вашему запросу ничего не найдено.')
        print()


def get_info():
    info = []
    # first_name = 'Ivan'
    # last_name = 'Ivanov'
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    info.append(last_name)
    info.append(first_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('Неправильный номер')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    info.append(phone_number)
    return info


def create_file():
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        # data.write('Фамилия;Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()


def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        for el in res:
            f_n_writer.writerow(el)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def record_info(info):
    lst = get_info()
    write_file(lst)


def main():
    while True:
        command = input('Введите команду:\n q - выход\n r - прочитать справочник\n w - добавить контакт\n'
                        ' s - поиск контакта\n d - удалить контакт\n e - изменить контакт\n')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            rst = read_file('phone.csv')
            for i in range(len(rst)):
                print(i, end=" ")
                for k, v in rst[i].items():
                    print(k + ': ', v, end=' ')
                print()
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info('phone.csv')
        elif command == 's':
            search_info('phone.csv')
        elif command == 'd':
            num_d = int(input('Введите номер удаляемой записи: '))
            delete_record(num_d)
        elif command == 'e':
            num_e = int(input('Введите номер редактируемой записи: '))
            edit_record(num_e)


main()
