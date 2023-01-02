from datetime import datetime


def get_birthdays_per_week(users, range_of_days=7):

    """Отримати дні народження на наступний тиждень"""

    current_date = datetime.now()
    for dict in users:
        user_name = dict.get('name')
        user_date = dict.get('birthday')
        user_date = user_date.replace(year = current_date.year)
        day_of_week = user_date.weekday()
        delta_days = user_date - current_date
        
        if 0 < delta_days.days <= range_of_days:
            # print(f"{user_date.strftime('%d, %A')}: {user_name}") виведення з числом місяця
            if day_of_week == 5 or day_of_week == 6:
                print(f"Monday: {user_name}")
            else:    
                print(f"{user_date.strftime('%A')}: {user_name}") # виведення дня тижня без числа
        elif 0 < delta_days.days > range_of_days:
            continue
        else:
            user_date = user_date.replace(year=user_date.year + 1)
            delta_days = user_date - current_date
            if 0 < delta_days.days <= range_of_days:
                # print(f"{user_date.strftime('%d, %A')}: {user_name}") виведення з числом місяця
                if day_of_week == 5 or day_of_week == 6:
                    print(f"Monday: {user_name}")
                else:    
                    print(f"{user_date.strftime('%A')}: {user_name}") # виведення дня тижня без числа
            elif 0 < delta_days.days > range_of_days:
                continue
           

# Список словників користувачів з датами народження
users = [
        {'name': 'Anastasiia',
        'birthday': datetime(year=2002, month=3, day=26)},
        {'name': 'Anna',
        'birthday': datetime(year=2000, month=1, day=11)},
        {'name': 'Inna',
        'birthday': datetime(year=2001, month=10, day=13)},
        {'name': 'Ivan',
        'birthday': datetime(year=1999, month=7, day=8)},
        {'name': 'Jeka',
        'birthday': datetime(year=1998, month=12, day=31)},
        {'name': 'Sanya',
        'birthday': datetime(year=1980, month=1, day=28)},
        ]

get_birthdays_per_week(users, range_of_days=30)


# if __name__ == __main__:
#     get_birthdays_per_week(users)
    


# реалізувати словник зі списками щоб прінтувати словник а не построчно
# Посортувати дні тижня по порядку