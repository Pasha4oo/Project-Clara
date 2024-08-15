from requests import post, Session
from bs4 import BeautifulSoup
from random import randint
from Settings import dev_mode
import asyncio
from pyrogram.errors import MessageNotModified
from pyrogram.enums import ChatAction
from Logger import save_chat

def send_text(lines, percent, transp='2', lowercase='', spaces='do', english_errors=''):
    #creates session and request text with errors
    url = 'https://seogift.ru/tools/generator-opechatok/'
    s = Session()
    payload = {
    'lines' : lines,
    'tolowercase' : lowercase,
    'deletemorespaces': spaces,
    'withenglish' : english_errors,
    'wordscounttransp' : transp,
    'percentrepl' : percent,
    'doactiontool' : 'do'
    }

    session = Session()

    data_text = session.post(url, data = payload)
    nasd = BeautifulSoup(data_text.text,"html.parser")

    ready_text = nasd.find('textarea', {'class' : 'int_text textarea_block'})
    print(ready_text.text)

    return ready_text.text

async def random_removes_errors(a, app, mes):
    #edit message after sending with 33% chance
    if randint(1,3) == 1:
        try:
            print('Edit Text!')
            await app.read_chat_history(mes.chat.id)
            await app.send_chat_action(mes.chat.id, ChatAction.TYPING)
            text_with_errors = send_text(a, '2', lowercase='do')
            if dev_mode == False:
                await asyncio.sleep(len(text_with_errors)//8)
            if True:
                edited_text = await app.send_message(mes.chat.id, text_with_errors)
                try:
                    save_chat('CLARA', edited_text.text)
                except AttributeError:
                    print('Save ATR ERROR')
                text_without_errors = send_text(a, '0', lowercase='do', transp='0')
                await asyncio.sleep(1)

        except MessageNotModified:
            pass

        if text_with_errors != text_without_errors:
                await app.edit_message_text(mes.chat.id, edited_text.id, text_without_errors)


    else:
        await app.read_chat_history(mes.chat.id)
        await app.send_chat_action(mes.chat.id, ChatAction.TYPING)
        text_with_errors = send_text(a, '3', lowercase='do')
        if dev_mode == False:
            await asyncio.sleep(len(text_with_errors)//8)
        if True:
            edited_text = await app.send_message(mes.chat.id, text_with_errors)
            try:
                save_chat('CLARA', edited_text.text)
            except AttributeError:
                print('Save ATR ERROR')

    #send rock emoji with 10% chance
    if randint(1,10) == 1 and int(mes.chat.id) != 7099353146:
        try:
            await app.send_reaction(mes.chat.id, mes.id, "🗿")
        except Exception as error:
            print(f'TEXT ERRORS ERROR: {error}')
