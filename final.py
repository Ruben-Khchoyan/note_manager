

infor = {'username':input("Введите Ваше имя: "),
         'note':input("Введите заметку: "),
         'status':input("Введите статус заметки: "),
         'created_date':input("Введите дату создания заметки: "),
         'issue_date':input("Введите дату истечения заметки: "),
         'title_1':input("Введите заголовок 1: "),
         'title_2':input("Введите заголовок 2: "),
         'title_3':input("Введите заголовок 3: ")
         }

print("Имя пользователя:", infor['username'])
print("Описание заметки:", infor['note'])
print("Статус заметки:", infor['status'])
print("Дата создания заметки:", infor['created_date'])
print("Дата истечения заметки:", infor['issue_date'])
print("Заголовок 1:", infor['title_1'])
print("Заголовок 2:", infor['title_2'])
print("Заголовок 3:", infor['title_3'])