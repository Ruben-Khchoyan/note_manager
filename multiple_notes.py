# Импорт модуля datetime
from datetime import datetime as dt


# Список notes для хранения всех заметок
notes = []


print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')


# Функция для проверки соответствия введенный даты требуемым форматам
def check(per):
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y'):
        try:
            return dt.strptime(per, fmt)
        except ValueError:
            pass
    else:
        print('Введен неверный формат данных!')
        return 0


# Функция для создания заметок
def note():
    # Цикл для введения имени пользователя и проверки чтобы не была пустая строка
    while True:
        user_name = input("Введите имя пользователя: ")
        if user_name.strip() == '':
            continue
        break


    # Цикл для введения заголовка заметки и проверки чтобы не была пустая строка
    while True:
        title = input("Введите заголовок заметки: ")
        if title.strip() == '':
            continue
        break


    # Цикл для введения описания заметки и проверки чтобы не была пустая строка
    while True:
        content = input("Введите описание заметки: ")
        if content.strip() == '':
            continue
        break


    # Цикл для введения статуса заметки по числам (так быстрее, чем писать статус).
    # Так же есть проверка чтобы введеное число было в диапазоне от 1 до 3.
    while True:
        num_status = input("Введите номер статуса заметки (1 -> новая; 2 -> в процессе; 3 -> выполнено): ")
        lst_status = ['новая', 'в процессе', 'выполнено']
        if num_status.isdigit(): # Проверка что введено число
            if int(num_status) in range(1, len(lst_status)+1):
                status = lst_status[int(num_status)-1].lower()
                break
        print('Статус заметки введен не правильно!')
        continue


    # Цикл для ввода даты создания и дедлайна заметки.
    # Через if и функцию check проверятся правильность введения формата данных
    while True:
        print(f'Форматы ввода дат:\n- ГГГГ-ММ-ДД\n- ДД.ММ.ГГГГ\n- ДД/ММ/ГГГГ\n- ДД-ММ-ГГГГ')


        # Цикл проверки формата ввденной даты создания
        created_date = input("Введите дату создания заметки: ")
        if check(created_date) != 0:
            created_date = check(created_date)
        else:
            continue


        # Цикл проверки формата ввденной даты истечения
        issue_date = input("Введите дату истечения заметки: ")
        if check(issue_date) != 0:
            issue_date = check(issue_date)
        else:
            continue


        # Цикл проверки, чтобы дата истечения была позже даты дедлайна
        if issue_date < created_date:
            print("Дата дедлайна не может быть раньше даты создания заметки!")
            continue
        else:
            break


    # Результат вывода фцнкции словарь со всеми данными заметок
    return {'Имя пользователя':user_name,
            'Заголовок':title,
            'Описание':content,
            'Статус':status,
            'Дата создания':created_date.strftime('%d-%m-%Y'),
            'Дедлайн':issue_date.strftime('%d-%m-%Y')}


# Добавление первой заметки с индексом 1
notes.append(note())


# Цикл для создания дополнительных заметок. В случае отказа цикл завершается.
while True:
    create_new_note = input("Хотите добавить ещё одну заметку? (да/нет): ")
    if create_new_note.strip().lower() not in ['да', 'нет']:
        print('\nНе корректный ответ!\n')
    elif create_new_note.strip().lower() == 'да':
        notes.append(note())
        continue
    elif create_new_note.strip().lower() == 'нет':
        break


# Вывод всех заметок из списка notes в удобном формате.
print("\nСписок заметок: ")
for i in range(len(notes)):
    print(i + 1, end=' ')
    for k, v in notes[i].items():
        print(f' {k}: {v}')
    print()