from params import TOKEN
import vk_api

def vk_yandex(vk_id, yandex_token):

    # получаю массив объектов фотографий
    # token = ''  # token vk program
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    photos = vk.photos.get(owner_id=vk_id, album_id='profile', extended=1, count=10)
    print(photos)
