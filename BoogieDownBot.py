# -*- coding: utf-8 -*-
import os
import logging
import textwrap
import random
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters 
import webscrap
import download
import thumbnail_scrape

TOKEN = os.environ['TOKEN']
updater = Updater(TOKEN)

APP_URL = os.environ['APP_URL']
PORT = int(os.environ.get('PORT', '8443'))
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
	intro_message = textwrap.dedent("""
	Welcome to BoogieDownBot! This chatbot will give you the top 5 tracks on the www.clubdancemixes.com website.
	Hit /tracks to get the tracks, and use the download commands to download them. Hit /search to find a track.
	""")
	bot.sendMessage(chat_id=update.message.chat_id, text=intro_message, parse_mode='markdown')

def tracks(bot, update):
	tracksFound = webscrap.song_scrape()
	bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
	bot.sendMessage(chat_id=update.message.chat_id, text=tracksFound, parse_mode='markdown')    
	
def download1(bot,update):
	thumbnail = thumbnail_scrape.getThumbnail(0)
	link=download.download_track(0)
	bot.send_chat_action(chat_id=update.message.chat_id, action="typing")   
	bot.sendAudio(chat_id=update.message.chat_id,audio=link, thumb=thumbnail)

def download2(bot,update):
	thumbnail = thumbnail_scrape.getThumbnail(1)
	link=download.download_track(1)
	bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
	bot.sendAudio(chat_id=update.message.chat_id,audio=link, thumb=thumbnail)

def download3(bot,update):
	thumbnail = thumbnail_scrape.getThumbnail(2)
	link=download.download_track(2)
	bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
	bot.sendAudio(chat_id=update.message.chat_id,audio=link, thumb=thumbnail)

def download4(bot,update):
	thumbnail = thumbnail_scrape.getThumbnail(3)
	link=download.download_track(3)
	bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
	bot.sendAudio(chat_id=update.message.chat_id,audio=link, thumb=thumbnail)

def download5(bot,update):
	thumbnail = thumbnail_scrape.getThumbnail(4)
	link=download.download_track(4)
	bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
	bot.sendAudio(chat_id=update.message.chat_id,audio=link, thumb=thumbnail)

def search(bot,update):
	bot.send_chat_action(chat_id = update.message.chat_id, action = 'typing')
	message_text = textwrap.dedent("Enter the name of the song to be searched")
	bot.sendMessage(chat_id=update.message.chat_id, text=message_text, parse_mode='markdown')
	updates = bot.get_updates()
	url = 'https://www.clubdancemixes.com/?s={updates}'
	tracksFound = webscrap.song_scrape(url) 
	bot.sendMessage(chat_id=update.message.chat_id, text=tracksFound, parse_mode='markdown')   


def unknown(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="I don't know how to answer to that.")

def main():
	"""Start the bot and use webhook to detect and respond to new messages."""
	dispatcher = updater.dispatcher
	# Handlers
	start_handler = CommandHandler('start', start)
	tracks_handler = CommandHandler('tracks', tracks)
	download1_handler=CommandHandler('download1',download1)
	download2_handler=CommandHandler('download2',download2)
	download3_handler=CommandHandler('download3',download3)
	download4_handler=CommandHandler('download4',download4)
	download5_handler=CommandHandler('download5',download5)
	search_handler=CommandHandler('search',search)
	unknown_message = MessageHandler(Filters.text | Filters.command, unknown)

	# Dispatchers
	dispatcher.add_handler(start_handler)
	dispatcher.add_handler(tracks_handler)
	dispatcher.add_handler(download1_handler)
	dispatcher.add_handler(download2_handler)
	dispatcher.add_handler(download3_handler)
	dispatcher.add_handler(download4_handler)
	dispatcher.add_handler(download5_handler)
	dispatcher.add_handler(search_handler)
	dispatcher.add_handler(unknown_message)

	updater.start_webhook(listen='0.0.0.0',
	  port=PORT,
	  url_path=TOKEN)
	updater.bot.set_webhook(APP_URL + TOKEN)
	updater.idle()

if __name__ == '__main__':
	main()
