import random
import telebot
import pyowm
from telebot import types
from pyowm.utils.config import get_default_config
from telebot.types import ReplyKeyboardMarkup
import requests
from bs4 import BeautifulSoup
import csv
HOST1 = 'https://www.ixbt.com'
URL1 = 'https://www.ixbt.com/news/'
HEADERS1 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.459'}


HOST2 = 'https://ua.korrespondent.net'
URL2 = 'https://ua.korrespondent.net'
HEADERS2 = { 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.459'}


HOST3 = 'https://sport.ua/'
URL3 = 'https://sport.ua/news/cyber'
HEADERS3 = { 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

HOST4 ='https://sport.24tv.ua'
URL4 = 'https://sport.24tv.ua/sport_tag1125/'
HEADERS4 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

HOST5 = 'https://zaxid.net'
URL5 = 'https://zaxid.net/koronavirus_v_ukrayini_statistika_kilkist_hvorih_na_koronavirus_ostanni_dani_n1499341'
HEADERS5 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

HOST6 = 'https://google.com'
URL6 = 'https://www.google.com/search?client=opera-gx&q=????????????????????+??????????????????????&sourceid=opera&ie=UTF-8&oe=UTF-8'
HEADERS6 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
####################################nomer 1
def get_html1(url, params =''):
    r = requests.get(url,headers = HEADERS1,params = params)
    return r
def get_content1(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li',class_= 'item item__border')
    info = []
    for item in items:
        info.append(
            [
                # 'text1': item.find('a', class_='href').get_text(strip=True),
                HOST1 + item.find('a').get('href')
                # item.find('div', class_='item__text__top').get_text(strip=True),
                # item.find('div', class_='item-image').find('img').get('src')
            ]

        )
        # for link in item.find_all('a', href=True):
        #     print(link['href'])
    return info
# html1 = get_html1(URL1)
# print(get_content1(html1.text))
###############################nomer 2
def get_html2(url,params=''):
    r = requests.get(url, headers=HEADERS2,params=params)
    return r
def get_content2(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'article')
    news = []
    for item in items:
        news.append(
            [
                # item.find('h3',class_='text').get_text(strip=True),
                item.find('a').get('href')
                ]
        )
    return news
# html2 = get_html2(URL2)
# print(get_content2(html2.text))
###############################nomer3
def get_html3(url,params=''):
    r = requests.get(url, headers=HEADERS3,params=params)
    return r
def get_content3(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'hentry')
    news = []
    for item in items:
        news.append(
            [
                item.find('a').get('href')
                ]
        )
    return news
#html3 = get_html3(URL3)
#print(get_content3(html3.text))
##########################################nomer4
def get_html4(url,params=''):
    r = requests.get(url, headers=HEADERS4,params=params)
    return r
def get_content4(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('article', class_ = 'small-12 medium-4 column')
    news = []
    for item in items:
        news.append(
            [
                # item.find('h3',class_='text').get_text(strip=True),
                item.find('a').get('href')
                ]
        )
    return news
# html4 = get_html4(URL4)
# print(get_content4(html4.text))
#########################################################nomer 5
def get_html5(url,params=''):
    r = requests.get(url, headers=HEADERS5,params=params)
    return r
def get_content5(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', id = 'newsSummary')
    news = []
    for i in items:
        news.append(
                # item.find('h3',class_='text').get_text(strip=True),
                i.find('ul').get_text()
        )
    return news
# html5 = get_html5(URL5)
# print(get_content5(html5.text))
############################################################NOMER 6
def get_html6(url,params=''):
    r = requests.get(url, headers=HEADERS6,params=params)
    return r
def get_content6(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', jsname = 'fUyIqc')
    news = []
    for i in items:
        news.append(
                # item.find('h3',class_='text').get_text(strip=True),
                 '????????????: '+ i.get_text()
        )
    return news
html6 = get_html6(URL6)
print(get_content6(html6.text))
############################################################
bot = telebot.TeleBot("1289317345:AAEKofsKDQtrcQQDW7zHt8O8fTvIpm_9ev4")
@bot.message_handler(commands=['start'])
def send_welocme(message):
    bot.send_message(
        message.chat.id,
        "?????? ?????????? ???????????????????? ??????",
        reply_markup=keyboard()
    )
first = ["???????????????? - ?????????????????? ???????? ?????? ?????????? ????????????????." \
    , "?????????????????????? ???????? ?????? ????????, ?????? ?????????????????? ???? ???????????????? ????????????!", \
         "???????????? ????????????????, ???????????????? ?????????? ???????????? ???????????????? ???? ???????? ?????????????????? ??????????????????.", \
         "?????????????????? ?????? ?????? ????????, ?????? ???????????? ???????? ???????????????? ?????? ?????????????????????? ???? ??????????????.", \
         "???????????? ???????? ?????? ????????, ?????? ?????????????????????? ?? ???????????????????????? ????????????????."]

first_part_of_second = ["?????? ??????'????????????, ???? ???????????? ?? ?????????? ?????????????? ???????????????? ???? ???????????????? ??????", \
                        "???????? ?????????????? ???? ??????????, ?????????????????????? ?????????????????? ??????", \
                        "????, ?????? ???????????????? ?????????????????? ???????????????? ???????????? ??????????, ?????????????? ??????'?????????? ??????", \
                        "???????? ?? ?????? ?????????????? ??????, ???????????????? ?????????? ????", \
                        "??????'????????????, ???? ?????????? ??????????????????????, ?? ?????????????? ?????? ???????????????? ?????? ???????????????? ???????????????? ???????????? ??????"]
second_part_of_second = ["?????????????????? ?? ?????????????? ?? ??????????????????.", \
                         "???????????? ?? ???????????? ??????????????, ?????? ???????????? ?????? ?????????????????? ?????????????????????? ????????????.", \
                         "???????? ?? ???????? ????????????'??, ???????????? ???? ???????????? ???????????????? ???????????? ??????????????.", \
                         "???????????????? ?????????????? - ???????????????? ????, ?????? ???? ???? ???????????????? ??????????.", \
                         "????????????????????, ?????? ???? ?????????????????????? ???????? ?? ?????????????????? ???????? ?? ?????????? ????????????."]

third = ["?????? ?????????? ???????????? ???????????????? ?????? ????????????????????, ?????? ???????????????? ???? ?????????????? ???? ????????????????.", \
         "????????????, ???? ?????????? ?????????????????????? ???????????? ????????????????????????, ???????? ???????????????????? ?????? ???????? ?????????????????? ????????.", \
         "???????????? ???????? ???? ???? ?????????????? ???????????????? ?????????? ?????????????????????????? ????????????????, ???? ???????? ?? ???????????????? ???????????? ???? ??????????.", \
         "???? ???????????????? ?????????????? ???????????????? ?????????????????? - ???????????????? ?????? ?????????? ??????, ???????? ???????? ?????????????????? ????????????.", \
         "???????? ???????????????????? ???????????????????? ???? ?????????? - ???????????????? ????????????, ?? ???????? ???? ?????????????? ???????????????? ?????? ?????????????? ??????????????."]

zodiac = ["????????", "??????????", "????????????????", "??????", "??????", "????????", "????????", "????????????????", "??????????????", "??????????????", "??????????????",
          "????????"]
whether1 = "??????????"
whether2 = "????????????"
whether3 = "????????"
whether4 = "??????????"
whether5 = "????????????"

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False,resize_keyboard=True)
    btn1 = types.KeyboardButton('??? ???????????? ???')
    markup.add(btn1)
    horoscope = types.KeyboardButton('??? ???????????????? ???')
    markup.add(horoscope)
    news = types.KeyboardButton('??? ???????????? ???')
    markup.add(news)
    return markup


@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "??? ???????????????? ???":
        # ?????????????? ????????????
        keyboard = types.InlineKeyboardMarkup()
        # ???? ?????????????? ?????????????? ?????????? ?? ???????????????????? ?????? ?????????????? ?????????? ??????????????
        key_oven = types.InlineKeyboardButton(text='????????', callback_data='zodiac')
        # ?? ?????????????????? ???????????? ???? ??????????
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='??????????', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='????????????????', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='??????', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='??????', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='????????', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='????????', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='????????????????', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='??????????????', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='??????????????', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='??????????????', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='????????', callback_data='zodiac')
        keyboard.add(key_ryby)
        # ???????????????????? ?????? ???????????? ?????????? ?? ?????????? ?????????????????? ?? ????????????
        bot.send_message(message.from_user.id, text='???????????? ???????? ???????? ??????????????', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "????????????????????????.\n?????? ?????????????? ???? ????????????(???????? ?? ?????? ???????????? ????????????)????????????????: /m.!????????????????: ???????? ???? ?????????????? ????????????, ???????????????????? ???? ???????????????? ???? ???????????????? ???????????? \"??????????\", ?????? ???? ???????????? \"???????????? ?? ????????\"!")

    elif message.text == "??? ???????????? ???":
        keyboard = types.InlineKeyboardMarkup()
        key_kiber = types.InlineKeyboardButton(text='???????????? ??????????????????????', callback_data='kibersport')
        keyboard.add(key_kiber)
        key_political = types.InlineKeyboardButton(text='???????????? ??????????????????', callback_data='political')
        keyboard.add(key_political)
        key_technologies = types.InlineKeyboardButton(text='???????????? ???????????????????? ??????????', callback_data='technologies')
        keyboard.add(key_technologies)
        key_sport = types.InlineKeyboardButton(text='???????????? ????????????', callback_data='sport')
        keyboard.add(key_sport)
        key_statistic = types.InlineKeyboardButton(text = '???????????????????? ???????????????????????? ?? ??????????????', callback_data = 'statistic')
        keyboard.add(key_statistic)
        bot.send_message(message.from_user.id, text='???????????? ???????????? ??????????', reply_markup=keyboard)

    elif message.text == "??? ???????????? ???":
        keyboard = types.InlineKeyboardMarkup()
        key_lutsk = types.InlineKeyboardButton(text='??????????', callback_data='whether1')
        keyboard.add(key_lutsk)
        key_kovel = types.InlineKeyboardButton(text='????????????', callback_data='whether2')
        keyboard.add(key_kovel)
        key_kyiv = types.InlineKeyboardButton(text='????????', callback_data='whether3')
        keyboard.add(key_kyiv)
        key_lviv = types.InlineKeyboardButton(text='??????????', callback_data='whether4')
        keyboard.add(key_lviv)
        key_harkiv = types.InlineKeyboardButton(text='????????????', callback_data='whether5')
        keyboard.add(key_harkiv)
        bot.send_message(message.from_user.id, text='???????????? ?????????? ??????????', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "?? ???????? ???? ??????????????. ???????????? /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # ???????? ???????????? ???? ???????? ???? 12 ???????????? ??? ?????????????? ????????????????
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = pyowm.OWM('ed2e2b6901a1f27028e28903a963d4be', config_dict)

    if call.data == "zodiac":
    # ?????????????????? ????????????????
        msg = random.choice(first) + ' ' + random.choice(first_part_of_second) + ' ' + random.choice(
            second_part_of_second) + ' ' + random.choice(third)
        # ???????????????????? ?????????? ?? ????????????????
        bot.send_message(call.message.chat.id, msg)
    if call.data == "whether1":
        observation = owm.weather_manager().weather_at_place(whether1)
        w = observation.weather
        temp = w.temperature('celsius')
        temputure = "?????????????????????? ?? "+ whether1 + " ?????????? " + str(temp['temp']) +"\n" "???????????????????????? ???? " + str(temp['feels_like'])
        # ???????????????????? ?????????? ?? ????????????????
        bot.send_message(call.message.chat.id, temputure)
    if call.data == "whether2":
        observation = owm.weather_manager().weather_at_place(whether2)
        w = observation.weather
        temp = w.temperature('celsius')
        temputure = "?????????????????????? ?? "+ whether2 + " ?????????? " + str(temp['temp']) +"\n" "???????????????????????? ???? " + str(temp['feels_like'])
        # ???????????????????? ?????????? ?? ????????????????
        bot.send_message(call.message.chat.id, temputure)
    if call.data == "whether3":
        observation = owm.weather_manager().weather_at_place(whether3)
        w = observation.weather
        temp = w.temperature('celsius')
        temputure = "?????????????????????? ?? "+ whether3 + " ?????????? " + str(temp['temp']) +"\n" "???????????????????????? ???? " + str(temp['feels_like'])
        # ???????????????????? ?????????? ?? ????????????????
        bot.send_message(call.message.chat.id, temputure)
    if call.data == "whether4":
        observation = owm.weather_manager().weather_at_place(whether4)
        w = observation.weather
        temp = w.temperature('celsius')
        temputure = "?????????????????????? ?? "+ whether4 + " ?????????? " + str(temp['temp']) +"\n" "???????????????????????? ???? " + str(temp['feels_like'])
        # ???????????????????? ?????????? ?? ????????????????
        bot.send_message(call.message.chat.id, temputure)
    if call.data == "whether5":
        observation = owm.weather_manager().weather_at_place(whether5)
        w = observation.weather
        temp = w.temperature('celsius')
        temputure = "?????????????????????? ?? "+ whether5 + " ?????????? " + str(temp['temp']) +"\n" "???????????????????????? ???? " + str(temp['feels_like'])
        # ???????????????????? ?????????? ?? ????????????????
        bot.send_message(call.message.chat.id, temputure)
    if call.data == "kibersport":
        html3 = get_html3(URL3)
        for i in range(6):
            bot.send_message(call.message.chat.id,get_content3(html3.text)[i])
        keyboard = types.InlineKeyboardMarkup()
        key_kiber = types.InlineKeyboardButton(text='???????????? ??????????????????????', callback_data='kibersport')
        keyboard.add(key_kiber)
        key_political = types.InlineKeyboardButton(text='???????????? ??????????????????', callback_data='political')
        keyboard.add(key_political)
        key_technologies = types.InlineKeyboardButton(text='???????????? ???????????????????? ??????????', callback_data='technologies')
        keyboard.add(key_technologies)
        key_sport = types.InlineKeyboardButton(text='???????????? ????????????', callback_data='sport')
        keyboard.add(key_sport)
        key_statistic = types.InlineKeyboardButton(text='???????????????????? ???????????????????????? ?? ??????????????', callback_data='statistic')
        keyboard.add(key_statistic)
        bot.send_message(call.from_user.id, text='???????????? ???????????? ??????????', reply_markup=keyboard)
    if call.data == 'technologies':
        html1 = get_html1(URL1)
        for i in range(len(get_content1(html1.text))):
            bot.send_message(call.message.chat.id,get_content1(html1.text)[i])
        keyboard = types.InlineKeyboardMarkup()
        key_kiber = types.InlineKeyboardButton(text='???????????? ??????????????????????', callback_data='kibersport')
        keyboard.add(key_kiber)
        key_political = types.InlineKeyboardButton(text='???????????? ??????????????????', callback_data='political')
        keyboard.add(key_political)
        key_technologies = types.InlineKeyboardButton(text='???????????? ???????????????????? ??????????', callback_data='technologies')
        keyboard.add(key_technologies)
        key_sport = types.InlineKeyboardButton(text='???????????? ????????????', callback_data='sport')
        keyboard.add(key_sport)
        key_statistic = types.InlineKeyboardButton(text='???????????????????? ???????????????????????? ?? ??????????????', callback_data='statistic')
        keyboard.add(key_statistic)
        bot.send_message(call.from_user.id, text='???????????? ???????????? ??????????', reply_markup=keyboard)
    if call.data == 'political':
        html2 = get_html2(URL2)
        for i in range(6):
            bot.send_message(call.message.chat.id,get_content2(html2.text)[i])
        keyboard = types.InlineKeyboardMarkup()
        key_kiber = types.InlineKeyboardButton(text='???????????? ??????????????????????', callback_data='kibersport')
        keyboard.add(key_kiber)
        key_political = types.InlineKeyboardButton(text='???????????? ??????????????????', callback_data='political')
        keyboard.add(key_political)
        key_technologies = types.InlineKeyboardButton(text='???????????? ???????????????????? ??????????', callback_data='technologies')
        keyboard.add(key_technologies)
        key_sport = types.InlineKeyboardButton(text='???????????? ????????????', callback_data='sport')
        keyboard.add(key_sport)
        key_statistic = types.InlineKeyboardButton(text='???????????????????? ???????????????????????? ?? ??????????????', callback_data='statistic')
        keyboard.add(key_statistic)
        bot.send_message(call.from_user.id, text='???????????? ???????????? ??????????', reply_markup=keyboard)
    if call.data == 'sport':
        html4 = get_html4(URL4)
        for i in range(4):
            bot.send_message(call.message.chat.id,get_content4(html4.text)[i])
        keyboard = types.InlineKeyboardMarkup()
        key_kiber = types.InlineKeyboardButton(text='???????????? ??????????????????????', callback_data='kibersport')
        keyboard.add(key_kiber)
        key_political = types.InlineKeyboardButton(text='???????????? ??????????????????', callback_data='political')
        keyboard.add(key_political)
        key_technologies = types.InlineKeyboardButton(text='???????????? ???????????????????? ??????????', callback_data='technologies')
        keyboard.add(key_technologies)
        key_sport = types.InlineKeyboardButton(text='???????????? ????????????', callback_data='sport')
        keyboard.add(key_sport)
        key_statistic = types.InlineKeyboardButton(text='???????????????????? ???????????????????????? ?? ??????????????', callback_data='statistic')
        keyboard.add(key_statistic)
        bot.send_message(call.from_user.id, text='???????????? ???????????? ??????????', reply_markup=keyboard)
    if call.data == 'statistic':
        html6 = get_html6(URL6)
        html5 = get_html5(URL5)
        bot.send_message(call.message.chat.id, get_content6(html6.text))
        bot.send_message(call.message.chat.id, get_content5(html5.text))
        keyboard = types.InlineKeyboardMarkup()
        key_kiber = types.InlineKeyboardButton(text='???????????? ??????????????????????', callback_data='kibersport')
        keyboard.add(key_kiber)
        key_political = types.InlineKeyboardButton(text='???????????? ??????????????????', callback_data='political')
        keyboard.add(key_political)
        key_technologies = types.InlineKeyboardButton(text='???????????? ???????????????????? ??????????', callback_data='technologies')
        keyboard.add(key_technologies)
        key_sport = types.InlineKeyboardButton(text='???????????? ????????????', callback_data='sport')
        keyboard.add(key_sport)
        key_statistic = types.InlineKeyboardButton(text='???????????????????? ???????????????????????? ?? ??????????????',callback_data='statistic')
        keyboard.add(key_statistic)
        bot.send_message(call.from_user.id, text='???????????? ???????????? ??????????', reply_markup=keyboard)
bot.polling(none_stop=True, interval=0)
