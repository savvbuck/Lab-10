import time
import requests
from voice import voice
import json


def create(type='single'):

    url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"
    querystring = {"format":"json", "blacklistFlags":"nsfw,racist", "lang":"en", "type":type}
    headers = {
	"X-RapidAPI-Key": "3f62fc2010mshd91f0dd98db5d87p1505edjsnb04b8d3e7538",
	"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    res = json.loads(response.text)
    voice.text_to_speech(res['setup'])
    time.sleep(1)
    voice.text_to_speech(res['delivery'])
    print(res['setup'], res['delivery'])
    


# def thanks(text):
#     options = [
#         'Было несложно!',
#         'Вам спасибо',
#         'Обращайтесь'
#     ]
#     voice.text_to_speech(random.choice(options))


# def relax(text):
#     options = [
#         'Ура, смотрим котиков!',
#         'Предлагаю ютуб',
#         'Лучше бы погулять сходили'
#     ]
#     # webbrowser.open('https://youtu.be/C72eSqbw6Wk?feature=shared', new=0, autoraise=True)
#     payload = {
#         'q': 'cats',
#         'regionCode': 'RU',
#         'maxResults': '100',
#         'key': 'AIzaSyCq-ThhgzsZGFZx-5z-CBOis9bY6e2AA6Y'
#     }

#     res = requests.get('https://www.googleapis.com/youtube/v3/search', params=payload)
#     vid = res.json()
#     idx = random.randint(0, 99)
#     vid = res.json()['items'][idx]['id']['videoId']
#     webbrowser.open(f'https://youtu.be/{vid}feature=shared', new=0, autoraise=True)
#     voice.text_to_speech(random.choice(options))


# def stop(text):
#     options = [
#         'За работу',
#         'Хватит на сегодня, да?',
#     ]
#     pyautogui.hotkey('ctrl', 'w')
#     voice.text_to_speech(random.choice(options))