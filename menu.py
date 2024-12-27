
from colorama import Fore

from Project1.note_manager.create_note_function import create_note
from Project1.note_manager.display_notes_function import display_notes
from Project1.note_manager.delete_note import del_note
from Project1.note_manager.search_notes_function import search_notes
from Project1.note_manager.update_note_function import update_note


# Список с несколькими заметками
lst_notes = [{'username': 'Игорь',
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


# # Список с одной заметкой
# lst_notes = [{'username': 'Алексей',
#               'title': 'Список дел',
#               'content': 'Купить продукты на неделю',
#               'status': 'новая',
#               'created_date': '18-11-2024',
#               'issue_date': '19-11-2024'}]


# # Пустой список заметок
# lst_notes = []


def output_notes(notes):
    import termtables as tt
    type_info = ['№', 'Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн']
    for_display = []
    for i, v in enumerate(notes):
        for_display.append([i + 1] + list(v.values()))
    print(tt.to_string(for_display, header=type_info))  # Вывод таблицы с полной информацией


if len(lst_notes) >= 1:
    output_notes(lst_notes)
else:
    print("Список заметок пуст!")


while True:
    print(Fore.GREEN + '\nМеню действий:',
        Fore.YELLOW + '\n1. Создать новую заметку',
        Fore.BLUE + '\n2. Показать все заметки',
        Fore.MAGENTA + '\n3. Обновить заметку',
        Fore.RED + '\n4. Удалить заметку',
        Fore.CYAN + '\n5. Найти заметки',
        Fore.BLUE + '\n6. Выйти из программы')
    solve = input(Fore.GREEN + '\nНапишите номер одного из действий: ').strip()


    if solve == '1':
        lst_notes.append(create_note())
        print("Заметка создана!")
        output_notes(lst_notes)
        continue


    elif solve == '2':
        display_notes(lst_notes)
        continue


    elif solve == '3':
        # Цикл для изменения заметок вызовом функции update_note. В случае отказа цикл завершается.
        while len(lst_notes) >= 1:
            question = input("\nЖелаете изменить данные заметки? (да/нет): ")
            if question.strip().lower() not in ['да',
                                                'нет']:  # Условный оператор выводящий замечание если не првильно дан ответ на вопрос
                print('\nНе корректный ответ!')
            elif question.strip().lower() == 'да':
                output_notes(lst_notes)
                note_num = input('\nВыберите номер заметки, которую хотите изменить: ').strip()
                if note_num.isdigit() and int(note_num) in range(
                        len(lst_notes) + 1):  # Проверка введеного номера заметки в списке заметок
                    update_note(lst_notes[int(note_num) - 1])
                else:  # Выводит замечение если заметки с таким номером не существует
                    print("\nВведен неверный номер заметки!")
            elif question.strip().lower() == 'нет':  # Если измений заметкам не требуется или больше изменений не требуется, то выводиться актуальный список заметок
                output_notes(lst_notes)
                break
            output_notes(lst_notes)
        else:
            print("Список заметок пуст!")
        continue


    elif solve == '4':
        del_note(lst_notes)
        continue


    elif solve == '5':
        search_notes(lst_notes)
        continue


    elif solve == '6':
        break


    else:
        print("Неверный выбор. Пожалуйста, выберите действие из меню.")
        continue
print('Программа завершена. Спасибо за использование!')

