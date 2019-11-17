import requests

proxies = {
    'http': 'http://13.95.132.65:8888',
    'https': 'https://13.95.132.65:8888'
    }
TOKEN = '593269274:AAFpkvb2SmMFXKAoWAY22akbBrwYJ76rnnk'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

payload = {
    'chat_id': 259297371,
    'text': 'И тебе привет, Славка',
    'reply_to_message_id': 14
    }

r = requests.post(f'{MAIN_URL}/sendMessage', data=payload)

print(r.json())
