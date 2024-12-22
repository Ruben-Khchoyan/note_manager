
lst_notes = [{'Имя пользователя': 'Дима',
          'Заголовок': 'Распечатать диплом',
          'Описание': 'Купить бумагу для принтера',
          'Статус': 'новая',
          'Дата создания': '12-12-1212',
          'Дедлайн': '12-12-1255'},
         {'Имя пользователя': 'Ольга',
          'Заголовок': 'Сварить борщ',
          'Описание': 'Купить капусту и свеклу',
          'Статус': 'в процессе',
          'Дата создания': '12-12-1212',
          'Дедлайн': '12-12-1444'}]


# Функция для вывода текущих заметок
def output_notes(notes):
    if len(notes) == 1:
        print('Текущая заметка:')
        for i in range(len(notes)):
            for k, v in notes[i].items():
                print(f'{k}: {v}')
            print()
    elif len(notes) == 0:
        print('\nCписок заметок пуст!')
    else:
        print('Текущие заметки:')
        for i in range(len(notes)):
            for k, v in notes[i].items():
                print(f'{k}: {v}')
            print()
            # Конец функции


# Вывод текущих заметок при помощи функции output_notes
output_notes(lst_notes)


# Функция для удаления заметок note по ключевым словам word
def del_note(word, note):
    ind_del_note = [] # Список с индексами заметок которые требуется удалить
    len_before_remove = len(note) # Подсчет длины списка с заметками перед удалением
    # Цикл для прохождения по всем элементам списка с заметками
    for i in range(len(note)):
        # Условный оператор для проверки входимости ключевых слов в имя пользователя или заголовки
        if word.strip().lower() in note[i]['Имя пользователя'].lower() or word.strip().lower() in note[i][
            'Заголовок'].lower():
            for k, v in note[i].items():
                print(f'{k}: {v}')
            print()


            # Цикл для уточнения информации об удалении заметки.
            # Если да то номер индекса добавляется в список ind_del_note
            while True:
                solve = input("Вы уверены, что хотите удалить заметку? (да/нет): ").strip().lower()
                if solve not in ['да', 'нет']:
                    print('\nНе корректный ответ!\n')
                    continue
                elif solve == 'да':
                    ind_del_note.append(i)
                    break
                elif solve == 'нет':
                    print('Заметка не удалена!')
                    break


    # Цикл для удаления заметок по индексам из списка ind_del_note в обратном порядке чтобы не было ошибки
    for i in ind_del_note[::-1]:
        note.pop(i)
        print('\nЗаметка успешно удалена. ', end='')


    len_after_remove = len(note) # Подсчет длины списка с заметками после удаления
    # Условный оператор для сравнения длины списков до и после удаления.
    # Если длины одинаковые то заметок в списке не найдено по словам word
    if len_before_remove == len_after_remove:
        print('\nЗаметок с таким именем пользователя или заголовком не найдено или заметки не удалены.')
        # Конец функции


# Цикл для удаления заметок при желании удалить заметки и их наличии в списке
while True:
    if len(lst_notes) != 0:
        del_solve = input('Желаете удалить заметки? (да/нет): ')
        if del_solve not in ['да', 'нет']:
            print('\nНе корректный ответ!\n')
            continue
        elif del_solve == 'да':
            output_notes(lst_notes)
            note_word = input('Введите имя пользователя или заголовок для удаления заметки: ')
            del_note(note_word, lst_notes)
            continue
        elif del_solve == 'нет':
            break
    else:
        print("\nCписок заметок пуст.")
        break


# Вывод заметок после удаления
if len(lst_notes) == 1:
    print('\nОсталась одна заметка:')
    for i in range(len(lst_notes)):
        for k, v in lst_notes[i].items():
            print(f'{k}: {v}')
        print()
elif len(lst_notes) > 1:
    print('\nОстались следующие заметки:')
    for i in range(len(lst_notes)):
        for k, v in lst_notes[i].items():
            print(f'{k}: {v}')
        print()