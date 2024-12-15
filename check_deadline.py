from datetime import datetime as dt

date_user = dt.today()
issue_date = dt.strptime('26.06.2026', '%d.%m.%Y')
date_deadline = abs(issue_date - date_user)

if issue_date > date_user:
    print('Количество дней до дедлайна:', date_deadline.days)
else:
    print('Дедлайн прошел!')
