from config import FB_ACCESS_TOKEN
import requests

API_URL = 'https://graph.facebook.com/v5.0'


def fb_post_text_only(group_id, message):
    url = f'{API_URL}/{group_id}/feed'
    data = {
        'access_token': FB_ACCESS_TOKEN,
        'message': message
    }
    return requests.post(url, data=data).content


def fb_post(group_id, attachment=None, caption=None):
    if not attachment:
        return fb_post_text_only(group_id, caption)
    url = f'{API_URL}/{group_id}/photos'
    files = {'upload_file': open(attachment, 'rb')}
    data = {
        'access_token': FB_ACCESS_TOKEN,
        'caption': caption
    }
    return requests.post(url, data=data, files=files).content


if __name__ == '__main__':
    pass