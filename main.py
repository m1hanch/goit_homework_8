import datetime
from datetime import datetime, timedelta

#Прикладовий словник
users = [{'name': 'Andrew', 'birthday': '2000-07-13'}, {'name': 'Alina', 'birthday': '2002-07-01'},
         {'name': 'Bogdan', 'birthday': '2001-07-15'}, {'name': 'Maria', 'birthday': '2003-07-14'},
         {'name': 'Dmytro', 'birthday': '1999-07-16'}, {'name': 'Anna', 'birthday': '2004-07-10'},
         {'name': 'Danylo', 'birthday': '2003-07-13'}, {'name': 'Kateryna', 'birthday': '2004-07-08'},
         {'name': 'Olga', 'birthday': '2004-07-11'}]

def get_birthdays_per_week(users: list)->None:

    #словник у якому будуть зберігатися імена людей, яких треба привітати для кожного дня
    res_dict = {'Monday':'','Tuesday':'','Wednesday':'','Thursday':'','Friday':'','Saturday':'','Sunday':''}
    #допоміжний список для перетворення цифри у назву тижна 0 -> Понеділок
    weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #Визначання поточної дати
    today = datetime.now().date()
    #today = datetime(year=2023, month=7, day=10)
    next_monday=''

    for user in users:
        #перетворення дня народження у datetime
        bday = user['birthday']
        bday = str(datetime.now().year) + bday[4:]
        bday = datetime.strptime(bday, '%Y-%m-%d')

        #Перевірка дня народження на минулих вихідних, якщо сьогодні понеділок
        if today.weekday() == 0 and today-timedelta(days=2) <= bday.date() < today:
            if res_dict['Monday']=='':
                res_dict.update({'Monday':res_dict['Monday']+user['name']})
            else:
                res_dict.update({'Monday': res_dict['Monday'] + ', ' + user['name']})

        #Якщо день народження знаходиться у діапазоні 1 тижня від сьогоднішньої дати, то додаємо до словника
        if today <= bday.date() <= today + timedelta(weeks=1):
            day = weekday[bday.weekday()]
            if res_dict[day]=='':
                res_dict.update({day: res_dict[day]+ user['name']})
            else:
                res_dict.update({day:res_dict[day]+", "+user['name']})
    #Додатково створє список людей, яких потрібно привітати у наступний понеділок, якщо ДН було на вихідних
    if res_dict['Sunday'] != '':
        next_monday+=res_dict['Sunday']+', '
    if res_dict['Saturday']!='':
        next_monday+=res_dict['Saturday']+', '
    next_monday = next_monday[:-2]

    #Виведення імен для кожного дня від Понеділка до П'ятниці
    for day,names in res_dict.items():
        if day!='Saturday' and day!='Sunday':
            print(day,names)

    #Виведення імен для наступного понеділка
    print("Next monday "+next_monday)


if __name__=='__main__':
    get_birthdays_per_week(users)