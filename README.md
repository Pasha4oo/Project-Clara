# AI User Bot

## What is this project about?
Telegram User bot for simulating human spelling and communicating with a real person using artificial intelligence.
In particular, in the telegram bot AnonRuBot. The task of "Clara" is to place a person in a dialogue with AI without informing him.

**Example of chat communication ("Clara" on the right, experimental on the left):**

<img src="https://github.com/user-attachments/assets/2b79f80d-0d86-4fdf-a513-781adff2c0c1" width="500">

**Logging example:**

<img src="https://github.com/user-attachments/assets/1822c41b-8d5b-47de-a445-b23f9772672f" width="500">

## How does this work?

**Imitation of humanity consists of the following points**

1. Errors in the text.  
2. Text with a small letter.  
3. Recognition of Telegram stickers. 
4. Recognition of audio messages, “circles”. 
5. No English. 
6. Reply after a time interval depending on the message size. 
7. Sending emoji. 
8. Understanding several consecutive messages in one. 
9. Sending several small responses instead of one big one. 
10. Editing your message, removes errors.
11. Sending reactions to a message. 
12. List of exception words. 
13. Understanding “responses” to a message.


*These 13 points allow you to achieve the best results*

### File descriptions

| Title | Description | 
|-------|-------------|
| Settings| Stores variables used in all other files|
| GUI | Created using PySide 6 Designer, stores a class that is imported into MessageHandler|
|MessageHandler| Main file running in two threads. The first thread is occupied by a GUI class object, it starts and stops the bot, and applies settings. The second thread is busy with the rest of the program. An asynchronous function reacts to messages based on keywords, performs premature processing and sends it for further processing to Processing or Media|
| Media | Processes audio/media into text thanks to vosk and sends it to Processing| 
| Processing | Processes text, contacts Character.Ai servers, performs basic setup, starts end timer, sends to TextErrors|
| TextErrors | Contacts SeoGift to retrieve text with errors. Sends reactions, imitates writing text. Routes the data to Loger and finally sends it to Telegram |
| Loger | Saves correspondence into a convenient file|


### Schemes

**Operation**

<img src="https://github.com/user-attachments/assets/89cd16fd-d435-4b09-98d7-0af4caccc5a5" width="500">


**Import**

<img src="https://github.com/user-attachments/assets/61b1ab47-3ce4-48d8-b945-de5930688be7" width="500">

## Getting Started
You need Python >= 3.12.3
```
git clone --recurse-submodules https://github.com/Pasha4oo/Project-Clara
```

```
python MessageHandler.py
```
