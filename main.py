import os
from vk import vk_post
from tg import tg_send_to_chanel
from facebook import fb_post
from config import VK_GROUP_ID, VK_ALBUM_ID, TG_CHANEL, FB_GROUP_ID


if __name__ == '__main__':
    filename = input('Please, enter filename or press enter to skip: ')
    message = input('And now write your message or press enter to skip: ')
    photos_dir = os.path.join(os.path.dirname(__file__), 'uploads', 'photos')
    attachment = os.path.join(photos_dir, filename) if filename else None
    os.makedirs(photos_dir, exist_ok=True)

    if not message and not filename:
        exit('No message to post')

    if attachment:
        if not os.path.exists(attachment):
            exit('Wrong attachment name or file doesn\'t exist')

    vk_post(VK_ALBUM_ID, message=message, attachments=attachment, group_id=VK_GROUP_ID)
    tg_send_to_chanel(TG_CHANEL, message, attachment)
    fb_post(group_id=FB_GROUP_ID, attachment=attachment, caption=message)
