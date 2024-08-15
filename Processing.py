from TextErrors import random_removes_errors

from Settings import *

import asyncio

import re

from time import time

import json

import pandas as pd

async def send_message_to_ai(chat, user_text, client_id):
    message = await chat.send_message(
        char, newss[client_id].chat_id, user_text
    )
    print(f'{message.name}: {message.text}')

    return message

async def exceptions(message):
    for word in words:
        print(word)
        if ((message.text).upper()).find(word) != -1:
            return True
    return False

async def bad_words(chat, message):
    while await asyncio.sleep(0, result=True):
        if re.search('[a-zA-Z]', message.text) != None or len(list(message.text)) >= 100 or await exceptions(message):
            print('Bad letters detected! Reroll')

            chat_id = (message.turn_key).chat_id
            turn_id = (message.turn_key).turn_id

            message = await chat.next_message(
            char, chat_id, turn_id
            )

            print(f'{message.name}: {message.text}')

            await asyncio.sleep(0.1)

            continue
        else:
            return message

async def main(text, tel_client, cli, mes, client_id, first, app, news):
    global opened_time
    global message_count
    global client
    global char
    global chat_id
    global turn_id
    global chat_ids
    global timet
    global first_sentences
    global words
    timet = mes

    if text == 'RESET_SETTINGS':
        print("PROCESSING RESET STARTED")
        with open('H://MyCode//UserBotForAlice//UserBotForAlice//downloads//chats//reset_settings.json', 'r') as chat:
            settings = json.load(chat)
            if settings:
                first_sentences = settings['Questions'].split(',')
                print(first_sentences)
                words = settings['Exceptions'].split(',')
                char = settings['Character']
                print("CLOSED")
    else:
        message_count = 0
 
        if first[client_id] == 0:
            first[client_id] += 1
            print('Init ME')
            print(first)
            me.append(await cli.get_me())

        new = 0
        answer = 0

        print('Starting async chat')
        async with await cli.connect() as chat:

            print('Successfully started chat')
            print(f'FIRST: {first}')

            if first[client_id] == 1:
                new, answer = await chat.new_chat(
                    char, me[client_id].id
                )
                if anon_bot and len(newss) < client_id:
                    newss[client_id] = new
                else:
                    newss.append(new)
                print('Before answer')
                print(f'{answer.name}: {answer.text}')

                for sentence in first_sentences:
                    print(sentence)
                    message = await send_message_to_ai(chat, sentence, client_id)
                    message = await bad_words(chat, message)

                await app.send_message(mes.chat.id, '/search')
                already_started = False
                await timer(mes, client_id, app)

            if first[client_id] >= 2:
                text.replace('None', '')
                message = await send_message_to_ai(chat, text, client_id)
                await asyncio.sleep(0.1)
                message = await bad_words(chat, message)

                message = str(message.text).replace('.', '\n')
                message = str(message).replace('! ', '! \n')
                message = str(message).replace('? ', '? \n')
                message = str(message).split("\n")
                print(message)

                for a in message:

                    #await stickers_check(a)

                    if a != '' and a != None:

                        await random_removes_errors(a, app, mes)
                opened_time[opened_time_index[client_id]] = 0
                news[client_id] = ''
                await timer(mes, client_id, app)

async def timer(messages, client_id, app):
    than = time()
    now = time()
    print(now - than)
    while now - than < 120:
        now = time()
        await asyncio.sleep(5)
        print(now - than)
    if timet == messages:
        await app.send_message(messages.chat.id, '/stop')
