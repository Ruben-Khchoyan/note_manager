

# Список с несколькими заметками
lst_notes_1 = [{'username': 'Алексей',
              'title': 'Список дел',
              'content': 'Купить продукты на неделю',
              'status': 'новая',
              'created_date': '18-11-2024',
              'issue_date': '19-11-2024'},

             {'username': 'Петя',
              'title': 'Список овощей',
              'content': 'Купить грибы и помидоры',
              'status': 'в процессе',
              'created_date': '01-11-2024',
              'issue_date': '30-11-2024'},

             {'username': 'Илья',
              'title': 'Починить машину',
              'content': 'Купить клапана и свечи',
              'status': 'новая',
              'created_date': '04-11-2024',
              'issue_date': '20-11-2024'}]


# Список с одной заметкой
lst_notes_2 = [{'username': 'Алексей',
              'title': 'Список дел',
              'content': 'Купить продукты на неделю',
              'status': 'новая',
              'created_date': '18-11-2024',
              'issue_date': '19-11-2024'}]


# Пустой список заметок
lst_notes_3 = []


# Начало функции вывода заметок
def display_notes(notes):

    # Импорт модуля termtables (просто нравиться формат вывода)
    import termtables as tt


    # Цикл для определения уровня детализации вывода информации.
    # Если список пуст, то выводиться соответсвующее замечание
    while True:

        if len(notes) == 0:
            print('\nУ вас нет сохранённых заметок.')
            break


        create_new_note = input("1 -> вывести только заголовки заметок\n"
                                "2 -> вывести полность данные\n"
                                "Выберите уровень детализации: ")


        if create_new_note.strip().lower() == '1':

            # Список с заголовками таблицы вывода
            type_info = ['№', 'Заголовок']

            # Если количество заметок в списке больше 1
            if len(notes) > 1:
                print('Список заголовков заметок:')
                lst_dict_titles = [] # Список с заголовками
                for i in range(len(notes)): # Цикл вывода нужных значений
                    lst_dict_titles.append([i + 1] + [notes[i].get('title')])

                print(tt.to_string(lst_dict_titles, header=type_info)) # Вывод таблицы с заголовками
                break

            # Если заметка одна
            elif len(notes) == 1:
                print('Заголовок заметки:')
                lst_dict_values = [1] + [notes[0].get('title')] # Вывод нужного заголовка
                print(tt.to_string([lst_dict_values], header=type_info)) # Вывод таблицы с заголовком
                break

        elif create_new_note.strip().lower() == '2':

            # Список с заголовками таблицы вывода
            type_info = ['№', 'Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн']

            # Если количество заметок в списке больше 1
            if len(notes) > 1:
                print('Список заметок:')
                lst_dict_values = [] # Список всех значений
                for i in range(len(notes)): # Цикл вывода списков со всеми значениями
                    lst_dict_values.append([i + 1] + list(notes[i].values()))

                print(tt.to_string(lst_dict_values, header=type_info)) # Вывод таблицы с полной информацией
                break

            # Если заметка одна
            elif len(notes) == 1:
                print('Заметка:')
                lst_dict_values = [1] + list(notes[0].values()) # Список всех значений заметки
                print(tt.to_string([lst_dict_values], header=type_info)) # Вывод таблицы с полной информацией
                break

        else: # Если не правильный ответ то цикл while повторяется
            print('\nНе корректный ответ!\n')
# Конец функции вывода заметок


# Вызов функции для вывода списка с несколькими заметками
display_notes(lst_notes_1)
print()


# Вызов функции для вывода одной заметки из списка
display_notes(lst_notes_2)
print()


# Вызов функции для пустого списка заметок
display_notes(lst_notes_3)
