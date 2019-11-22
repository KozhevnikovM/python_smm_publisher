import vk_api
from config import VK_API_VERSION, VK_LOGIN, VK_TOKEN, VK_APP_ID


def upload_photo(filepath, album_id, group_id):
    vk_session = vk_api.VkApi(VK_LOGIN, token=VK_TOKEN)
    uploader = vk_api.VkUpload(vk_session)
    photo = uploader.photo(filepath, album_id=album_id, group_id=group_id)
    vk_photo_url = f'photo{photo[0]["owner_id"]}_{photo[0]["id"]}'
    return vk_photo_url


def vk_post(album_id, message=None, attachments=None, group_id=None, from_group=1):
    vk_session = vk_api.VkApi(VK_LOGIN, token=VK_TOKEN, api_version=VK_API_VERSION, app_id=VK_APP_ID)
    vk = vk_session.get_api()
    photo_url = upload_photo(attachments, album_id, group_id) if attachments else None
    vk.wall.post(message=message, attachments=photo_url, owner_id=-group_id, from_group=from_group)


if __name__ == '__main__':
    pass