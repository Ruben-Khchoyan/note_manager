
from datetime import datetime as dt

temp_issue_date = dt.strptime(input("Введите дату в формате ДД.ММ.ГГГГ: "), '%d.%m.%Y')
temp_created_date = dt.strptime(input("Введите дату в формате ДД.ММ.ГГГГ: "), '%d.%m.%Y')

print((str(temp_issue_date).split())[0][5:])
print((str(temp_created_date).split())[0][5:])