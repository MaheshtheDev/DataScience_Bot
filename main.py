import telebot
import time
import os
import requests
from flask import Flask, request
from bs4 import BeautifulSoup
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
bot_token = '1193768093:AAH9yTXq77fgpWHhv1HsusfBeunEo135fDc'
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

headingdst = "Top Stories in Data Science"
headingdsl = "Latest Articles on Data Science"
headingmlt = "Top Stories in Machine Learning"
headingmll = "Latest Articles on Machine Learning"
headingvizt = "Top Stories in Visualization"
headingvizl = "Latest Articles on Visualization"

new_linksdsl = "<b>"+headingdsl+"</b>"
for i in range(5):
    new_linksdsl += "\n" + str(i+1) +". <a href=\""+linksds[i]+"\">"+art_nameds[i]+"</a>" 
new_linksmll = "<b>"+headingmll+"</b>"
for i in range(5):
    new_linksmll += "\n" + str(i+1) +". <a href=\""+linksml[i]+"\">"+art_nameml[i]+"</a>" 
new_linksvizl = "<b>"+headingvizl+"</b>"
for i in range(5):
    new_linksvizl += "\n" + str(i+1) +". <a href=\""+linksviz[i]+"\">"+art_nameviz[i]+"</a>" 

lat_linksdst = "<b>"+headingdst+"</b>"
for i in range(5,11):
    lat_linksdst += "\n" + str(i-4) +". <a href=\""+linksds[i]+"\">"+art_nameds[i]+"</a>"
lat_linksmlt = "<b>"+headingmlt+"</b>"
for i in range(5,11):
    lat_linksmlt += "\n" + str(i-4) +". <a href=\""+linksml[i]+"\">"+art_nameml[i]+"</a>"
lat_linksvizt = "<b>"+headingvizt+"</b>"
for i in range(5,11):
    lat_linksvizt += "\n" + str(i-4) +". <a href=\""+linksviz[i]+"\">"+art_nameviz[i]+"</a>"


# def gen_markup1():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 1
#     markup.add(InlineKeyboardButton("Data Science", callback_data="dsl"),InlineKeyboardButton("Machine Learning",callback_data="mll"),InlineKeyboardButton("Visualization",callback_data="vizl"))
#     return markup
hidekeyboard = types.ReplyKeyboardRemove()
def reply_markup1():
    markupl = ReplyKeyboardMarkup()
    markupl.row_width = 1
    item_bt1 = types.KeyboardButton('/l Data Science')
    item_bt2 = types.KeyboardButton('/l Machine Learning')
    item_bt3 = types.KeyboardButton('/l Data Vizualization')
    markupl.add(item_bt1,item_bt2,item_bt3)
    return markupl

def reply_markup2():
    markupl = ReplyKeyboardMarkup()
    markupl.row_width = 1
    item_bt1 = types.KeyboardButton('/t Data Science')
    item_bt2 = types.KeyboardButton('/t Machine Learning')
    item_bt3 = types.KeyboardButton('/t Data Vizualization')
    markupl.add(item_bt1,item_bt2,item_bt3)
    return markupl

@bot.message_handler(func=lambda message: message.text in ['/l Data Science','/l Machine Learning','/l Data Vizualization','/t Data Science','/t Machine Learning','/t Data Vizualization'])
def send_message(message):
    bot.send_chat_action(message.chat.id, 'typing')
    if message.text == "/l Data Science":
        bot.send_message(message.chat.id,new_linksdsl,parse_mode='HTML',reply_markup=hidekeyboard)
    if message.text == "/l Machine Learning":
        bot.send_message(message.chat.id,new_linksmll,parse_mode='HTML',reply_markup=hidekeyboard)
    if message.text == "/l Data Vizualization":
        bot.send_message(message.chat.id,new_linksvizl,parse_mode='HTML',reply_markup=hidekeyboard)  
    if message.text == "/t Data Science":
        bot.send_message(message.chat.id,lat_linksdst,parse_mode='HTML',reply_markup=hidekeyboard)        
    if message.text == "/t Machine Learning":
        bot.send_message(message.chat.id,lat_linksmlt,parse_mode='HTML',reply_markup=hidekeyboard)      
    if message.text == "/t Data Vizualization":
        bot.send_message(message.chat.id,lat_linksvizt,parse_mode='HTML',reply_markup=hidekeyboard)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Welcome, Pal!')
    bot.send_message(message.chat.id, 'Use /latest for Latest Articles \nUse /trend for Trending Articles \nUse /dev for Developer Information')

@bot.message_handler(commands=['dev'])
def send_welcome(message):
    bot.send_message(message.chat.id, "I'm made by MaheshtheDev.\nYou can Connect with my Developer!")
    bot.send_message(message.chat.id, sm_links,parse_mode='HTML')

@bot.message_handler(commands=['trend'])
def send_message(message):
    bot.send_message(message.chat.id,"Select the Category", reply_markup=reply_markup2())

@bot.message_handler(commands=['latest'])
def send_message(message):
    bot.send_message(message.chat.id,"Select the Category", reply_markup=reply_markup1())

# bot.remove_webhook()
# bot.polling()

@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://warm-ridge-74785.herokuapp.com/' + bot_token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
