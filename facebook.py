from config import FB_ACCESS_TOKEN
import requests
from requests.exceptions import HTTPError

API_URL = 'https://graph.facebook.com/v5.0'


def fb_post_text_only(group_id, message):
    url = f'{API_URL}/{group_id}/feed'
    data = {
        'access_token': FB_ACCESS_TOKEN,
        'message': message
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.content


def fb_post(group_id, attachment=None, caption=None):
    if not attachment:
        return fb_post_text_only(group_id, caption)
    url = f'{API_URL}/{group_id}/photos'
    data = {
        'access_token': FB_ACCESS_TOKEN,
        'caption': caption
    }
    with open(attachment, 'rb') as file:
        files = {'upload_file': file}
        response = requests.post(url, data=data, files=files)
    response.raise_for_status()
    return response.content


if __name__ == '__main__':
    pass