import time
import requests
from voice import voice
import json


def single_joke(text):
    create(type='single')

def twopart_joke(text):
    create(type='twopart')

def write_down(text):
    with open('joke_list.txt', 'a') as jk:
        with open ('template.txt', 'r') as tmp:
            jk.write(f'{tmp.read()}\n')
            jk.flush()
    voice.text_to_speech('Previous joke was written to joke_list.txt')


def clear(text):
    with open('joke_list.txt', 'w') as jk:
        jk.close()
    voice.text_to_speech('joke_list was cleared')


def create(type='twopart'):
    url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"
    querystring = {"format":"json", "blacklistFlags":"nsfw,racist", "lang":"en", "type":type}
    headers = {
	"X-RapidAPI-Key": "3f62fc2010mshd91f0dd98db5d87p1505edjsnb04b8d3e7538",
	"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    res = json.loads(response.text)
    if res['type'] == 'single':
        with open('template.txt', 'w') as tmp:
            tmp.write(res['joke'])
        voice.text_to_speech(res['joke'])
    if res['type'] == 'twopart':
        with open('template.txt', 'w') as tmp:
            tmp.write(res['setup'])
            tmp.write(res['delivery'])
        voice.text_to_speech(res['setup'])
        time.sleep(0.7)
        voice.text_to_speech(res['delivery'])
    
    


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