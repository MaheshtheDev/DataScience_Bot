import telebot
import time
import os
import requests
from flask import Flask, request
from bs4 import BeautifulSoup
bot_token = '1000110388:AAFdfrAD61GecD7sphhi2nvyGb_R_vu0xQc'
bot = telebot.TeleBot(token=bot_token)
server = Flask(__name__)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Welcome!')
    bot.send_message(message.chat.id, 'Use /latest for Latest Articles \nUse /trend for Trending Articles \nUse /dev for Developer Information')

pageds=requests.get("https://towardsdatascience.com/data-science/home")
soup = BeautifulSoup(pageds.content,'html.parser')
t2 = soup.find_all(class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
art_nameds = []
for i in t2:
    j = list(i)
    j1 = list(j[0])
    art_nameds.append(j1[0])
l = []
for i in soup.find_all('a',href=True):
    l.append(i['href'])
linksds = l[12:-6:4]

heading = "*Top Stories in Data Science*"
new_linksds = ""
for i in range(5):
    new_linksds += "\n" + str(i+1) +". <a href=\""+linksds[i]+"\">"+art_nameds[i]+"</a>" 

heading_ll = "*Latest Articles on Data Science in Towards DataScience*"
lat_links = ""
git_acc = "https://github.com/maheshthedev"
linkin = "https://www.linkedin.com/in/maheshthedev/"
for i in range(5,11):
    lat_links += "\n" + str(i-4) +". <a href=\""+linksds[i]+"\">"+art_nameds[i]+"</a>"
sm_links = "<a href=\""+linkin+"\">"+"LinkedIn"+"</a>"
sm_links +=" · " + "<a href=\""+git_acc+"\">"+"GitHub"+"</a>"

# pageml=requests.get("https://towardsdatascience.com/machine-learning/home")
# soup = BeautifulSoup(pageml.content,'html.parser')
# t2 = soup.find_all(class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
# art_nameml = []
# for i in t2:
#     j = list(i)
#     j1 = list(j[0])
#     art_nameds.append(j1[0])
# lml = []
# for i in soup.find_all('a',href=True):
#     lml.append(i['href'])
# linksml = lml[12:-6:4]

# new_linksml = ""
# for i in range(5):
#     new_linksml += "\n" + str(i+1) +". <a href=\""+linksml[i]+"\">"+art_nameml[i]+"</a>" 

@bot.message_handler(commands=['dev'])
def send_welcome(message):
    bot.send_message(message.chat.id, "I'm made by MaheshtheDev.\nHe is passionate about Data Science \nYou can Connect with my Developer:MaheshtheDev")
    bot.send_message(message.chat.id, sm_links,parse_mode='HTML')

@bot.message_handler(commands=['trend'])
def send_message(message):
    bot.send_message(message.chat.id,heading,parse_mode='Markdown')
    bot.send_message(message.chat.id,new_linksds,parse_mode='HTML')

@bot.message_handler(commands=['latest'])
def send_message(message):
    bot.send_message(message.chat.id,heading_ll,parse_mode='Markdown')
    bot.send_message(message.chat.id,lat_links,parse_mode='HTML')

@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://salty-scrubland-38376.herokuapp.com/' + bot_token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
