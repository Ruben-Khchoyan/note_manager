
# # Список с заметками в виде словаря
# lst_notes = [{'username': 'Алексей',
#               'title': 'Список дел',
#               'content': 'Купить продукты на неделю',
#               'status': 'новая',
#               'created_date': '18-11-2024',
#               'issue_date': '19-11-2024'},
#
#              {'username': 'Петя',
#               'title': 'Список овощей',
#               'content': 'Купить грибы и помидоры',
#               'status': 'в процессе',
#               'created_date': '01-11-2024',
#               'issue_date': '30-11-2024'},
#
#              {'username': 'Илья',
#               'title': 'Починить машину',
#               'content': 'Купить клапана и свечи',
#               'status': 'новая',
#               'created_date': '04-11-2024',
#               'issue_date': '20-11-2024'}]


# Функция вывод заметок из списка заметок.
def output_notes(notes):
    import termtables as tt
    type_info = ['№', 'Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн']
    for_display = []
    for i, v in enumerate(notes):
        for_display.append([i + 1] + list(v.values()))
    print(tt.to_string(for_display, header=type_info))  # Вывод таблицы с полной информацией


# # Вывод заметок первоначальный
# output_notes(lst_notes)


# Начало функции изменения заметок
def update_note(note):

    # Импорт модуля datetime
    from datetime import datetime as dt

    import termtables as tt

    type_info = ['№', 'Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн']

    # Функция для проверки соответствия введенный даты требуемым форматам
    def data_check(per):
        for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y'):
            try:
                return dt.strptime(per, fmt)
            except ValueError:
                pass
        else:
            return 0
    # Конец функции проверки введенной даты


    while True:
        # Выбор типа данных для изменения
        change_type_data = input(f'\nКакие данные вы хотите обновить? (username, title, content, status, issue_date, (не хотите менять - нажмите Enter): ').strip().lower()
        # Условный оператор для изменения времени дедлайна
        if change_type_data == 'issue_date':
            while True:
                print(f'\n{change_type_data} : {note[change_type_data]}') # Вывод текущей даты дедлайна
                print(f'\nФорматы ввода дат:\n- ГГГГ-ММ-ДД\n- ДД.ММ.ГГГГ\n- ДД/ММ/ГГГГ\n- ДД-ММ-ГГГГ') # Поддерживаемые форматы ввода дат
                change_time = input(f'Введите новое значение для {change_type_data}: ') # Ввод новой даты
                if data_check(change_time) != 0 and data_check(change_time) < data_check(note['created_date']): # Проверка если дата нужного формат, но раньше даты создания то выводит замечание
                    print("\nДата дедлайна не может быть раньше даты создания заметки!")
                elif data_check(change_time) != 0: # Проверка если дата нужного формата, то данные меняются и конец цикла while
                    note[change_type_data] = dt.strftime(data_check(change_time), '%d-%m-%Y')
                    break
                elif change_time == '': # Если пустая строка то данные не меняются и конец цикла while
                    print('\nДанные не изменены!')
                    break
                else:
                    print('\nВведен неверный формат данных!') # Вывод если формат данных неверный

        elif change_type_data in ['username', 'title', 'content', 'status']: # Условный оператор для изменения других данных заметок
            while True:
                print(f'\n{change_type_data} : {note[change_type_data]}')
                change_data = input(f'\nВведите новое значение для {change_type_data}: ').strip()
                if change_data != '': # Если не пустая строка то данные меняются и конец цикла while
                    note[change_type_data] = change_data
                    break
                else: # Если пустая строка то данные не меняются и конец цикла while
                    print('\nДанные не изменены!')
                    break

        elif change_type_data == '': # Если не введено наименование данных заметки то данные не меняются и конец цикла while
            break

        else: # Если не правильно введено наименование данных заметки
            print('\nНе корректный ответ!')

    print(f'\nЗаметка обновлена:')
    print(tt.to_string([list(note.values())], header=type_info[1:]))
# Конец функции изменения заметок



# # Цикл для изменения заметок вызовом функции update_note. В случае отказа цикл завершается.
# while True:
#     question = input("\nЖелаете изменить данные заметки? (да/нет): ")
#     if question.strip().lower() not in ['да',
#                                         'нет']:  # Условный оператор выводящий замечание если не првильно дан ответ на вопрос
#         print('\nНе корректный ответ!')
#     elif question.strip().lower() == 'да':
#         output_notes(lst_notes)
#         note_num = input('\nВыберите номер заметки, которую хотите изменить: ').strip()
#         if note_num.isdigit() and int(note_num) in range(
#                 len(lst_notes) + 1):  # Проверка введеного номера заметки в списке заметок
#             update_note(lst_notes[int(note_num) - 1])
#         else:  # Выводит замечение если заметки с таким номером не существует
#             print("\nВведен неверный номер заметки!")
#     elif question.strip().lower() == 'нет':  # Если измений заметкам не требуется или больше изменений не требуется, то выводиться актуальный список заметок
#         output_notes(lst_notes)
#         break
# output_notes(lst_notes)
