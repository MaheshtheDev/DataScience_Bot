import telebot
import time
import os
import requests
from flask import Flask, request
from bs4 import BeautifulSoup
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot_token = '1000110388:AAFdfrAD61GecD7sphhi2nvyGb_R_vu0xQc'
bot = telebot.TeleBot(token=bot_token)
server = Flask(__name__)

git_acc = "https://github.com/maheshthedev"
linkin = "https://www.linkedin.com/in/maheshthedev/"
sm_links = "<a href=\""+git_acc+"\">"+"GitHub"+"</a>"
sm_links +=" · " + "<a href=\""+linkin+"\">"+"LinkedIn"+"</a>"

pageds=requests.get("https://towardsdatascience.com/data-science/home")
soup1 = BeautifulSoup(pageds.content,'html.parser')
t2 = soup1.find_all(class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
l = []
for i in soup1.find_all('a',href=True):
    l.append(i['href'])
pageml=requests.get("https://towardsdatascience.com/machine-learning/home")
soup2 = BeautifulSoup(pageml.content,'html.parser')
t3 = soup2.find_all(class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
for i in soup2.find_all('a',href=True):
    l.append(i['href'])
pageviz=requests.get("https://towardsdatascience.com/data-visualization/home")
soup3 = BeautifulSoup(pageviz.content,'html.parser')
t4 = soup3.find_all(class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
for i in soup3.find_all('a',href=True):
    l.append(i['href'])
t1 = t2 + t3 + t4

art_name = []
for i in t1:
    j = list(i)
    j1 = list(j[0])
    art_name.append(j1[0])

art_nameds = art_name[:11]
art_nameml = art_name[11:22]
art_nameviz = art_name[22:]

linksds = l[12:-130:4]
linksml = l[74:-68:4]
linksviz = l[136:-6:4]

headingdsl = "*Top Stories in Data Science*"
headingdst = "*Latest Articles on Data Science*"
headingmll = "*Top Stroies in Machine Learning"
headingmlt = "*Latest Articles on Machine Learning"
headingvizl = "*Top Stories in Visualization*"
headingvizt = "*Latest Articles on Visualization"

new_linksdsl = ""
for i in range(5):
    new_linksdsl += "\n" + str(i+1) +". <a href=\""+linksds[i]+"\">"+art_nameds[i]+"</a>" 
new_linksmll = ""
for i in range(5):
    new_linksmll += "\n" + str(i+1) +". <a href=\""+linksml[i]+"\">"+art_nameml[i]+"</a>" 
new_linksvizl = ""
for i in range(5):
    new_linksvizl += "\n" + str(i+1) +". <a href=\""+linksviz[i]+"\">"+art_nameviz[i]+"</a>" 

lat_linksdst = ""
for i in range(5,11):
    lat_linksdst += "\n" + str(i-4) +". <a href=\""+linksds[i]+"\">"+art_nameds[i]+"</a>"
lat_linksmlt = ""
for i in range(5,11):
    lat_linksmlt += "\n" + str(i-4) +". <a href=\""+linksml[i]+"\">"+art_nameml[i]+"</a>"
lat_linksvizt = ""
for i in range(5,11):
    lat_linksvizt += "\n" + str(i-4) +". <a href=\""+linksviz[i]+"\">"+art_nameviz[i]+"</a>"


def gen_markup1():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Data Science", callback_data="dsl"),InlineKeyboardButton("Machine Learning",callback_data="mll"),InlineKeyboardButton("Visualization",callback_data="vizl"))
    return markup

def gen_markup2():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Data Science", callback_data="dst"),InlineKeyboardButton("Machine Learning",callback_data="mlt"),InlineKeyboardButton("Visualization",callback_data="vizt"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "dsl":
        bot.send_message(call.message.chat.id,headingdsl,parse_mode='Markdown')
        bot.send_message(call.message.chat.id,new_linksdsl,parse_mode='HTML')
    elif call.data == "dst":
        bot.send_message(call.message.chat.id,headingdst,parse_mode='Markdown')
        bot.send_message(call.message.chat.id,lat_linksdst,parse_mode='HTML')    
    elif call.data == "mll":
            bot.send_message(call.message.chat.id,headingmll,parse_mode='Markdown')
            bot.send_message(call.message.chat.id,new_linksmll,parse_mode='HTML')    
    elif call.data == "mlt":
            bot.send_message(call.message.chat.id,headingmlt,parse_mode='Markdown')
            bot.send_message(call.message.chat.id,lat_linksmlt,parse_mode='HTML')    
    elif call.data == "vizl":
            bot.send_message(call.message.chat.id,headingvizl,parse_mode='Markdown')
            bot.send_message(call.message.chat.id,new_linksvizl,parse_mode='HTML')    
    elif call.data == "vizt":
            bot.send_message(call.message.chat.id,headingvizt,parse_mode='Markdown')
            bot.send_message(call.message.chat.id,lat_linksvizt,parse_mode='HTML')    

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Welcome!')
    bot.send_message(message.chat.id, 'Use /latest for Latest Articles \nUse /trend for Trending Articles \nUse /dev for Developer Information')

@bot.message_handler(commands=['dev'])
def send_welcome(message):
    bot.send_message(message.chat.id, "I'm made by MaheshtheDev.\nHe is passionate about Data Science \nYou can Connect with my Developer!")
    bot.send_message(message.chat.id, sm_links,parse_mode='HTML')

@bot.message_handler(commands=['trend'])
def send_message(message):
    bot.send_message(message.chat.id,"Select the Category", reply_markup=gen_markup1())

@bot.message_handler(commands=['latest'])
def send_message(message):
    bot.send_message(message.chat.id,"Select the Category", reply_markup=gen_markup2())

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
