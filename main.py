import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.bot import log
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)
import telebot
import time
import os
import requests
from flask import Flask, request
from bs4 import BeautifulSoup
# server = Flask(__name__)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

LATEST, TRENDING = range(2)
git_acc = "https://github.com/maheshthedev"
linkin = "https://www.linkedin.com/in/maheshthedev/"
ggsearch = "https://www.google.com/search?q=maheshthedev"
sm_links = "<a href=\""+git_acc+"\">"+"GitHub"+"</a>"
sm_links += " · " + "<a href=\""+linkin+"\">"+"LinkedIn"+"</a>"
sm_links += " - " + "<a href=\""+ggsearch+"\">"+"MaheshtheDev"+"</a>"

pageds = requests.get("https://towardsdatascience.com/data-science/home")
soup1 = BeautifulSoup(pageds.content, 'html.parser')
t2 = soup1.find_all(
    class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
lds = []
for i in soup1.find_all('a', href=True):
    lds.append(i['href'])

pageml = requests.get("https://towardsdatascience.com/machine-learning/home")
soup2 = BeautifulSoup(pageml.content, 'html.parser')
t3 = soup2.find_all(
    class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
lml = []
for i in soup2.find_all('a', href=True):
    lml.append(i['href'])

pageviz = requests.get(
    "https://towardsdatascience.com/data-visualization/home")
soup3 = BeautifulSoup(pageviz.content, 'html.parser')
t4 = soup3.find_all(
    class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
lviz = []
for i in soup3.find_all('a', href=True):
    lviz.append(i['href'])

pageai = requests.get(
    "https://towardsdatascience.com/artificial-intelligence/home")
soup4 = BeautifulSoup(pageai.content, 'html.parser')
t5 = soup4.find_all(
    class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
lai = []
for i in soup3.find_all('a', href=True):
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
    new_linksdsl += "\n" + str(i+1) + ". <a href=\"" + \
        linksds[i]+"\">"+art_nameds[i]+"</a>"
new_linksmll = "<b>"+headingmll+"</b>"
for i in range(5):
    new_linksmll += "\n" + str(i+1) + ". <a href=\"" + \
        linksml[i]+"\">"+art_nameml[i]+"</a>"
new_linksvizl = "<b>"+headingvizl+"</b>"
for i in range(5):
    new_linksvizl += "\n" + str(i+1) + ". <a href=\"" + \
        linksviz[i]+"\">"+art_nameviz[i]+"</a>"
new_linksail = "<b>"+headingail+"</b>"
for i in range(5):
    new_linksail += "\n" + str(i+1) + ". <a href=\"" + \
        linksai[i]+"\">"+art_nameai[i]+"</a>"

lat_linksdst = "<b>"+headingdst+"</b>"
for i in range(5, 11):
    lat_linksdst += "\n" + str(i-4) + ". <a href=\"" + \
        linksds[i]+"\">"+art_nameds[i]+"</a>"
lat_linksmlt = "<b>"+headingmlt+"</b>"
for i in range(5, 11):
    lat_linksmlt += "\n" + str(i-4) + ". <a href=\"" + \
        linksml[i]+"\">"+art_nameml[i]+"</a>"
lat_linksvizt = "<b>"+headingvizt+"</b>"
for i in range(5, 11):
    lat_linksvizt += "\n" + str(i-4) + ". <a href=\"" + \
        linksviz[i]+"\">"+art_nameviz[i]+"</a>"
lat_linksait = "<b>"+headingait+"</b>"
for i in range(5, 11):
    lat_linksait += "\n" + str(i-4) + ". <a href=\"" + \
        linksai[i]+"\">"+art_nameai[i]+"</a>"

latestBackNavigation = InlineKeyboardMarkup([[InlineKeyboardButton(
    "« Back", callback_data='latest'), InlineKeyboardButton("✗ Exit", callback_data='exit')]])
trendBackNavigation = InlineKeyboardMarkup([[InlineKeyboardButton(
    "« Back", callback_data='trend'), InlineKeyboardButton("✗ Exit", callback_data='exit')]])


def start(update: Update, _: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    update.message.reply_markdown_v2(
        fr'Welcome {user.mention_markdown_v2()}\!',
        reply_markup=ReplyKeyboardRemove()
    )
    update.message.reply_html(
        'I can get you the Latest and Trending articles on Various Data Science Modules ',
    )
    update.message.reply_html(
        'Use /latest for Latest Articles \nUse /trend for Trending Articles \nUse /dev for Developer Info',
    )
    # Tell ConversationHandler that we're in state `LATEST` now
    return LATEST


def latest(update: Update, _: CallbackContext) -> int:
    """This Command will return list of Categories available in Latest Section"""
    query = update.callback_query
    logger.info("User Requested Latest Command")
    keyboard = [
        [
            InlineKeyboardButton("Data Science", callback_data='dsl'),
        ],
        [
            InlineKeyboardButton("Machine Learning", callback_data='mll'),
        ],
        [
            InlineKeyboardButton("Data Visualization", callback_data='dvl'),
        ],
        [
            InlineKeyboardButton("Artificial Intelligence",
                                 callback_data='ail'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query is None:
        update.message.reply_text(
            "Select the Category", reply_markup=reply_markup)
    else:
        logger.info("user get back to list")
        query.answer()
        query.edit_message_text("Select the Category",
                                reply_markup=reply_markup)
    return LATEST


def trending(update: Update, _: CallbackContext) -> int:
    """This Command will return list of Categories available in Trending Section"""
    logger.info("User Requested the Trend Command")
    keyboard = [
        [
            InlineKeyboardButton("Data Science", callback_data='dst'),
        ],
        [
            InlineKeyboardButton("Machine Learning", callback_data='mlt'),
        ],
        [
            InlineKeyboardButton("Data Visualization", callback_data='dvt'),
        ],
        [
            InlineKeyboardButton("Artificial Intelligence",
                                 callback_data='ait'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Select the Category", reply_markup=reply_markup)
    return TRENDING


def ds(update: Update, _: CallbackContext) -> int:
    """Show all `Latest` or `Trending` Articles on Data Science"""
    query = update.callback_query
    logger.info("User requested %s", _)
    query.answer()
    if query.data == 'dsl':
        logger.info("User requested Latest Data Science Articles")
        query.edit_message_text(
            new_linksdsl, parse_mode='HTML', reply_markup=latestBackNavigation)
        return LATEST
    else:
        logger.info("User requested Trending Data Science Articles")
        query.edit_message_text(
            lat_linksdst, parse_mode='HTML', reply_markup=trendBackNavigation)
        return TRENDING


def ml(update: Update, _: CallbackContext) -> int:
    """Show all `Latest` or `Trending` Articles on Machine Learning"""
    query = update.callback_query
    query.answer()
    if query.data == 'mll':
        logger.info("User requested Latest Machine Learning Articles")
        query.edit_message_text(
            new_linksmll, parse_mode='HTML', reply_markup=latestBackNavigation)
        return LATEST
    else:
        query.edit_message_text(
            lat_linksmlt, parse_mode='HTML', reply_markup=trendBackNavigation)
        return TRENDING


def dv(update: Update, _: CallbackContext) -> int:
    """Show all `Latest` or `Trending` Articles on Machine Learning"""
    query = update.callback_query
    query.answer()
    if query.data == 'dvl':
        logger.info("User requested Latest Data Vizualization Articles")
        query.edit_message_text(
            new_linksvizl, parse_mode='HTML', reply_markup=latestBackNavigation)
        return LATEST
    else:
        logger.info("User requested Trending Data Vizualization Articles")
        query.edit_message_text(
            lat_linksvizt, parse_mode='HTML', reply_markup=trendBackNavigation)
        return TRENDING


def ai(update: Update, _: CallbackContext) -> int:
    """Show all `Latest` or `Trending` Articles on Artifical Intelligence"""
    query = update.callback_query
    query.answer()
    if query.data == 'ail':
        logger.info("User requested Latest Aritifical Intelligence Articles")
        query.edit_message_text(
            new_linksail, parse_mode='HTML', reply_markup=latestBackNavigation)
        return LATEST
    else:
        logger.info("User requested Trending Aritifical Intelligence Articles")
        query.edit_message_text(
            lat_linksait, parse_mode='HTML', reply_markup=trendBackNavigation)
        return TRENDING


def dev(update: Update, _: CallbackContext) -> int:
    """This is Display the Developer Information"""
    update.message.reply_html(
        "I'm made by S v Mahesh Reddy.\nYou can Connect with my Developer!",
    )
    update.message.reply_html(sm_links)
    return ConversationHandler.END


def exit(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text("Thanks for Checking the Articles")
    return ConversationHandler.END


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("1011166147:AAFP_n_ZATGiGIsCu3M8R4gBo-Vb3YMHtCM")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states Latest and Trending
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start), CommandHandler(
            'latest', latest), CommandHandler('trending', trending), CommandHandler('dev', dev)],
        states={
            LATEST: [
                CallbackQueryHandler(ds, pattern='^' + 'dsl' + '$'),
                CallbackQueryHandler(ml, pattern='^' + 'mll' + '$'),
                CallbackQueryHandler(dv, pattern='^' + 'dvl' + '$'),
                CallbackQueryHandler(ai, pattern='^' + 'ail' + '$'),
                CallbackQueryHandler(latest, pattern='^' + 'latest' + '$'),
                CallbackQueryHandler(exit, pattern='^' + 'exit' + '$'),
            ],
            TRENDING: [
                CallbackQueryHandler(ds, pattern='^' + 'dst' + '$'),
                CallbackQueryHandler(ml, pattern='^' + 'mlt' + '$'),
                CallbackQueryHandler(dv, pattern='^' + 'dvt' + '$'),
                CallbackQueryHandler(ai, pattern='^' + 'ait' + '$'),
                CallbackQueryHandler(trending, pattern='^' + 'trend' + '$')
            ]
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
