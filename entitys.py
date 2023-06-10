#
#
#
import requests

# update = requests.get(f"https://api.telegram.org/bot6067696369:AAEVrzTDSJc3tW_Jb7jF89NjB6MCS6Q89k8/getUpdates")

class VoiceMessage:
    def __init__(self, update):
        self.message_id = update.json()['result'][0]['message']['message_id']
        self.from_id = update.json()['result'][0]['message']['from']['id']
        self.from_is_bot = update.json()['result'][0]['message']['from']['is_bot']
        self.from_first_nane =  update.json()['result'][0]['message']['from']['first_name']
        self.from_username =  update.json()['result'][0]['message']['from']['username']
        self.from_language_code = update.json()['result'][0]['message']['from']['language_code']
        self.chat_id = update.json()['result'][0]['message']['chat']['id']
        self.chat_first_name = update.json()['result'][0]['message']['chat']['first_name']
        self.chat_username = update.json()['result'][0]['message']['chat']['username']
        self.chat_type = update.json()['result'][0]['message']['chat']['type']
        self.date = update.json()['result'][0]['message']['date']
        self.voice_duration = update.json()['result'][0]['message']['voice']['duration']
        self.voice_mime_type = update.json()['result'][0]['message']['voice']['mime_type']
        self.file_id = update.json()['result'][0]['message']['voice']['file_id']
        self.file_unique_id = update.json()['result'][0]['message']['voice']['file_unique_id']
        self.file_file_size = update.json()['result'][0]['message']['voice']['file_size']

    def get_download_link(self, BOT_TOKEN):
        path = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={self.file_id}')
        file_path = path.json()['result']['file_path']
        download_link = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}'
        return download_link



