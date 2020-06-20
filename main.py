import telebot
import time
import os
import requests
from flask import Flask, request
from bs4 import BeautifulSoup
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
bot_token = os.environ.get('TELAPITOKEN')
bot = telebot.TeleBot(token=bot_token)
server = Flask(__name__)

git_acc = "https://github.com/maheshthedev"
linkin = "https://www.linkedin.com/in/maheshthedev/"
gsearch = "https://www.google.com/search?q=maheshthedev"
sm_links = "<a href=\""+git_acc+"\">"+"GitHub"+"</a>"
sm_links +=" · " + "<a href=\""+linkin+"\">"+"LinkedIn"+"</a>"
sm_links +=" - "+ "<a href=\""+gsearch+"\">"+"MaheshtheDev"+"</a>"

pageds=requests.get("https://towardsdatascience.com/data-science/home")
soup1 = BeautifulSoup(pageds.content,'html.parser')
t2 = soup1.find_all(class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
lds = []
for i in soup1.find_all('a',href=True):
    lds.append(i['href'])

pageml=requests.get("https://towardsdatascience.com/machine-learning/home")
soup2 = BeautifulSoup(pageml.content,'html.parser')
t3 = soup2.find_all(class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
lml = []
for i in soup2.find_all('a',href=True):
    lml.append(i['href'])

pageviz=requests.get("https://towardsdatascience.com/data-visualization/home")
soup3 = BeautifulSoup(pageviz.content,'html.parser')
t4 = soup3.find_all(class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
lviz = []
for i in soup3.find_all('a',href=True):
    lviz.append(i['href'])

pageai=requests.get("https://towardsdatascience.com/artificial-intelligence/home")
soup4 = BeautifulSoup(pageai.content,'html.parser')
t5 = soup4.find_all(class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
lai = []
for i in soup3.find_all('a',href=True):
    lai.append(i['href'])
t1 = t2 + t3 + t4 + t5

art_name = []
for i in t1:
    j = list(i)
    j1 = list(j[0])
    art_name.append(j1[0])

art_nameds = art_name[:11]
art_nameml = art_name[11:22]
art_nameviz = art_name[22:33]
art_nameai = art_name[33:]

linksds = lds[13:-8:4]
linksml = lml[13:-8:4]
linksviz = lviz[13:-8:4]
linksai = lai[13:-8:4]

headingdst = "Top Stories in Data Science"
headingdsl = "Latest Articles on Data Science"
headingmlt = "Top Stories in Machine Learning"
headingmll = "Latest Articles on Machine Learning"
headingvizt = "Top Stories in Visualization"
headingvizl = "Latest Articles on Visualization"
headingait = "Top Stories in Artificial Intelligence"
headingail = "Latest Articles on Artificial Intelligence"

new_linksdsl = "<b>"+headingdsl+"</b>"
for i in range(5):
    new_linksdsl += "\n" + str(i+1) +". <a href=\""+linksds[i]+"\">"+art_nameds[i]+"</a>" 
new_linksmll = "<b>"+headingmll+"</b>"
for i in range(5):
    new_linksmll += "\n" + str(i+1) +". <a href=\""+linksml[i]+"\">"+art_nameml[i]+"</a>" 
new_linksvizl = "<b>"+headingvizl+"</b>"
for i in range(5):
    new_linksvizl += "\n" + str(i+1) +". <a href=\""+linksviz[i]+"\">"+art_nameviz[i]+"</a>" 
new_linksail = "<b>"+headingail+"</b>"
for i in range(5):
    new_linksail += "\n" + str(i+1) +". <a href=\""+linksai[i]+"\">"+art_nameai[i]+"</a>" 

lat_linksdst = "<b>"+headingdst+"</b>"
for i in range(5,11):
    lat_linksdst += "\n" + str(i-4) +". <a href=\""+linksds[i]+"\">"+art_nameds[i]+"</a>"
lat_linksmlt = "<b>"+headingmlt+"</b>"
for i in range(5,11):
    lat_linksmlt += "\n" + str(i-4) +". <a href=\""+linksml[i]+"\">"+art_nameml[i]+"</a>"
lat_linksvizt = "<b>"+headingvizt+"</b>"
for i in range(5,11):
    lat_linksvizt += "\n" + str(i-4) +". <a href=\""+linksviz[i]+"\">"+art_nameviz[i]+"</a>"
lat_linksait = "<b>"+headingait+"</b>"
for i in range(5,11):
    lat_linksait += "\n" + str(i-4) +". <a href=\""+linksai[i]+"\">"+art_nameai[i]+"</a>"


hidekeyboard = types.ReplyKeyboardRemove()
def reply_markup1():
    markupl = ReplyKeyboardMarkup()
    markupl.row_width = 1
    item_bt1 = types.KeyboardButton('Data Science (DSl)')
    item_bt2 = types.KeyboardButton('Machine Learning (MLl)')
    item_bt3 = types.KeyboardButton('Data Vizualization (DVl)')
    item_bt4 = types.KeyboardButton('Artificial Intelligence (AIl)')
    markupl.add(item_bt1,item_bt2,item_bt3,item_bt4)
    return markupl

def reply_markup2():
    markupl = ReplyKeyboardMarkup()
    markupl.row_width = 1
    item_bt1 = types.KeyboardButton('Data Science (DSt)')
    item_bt2 = types.KeyboardButton('Machine Learning (MLt)')
    item_bt3 = types.KeyboardButton('Data Vizualization (DVt)')
    item_bt4 = types.KeyboardButton('Artificial Intelligence (AIt)')
    markupl.add(item_bt1,item_bt2,item_bt3,item_bt4)
    return markupl

@bot.message_handler(func=lambda message: message.text in ['Data Science (DSl)','Machine Learning (MLl)','Data Vizualization (DVl)','Artificial Intelligence (AIl)','Data Science (DSt)','Machine Learning (MLt)','Data Vizualization (DVt)','Artificial Intelligence (AIt)'])
def send_message(message):
    bot.send_chat_action(message.chat.id, 'typing')
    if message.text == "Data Science (DSl)":
        bot.send_message(message.chat.id,new_linksdsl,parse_mode='HTML',reply_markup=hidekeyboard)
    if message.text == "Machine Learning (MLl)":
        bot.send_message(message.chat.id,new_linksmll,parse_mode='HTML',reply_markup=hidekeyboard)
    if message.text == "Data Vizualization (DVl)":
        bot.send_message(message.chat.id,new_linksvizl,parse_mode='HTML',reply_markup=hidekeyboard)
    if message.text == "Artificial Intelligence (AIl)":
        bot.send_message(message.chat.id,new_linksail,parse_mode='HTML',reply_markup=hidekeyboard)  
    if message.text == "Data Science (DSt)":
        bot.send_message(message.chat.id,lat_linksdst,parse_mode='HTML',reply_markup=hidekeyboard)        
    if message.text == "Machine Learning (MLt)":
        bot.send_message(message.chat.id,lat_linksmlt,parse_mode='HTML',reply_markup=hidekeyboard)      
    if message.text == "Data Vizualization (DVt)":
        bot.send_message(message.chat.id,lat_linksvizt,parse_mode='HTML',reply_markup=hidekeyboard)
    if message.text == "Artificial Intelligence (AIt)":
        bot.send_message(message.chat.id,lat_linksait,parse_mode='HTML',reply_markup=hidekeyboard)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Welcome, Pal!')
    bot.send_message(message.chat.id, 'Use /latest for Latest Articles \nUse /trend for Trending Articles \nUse /dev for Developer Information')

@bot.message_handler(commands=['dev'])
def send_welcome(message):
    bot.send_message(message.chat.id, "I'm made by S v Mahesh Reddy.\nYou can Connect with my Developer!")
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
