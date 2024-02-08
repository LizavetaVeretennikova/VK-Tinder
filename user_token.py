
GET_TOKEN_COMMAND = "/get_token"

def handle_token_command(event, vk):
    """Отправляет пользователю сообщение с просьбой предоставить его токен."""
    message = "Пожалуйста, отправьте свой токен в следующем сообщении."
    vk.messages.send(user_id=event.user_id, message=message, random_id=0)
