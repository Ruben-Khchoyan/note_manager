# Импорт модуля datetime
from datetime import datetime as dt


date_user = dt.today()


# Отображение текущего дня и вывод ифнормации
print(f'Текущая дата: {date_user.strftime("%d-%m-%Y")}')
# Информация о поддерживающих форматах ввода данных
print(f'Форматы ввода даты:\n- ГГГГ-ММ-ДД\n- ДД.ММ.ГГГГ\n- ДД/ММ/ГГГГ\n- ДД-ММ-ГГГГ')


# Функция для опредления соответсвия введенных данных соответсвующему формату циклом for
def check(per):
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y'):
        try:
            return dt.strptime(per, fmt)
        except ValueError:
            pass
    else:
        print('Введен неверный формат данных!')
        return 0


# Цикл while для ввода даты дедлайна. В случае ошибки выводиться 'Введен неверный формат данных!' и требование заново
# ввести дату дедлайна
while True:
    issue_date_str = input("Введите дату дедлайна в нужном формате: ")
    if check(issue_date_str) != 0:
        issue_date = check(issue_date_str)
        break
    else:
        continue


# Расчет количества дней до дедлайна или прошедших после дедлайна
date_deadline = abs(issue_date - date_user)


# Цикл if для вывода сответствующей информации и сроках дедлайна
if issue_date > date_user:
    print('Количество дней до дедлайна:', date_deadline.days)
elif issue_date.date() == date_user.date():
    print('Дедлайн сегодня!')
elif date_deadline.days % 10 == 1:
    print(f'Внимание! Дедлайн истек {date_deadline.days} день назад.')
elif date_deadline.days % 10 in [2, 3, 4]:
    print(f'Внимание! Дедлайн истек {date_deadline.days} дня назад.')
else:
    print(f'Внимание! Дедлайн истек {date_deadline.days} дней назад.')

