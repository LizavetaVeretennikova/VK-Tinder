from vk_api.utils import get_random_id
def write_message(vk_session, user_id, message):
    """Функция для отправки сообщения"""
    # инициализируем отправку сообщений
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})

def send_message(peer_id, message, attachments, vk):
    """Функция отправки сообщения с вложениями"""
    vk.messages.send(user_id=peer_id, message=message, attachment=','.join(attachments), random_id=get_random_id())