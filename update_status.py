
infor = {"status":"в процессе"}

lst_status =["выполнено", "в процессе", "отложено"]

print(f'Текущий статус заметки: "{infor.get("status")}"') # Отображение текущего статуса заметки

while True: # Цикл для ввода данных
    print('Статус заметки может быть:\n1. выполнено;\n2. в процессе;\n3. отложено.')
    d = input("Выберите значение или номер нового статус заметки: ")
    # Проверка что введенное зачение состоит из цифр и в нужном дипазоне.
    # Если да, то меняется статус и цикл завершается командой break
    if d.strip().isdigit() and int(d.strip()) in range(1, len(lst_status) + 1):
        infor["status"] = lst_status[int(d.strip()) - 1]
        print(f'Статус заметки успешно обновлён на: "{infor.get("status")}"')
        break
    elif d.strip() in lst_status: # Проверка что введенное зачение есть в списке статусов lst_status. Если да, то меняется статус и цикл завершается командой break
        infor["status"] = d
        print(f'Статус заметки успешно обновлён на: "{d}"')
        break
    else: # Если данные введены не корректно, то выводиться соответсвующая информация и командой continue возвращаемся в начало цикла и требуем заново ввести данные
        print('Введено некорректное значение!')
        continue
