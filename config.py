from dotenv import load_dotenv
import os

load_dotenv()
# Secret tokens
VK_API_VERSION = os.getenv('VK_API_VERSION')
VK_LOGIN = os.getenv('VK_LOGIN')
VK_TOKEN = os.getenv('VK_ACCESS_TOKEN')
VK_APP_ID = os.getenv('VK_APP_ID')
TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
FB_ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN')

vk_auth_link = os.getenv('VK_OAUTH_LINK')

# User settings:
VK_GROUP_ID = 181016321
VK_ALBUM_ID = 262494951

TG_CHANEL = '@python_auto_post'

FB_GROUP_ID = '4062480697102376'

if __name__ == '__main__':
    print(vk_auth_link)