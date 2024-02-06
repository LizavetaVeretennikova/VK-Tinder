from urllib.parse import urlencode

# ID приложения VK
APP_ID = '51849990'
# базовая ссылка из документации VK_API
OAUTH_BASE_URL = 'https://oauth.vk.com/authorize'
# Параметры
params = {
    # обязательные параметры:
    #
    'client_id': APP_ID,
    # ссылка куда пользователь попадает после авторизации
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    # указывает тип отображения страницы авторизации- форма авторизации в отдельном окне;
    'display': 'page',
    'scope': 'photos',
    'response_type': 'token'
}

oauth_url = f'{OAUTH_BASE_URL}?{urlencode(params)}'
print(oauth_url)

