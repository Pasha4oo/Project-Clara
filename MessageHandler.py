from characterai import aiocai

from Media import audio_rec

from Processing import main

from Logger import save_chat

from Settings import *

from GUI import MainWindow

import sys

import json

from pyrogram import Client, filters
from pyrogram.types import Message

import websockets

import asyncio

from threading import Thread

from websockets.exceptions import ConnectionClosedOK

from PySide6.QtWidgets import QApplication

#Set your own id and hash
api_id = 0
api_hash = ''

app = Client('my_account', api_id=api_id, api_hash=api_hash)

#looks for comming messages from anon_bot and favorites
@app.on_message(filters.chat([])) #type chats id
async def not_main(client: Client, messages: Message):
    print('There')
    if window.started == True:
        print('Not There')
        global opened_time
        global opened_time_index
        global already_started
        global search
        global times
        global global_mes
        global hello_message
        mes = messages
        times = messages

        if not messages.media:
            print(messages.text)
        else:
            print(messages)
        try:

            if messages.from_user.is_bot == False and messages.chat.id not in chat_ids:
                first.append(0)
                chat_ids.append(messages.chat.id)
                clients_db.append(aiocai.Client(tokens[chat_ids.index(mes.chat.id)]))
                news.append('')
                opened_time.append(0)
                opened_time_index.append(-1)
                search = True

            if bool(messages.photo):
                await client.download_media(messages)

            client_id = chat_ids.index(messages.chat.id)

            if not messages.media and anon_bot and ((mes.text).upper()).find('/SEARCH') != -1 and search:
                if already_started == True:
                    already_started = False
                    first[client_id] = 0
                    search = False
                    await asyncio.sleep(7)
                    search = True
                    news[client_id] = 'a'
                    if already_started == False:
                        await app.send_message(mes.chat.id, 'а')

                elif already_started == False:
                    await asyncio.sleep(7)
                    print('FALSE')
                    print(client_id)
                    news[client_id] = ''
                    opened_time[opened_time_index[client_id]] = 0
                    search = True
                    first[client_id] = 0
                    already_started = False
                    try:
                        await main(news[client_id], client, clients_db[client_id], mes, client_id, first, app, news)
                    except (asyncio.exceptions.CancelledError, websockets.exceptions.ConnectionClosedOK):
                        print("ERR")
                        await asyncio.sleep(1)
                        await app.send_message(mes.chat.id, 'а')
                    except TimeoutError:
                        app.send_message(mes.chat.id, '/stop')
                    first[client_id] += 1
                    print(f'First: {first}')

            elif not messages.media and already_started == False and anon_bot and ((mes.text).upper()).find('СОБЕСЕДНИК НАЙДЕН') != -1:
                print('CHATTER FOUND!')
                save_chat('///', '///')
                await app.send_message(mes.chat.id, hello_message)
                already_started = True
                news[client_id] = 'a'

            elif not messages.media and ((mes.text).upper()).find('VIP-') != -1:
                pass

            elif not messages.media and ((mes.text).upper()).find('ЕСЛИ ХОТИТЕ,') != -1:
                pass

            elif not messages.media and ((mes.text).upper()).find('У ВАС НЕТ') != -1:
                pass

            elif not messages.media and ((mes.text).upper()).find('/STOPAD') != -1:
                pass

            elif not messages.media and ((mes.text).upper()).find('STOP') != -1:
                news[client_id] = ''
                opened_time[opened_time_index[client_id]] = 0
                search = True
                first[client_id] = 0
                already_started = False

            elif already_started and anon_bot and messages.from_user.is_self == False and ((mes.text).upper()).find('/SEARCH') == -1:
                print('/search FOUND!')
                mes = messages
                try:
                    save_chat('ANON', mes.text)
                except AttributeError:
                    print('Save ATR ERROR')
                print(chat_ids)
                print(tokens[chat_ids.index(messages.chat.id)])
                client_id = chat_ids.index(mes.chat.id)
                global_mes = messages
                await not_main_2(client_id, client, mes, messages, first, app, news)
        except AttributeError:
            print('ERROR ATR')
            global_mes = ''
            await asyncio.sleep(5)
            await app.send_message(mes.chat.id, '/stop')

async def not_main_2(client_id, client, mes, messages, first, app, news):
    print(bool(mes.sticker))
    print(bool(mes.media))
    if bool(mes.sticker) == False and bool(mes.media):
        try:
            print(client.download_media(messages))
            audio_text = audio_rec(await client.download_media(messages), messages)
            print(audio_text)
            await main(audio_text, client, clients_db[client_id], mes, client_id, first, app, news)
        except ValueError:
            print('ValueError')
            pass


    try:
        if (messages.text != None and ((messages.text).upper()).find('HTTP') == -1) or mes.sticker.file_name == 'sticker.webp':

            try:
                mes = messages

                print(f'From who? {mes.reply_to_message_id}')
                print(messages.from_user.is_self)

                if mes.reply_to_message_id != None and messages.from_user.is_self == True:
                    print(messages)
                    news[client_id] += f' {str((await app.get_messages(messages.chat.id, messages.reply_to_message_id)).text)} {str(messages.text)}'
                    print(news)

                else:
                    news[client_id] += f' {str(messages.text)}'

                try:
                    if mes.sticker.file_name == 'sticker.webp':
                        news[client_id] += f' {str(mes.sticker.emoji)}'
                except AttributeError:
                    pass

                print(opened_time)
                await time_and_push(first, mes, messages, client, news, clients_db, client_id, app)

            except asyncio.CancelledError:
                print('CancelledError :)')
                global_mes = ''
                await asyncio.sleep(5)
                await app.send_message(mes.chat.id, '/stop')
            except ConnectionClosedOK:
                print('WebScoket ERROR')
                global_mes = ''
                await asyncio.sleep(5)
                await app.send_message(mes.chat.id, '/stop')

    except AttributeError:
        pass

async def time_and_push(first, mes, messages, client, news, clients_db, client_id, app):
    global global_mes
    mes = messages
    client_id = chat_ids.index(mes.chat.id)
    if first[client_id] < 4:
        await asyncio.sleep(5)
    else:
        await asyncio.sleep(4)

    print('==============')
    print(global_mes.text)
    print(mes.text)

    if global_mes == mes:
        global_mes = ''
        first[client_id] += 1
        await asyncio.sleep(1)
        await main(news[client_id], client, clients_db[client_id], mes, client_id, first, app, news)

async def reset():
    global hello_message
    print('Reset Started!')
    with open('H://MyCode//UserBotForAlice//UserBotForAlice//downloads//chats//reset_settings.json', 'r') as chat:
        settings = json.load(chat)
        if settings:
            hello_message = settings['Greeting']
            print("APP CLOSED")
        print('OPEN CLOSED')
    await main('RESET_SETTINGS', '', '', '', '', '', '', '')

def button():
    global handler
    global app
    if window.started == False:
        print('Start')
        window.ui.pushButton_2.setText("Stop")
        first_sentences = window.ui.lineEdit.text()
        words = window.ui.lineEdit_2.text()
        hello_message = window.ui.lineEdit_3.text()
        char = window.ui.lineEdit_4.text()

        lineEdit_5 = window.ui.lineEdit_5.text()
        lineEdit_6 = window.ui.lineEdit_6.text()

        with open('H://MyCode//UserBotForAlice//UserBotForAlice//downloads//chats//reset_settings.json', 'w') as f:
            data = {}
            data['Questions'] = first_sentences
            data['Exceptions'] = words
            data['Greeting'] = hello_message
            data['Character'] = char
            data['api_id'] = lineEdit_5
            data['api_hash'] = lineEdit_6
            json.dump(data, f)

        window.started = True
        asyncio.run(reset())
    else:
        window.started = False
        window.ui.pushButton_2.setText("Start")
        print('False')

def gui():
    global window
    app_qt = QApplication()
    window = MainWindow(button)
    window.show()
    sys.exit(app_qt.exec())

if __name__ == '__main__':
    thread = Thread(target=gui, daemon=True)
    thread.start()
    app.run()