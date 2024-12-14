
from datetime import datetime as dt

infor = {'username':input("Введите Ваше имя: "),
         'note':input("Введите заметку: "),
         'status':input("Введите статус заметки: "),
         'created_date':dt.strptime(input("Введите дату создания в формате ДД.ММ.ГГГГ: "), '%d.%m.%Y'),
         'issue_date':dt.strptime(input("Введите дату в формате ДД.ММ.ГГГГ: "), '%d.%m.%Y'),
         'title':[input("Введите заголовок 1: "), input("Введите заголовок 2: "), input("Введите заголовок 3: ")],
         }

print("Имя пользователя:", infor['username'])
print("Описание заметки:", infor['note'])
print("Статус заметки:", infor['status'])
print("Дата создания заметки:", (str(infor['created_date']).split())[0][5:])
print("Дата истечения заметки:", (str(infor['issue_date']).split())[0][5:])

for i in range(len(infor['title'])):
    print(f'Заголовок {i+1} - {infor['title'][i]}' )