from speech_recognition import *
from entitys import *
import time


BOT_TOKEN = '6067696369:AAEVrzTDSJc3tW_Jb7jF89NjB6MCS6Q89k8'

query = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates")

if len(query.json()['result']) != 0:
    offset = int(query.json()['result'][0]['update_id'])
else:
    offset = int(open('lastoffset.txt').readline())

while True:
    update = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={offset}")
    if len(update.json()['result']) != 0 and 'message' in update.json()['result'][0] and 'voice' in update.json()['result'][0]['message']:
        start = time.time()
        print('Обработка голосового сообщения ...')
        message = VoiceMessage(update)


        voice_message = requests.get(message.get_download_link(BOT_TOKEN))
        with open('message_data/message.mp3', 'wb') as file:
            file.write(voice_message.content)
        recognition_text = speech_recognition(file_path='message_data/message.mp3')

        original_message_id = message.message_id

        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={message.chat_id}&text={recognition_text}&reply_to_message_id={original_message_id}")

        offset += 1

        stop = time.time()
        print('Ответ отправлен!')
        print(f'Запрос был обработан за {stop-start} секунд')
        with open('lastoffset.txt', 'w') as file:
            file.write(str(offset))
    elif len(update.json()['result']) != 0:
        print('Получено не голосовое сообщение')
        offset += 1
        with open('lastoffset.txt', 'w') as file:
            file.write(str(offset))





