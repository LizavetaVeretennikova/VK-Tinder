import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api_for_groups import Api

from params import TOKEN, GROUP_ID
from user_info import get_user_info
from write_message import write_message, send_message
from user_token import handle_token_command
# from find_potential import find_potential_matches
from top_three_photos import get_top_three_photos
# from send_msage import send_mess

# Создаем объект vk_session
vk_session = vk_api.VkApi(token=TOKEN)

# Инициализируем longpoll
longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()

GET_TOKEN_COMMAND = "/get_token"

# group_api = Api(TOKEN, GROUP_ID)



# Создаем цикл для постоянной связи с сервером
for event in longpoll.listen():
    # проверяем что event именно сообщение, а не например комментарий и что оно
    # адресовано нам(на случай если бота добавили в беседу) и что там только текст
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # получаемое сообщение
        received_message = event.text
        # отправитель id написавшего
        sender = event.user_id
        # устанавливаем критерии поиска исходя из критериев пользователя
        criteria = get_user_info(sender, vk)  #  potential_matches
        # Смотрим потенциальные совпадения и отправляйте информацию в чат.
        if event.text == GET_TOKEN_COMMAND:
            handle_token_command(event, vk)
            continue  # Пропустить дальнейшую обработку, поскольку мы обработали команду




        if received_message.lower() == 'привет':
            write_message(vk_session, sender, 'Добрый день!')
        elif received_message.lower() == 'пока':
            write_message(vk_session, sender, 'Доброй ночи!')
        else:
            write_message(vk_session, sender, 'Что?')

# Коля
# {'id': 23659472, 'city': {'id': 71, 'title': 'Кострома'}, 'sex': 2, 'first_name': 'Николай', 'last_name': 'Гусаров', 'can_access_closed': True, 'is_closed': False}
#                           Возраст                                   город            пол
# {'id': 23659472, 'bdate': '19.9.1985', 'city': {'id': 71, 'title': 'Кострома'}, 'sex': 2, 'first_name': 'Николай', 'last_name': 'Гусаров', 'can_access_closed': True, 'is_closed': False}
# Ваня
# {'id': 337900925, 'sex': 2, 'first_name': 'Иван', 'last_name': 'Будеев', 'can_access_closed': True, 'is_closed': False}
# Света
# {'id': 4951500, 'bdate': '3.7.1989', 'city': {'id': 71, 'title': 'Кострома'}, 'sex': 1, 'first_name': 'Светлана', 'last_name': 'Универ', 'can_access_closed': True, 'is_closed': True}
# 'sex': 1 девочка
# 'sex': 2 мальчик
