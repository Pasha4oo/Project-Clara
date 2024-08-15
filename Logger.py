import demoji
from time import time

#Saves message, converts emojis into text
def save_chat(who, text):
    try:
        with open('H://MyCode//UserBotForAlice//UserBotForAlice//downloads//chats//chats.txt', 'a') as chat:
            chat.write(f'{who} :: {demoji.replace_with_desc(text)} :: {time()} \n')
    except Exception as error:
        print(f'LOGGER ERROR: {error}')