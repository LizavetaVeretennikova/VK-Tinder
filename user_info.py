
from datetime import datetime, timedelta

def change_of_date(date_string, years):
    """Функция предназначена для прибавления или вычета лет к дате """
    date_format = '%d.%m.%Y'
    date_obj = datetime.strptime(date_string, date_format)
    new_date_obj = date_obj + timedelta(days=365*years)
    return new_date_obj.strftime(date_format)

def get_user_info(user_id, vk):
    """Функция предназначена находить данные у пользователя
     и добавлять их в словарь match_criteria"""
    user_info = vk.users.get(user_ids=user_id, fields='sex,bdate,city')[0]
    age = user_info['bdate']  # возраст
    city = user_info['city']['title']  # город
    gender = user_info['sex']  # пол
    if gender == 1:  # если девочка
        match_criteria = {
            'age': {
                'min': age,
                'max': change_of_date(age,   5)
            },
            'gender': gender,
            'city': city
        }
        result = match_criteria
    elif gender == 2:  # если мальчик
        match_criteria = {
            'age': {
                'min': change_of_date(age,  -5),
                'max': age
            },
            'gender': gender,
            'city': city
        }
        result = match_criteria
    else:
        match_criteria = 'что то пошло не так в функции get_user_info'
        return match_criteria
    return result


