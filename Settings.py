#from dotenv import load_dotenv

global app
global first_sentences
global words
global hello_message
global char
global api_id
global api_hash

#load_dotenv()

#api_id = os.getenv('api_id')
#api_hash = os.getenv('api_hash')

with open('H://MyCode//UserBotForAlice//UserBotForAlice//tokens.txt', 'r') as tok:
    tokens = tok.read().splitlines()
    print(tokens)

chat_ids = []
clients_db = []
newss = []
first = []
me = []

client_ai = ''

news = []
mes = ''
me_number = 0
opened_time = []
opened_time_index = []

message_count = 0

dev_mode = False
anon_bot = True
already_started = False
jik = True
stop = True
search = True
