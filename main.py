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
                # print(f"Monday: {user_name}")
                near_birthdays['name0'].append(user_name)
            else:    
                # print(f"{user_date.strftime('%A')}: {user_name}") # виведення дня тижня без числа
                near_birthdays[f"name{day_of_week}"].append(user_name)
        elif 0 < delta_days.days > range_of_days:
            continue
        else:
            user_date = user_date.replace(year=user_date.year + 1)
            delta_days = user_date - current_date
            if 0 < delta_days.days <= range_of_days:
                # print(f"{user_date.strftime('%d, %A')}: {user_name}") виведення з числом місяця
                if day_of_week == 5 or day_of_week == 6:
                    # near_birthdays.append({'day': "Monday", near_birthdays['name'].append()}) 
                    near_birthdays['name0'].append(user_name)
                       
                else:    
                    # named_day_of_week = user_date.strftime('%A')  виведення дня тижня без числа
                    near_birthdays[f"name{day_of_week}"].append(user_name)
            elif 0 < delta_days.days > range_of_days:
                continue

                # вивід фінальний
    for i in range(5):
        if near_birthdays[f"name{i}"] == []:
            continue
        else:
            print(near_birthdays[f"day{i}"]+':', ", ".join(near_birthdays[f"name{i}"]))
    

           

# Список словників користувачів з датами народження
users = [
        {'name': 'Anastasiia',
        'birthday': datetime(year=2002, month=3, day=26)},
        {'name': 'Anna',
        'birthday': datetime(year=2000, month=1, day=9)},
        {'name': 'Inna',
        'birthday': datetime(year=2001, month=1, day=13)},
        {'name': 'Ivan',
        'birthday': datetime(year=1999, month=1, day=8)},
        {'name': 'Jeka',
        'birthday': datetime(year=1998, month=12, day=31)},
        {'name': 'Sanya',
        'birthday': datetime(year=1980, month=1, day=28)},
        ]

near_birthdays = {
                'day0': 'Monday', 'name0': [],
                'day1': 'Tuesday', 'name1': [],
                'day2': 'Wednesday', 'name2': [],
                'day3': 'Thurthday', 'name3': [],
                'day4': 'Friday', 'name4': []
                }

get_birthdays_per_week(users, range_of_days=30)


if __name__ == '__main__':
    get_birthdays_per_week(users)
    