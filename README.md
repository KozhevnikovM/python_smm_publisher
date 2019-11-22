# Automatic publisher for Vkontakte, Facebook and Telegram
This script publishes your message and photo to 3 social networks:
* VK
* Facebook
* Telegram

## Used modules:
* Python telegram bot: https://github.com/python-telegram-bot/python-telegram-bot
* VK Api: https://github.com/python273/vk_api

## System requirements:
python3.5+

## How to install:
You're need:
* vk standalone application, 
* telegram bot with admin access to your chanel,
* facebook application with publish_to_groups access.

### Install requirements:

```bash
$ pip install -r requirements.txt

```
### Setup your credentials:
Rename dotenv.sample to .env and specify it with your credentials

* VK_API_VERSION - current vk api version
* VK_APP_ID - your standalone application id. To find it, click edit on your application page
* VK_ACCESS_TOKEN - your vk access token.
* VK_LOGIN - login for user with admin group access
* TG_BOT_TOKEN - your telegram bot token
* FB_ACCESS_TOKEN - your facebook access token

## How to run
Place your photo in 'uploads/photos'
run:
```bash
$ python main.py
```
Enter filename and message:
```bash
$ python main.py
Please, enter filename or press enter to skip: girl.png
And now write your message or press enter to skip: hi again

```

## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.

