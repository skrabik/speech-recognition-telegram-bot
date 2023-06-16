#
#
#
import requests

class VoiceMessage:
    def __init__(self, update):
        self.message_id = update.json()['result'][0]['message']['message_id']
        self.chat_id = update.json()['result'][0]['message']['chat']['id']
        self.file_id = update.json()['result'][0]['message']['voice']['file_id']

    def get_download_link(self, BOT_TOKEN):
        path = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={self.file_id}')
        file_path = path.json()['result']['file_path']
        download_link = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}'
        return download_link



