

from telegram.ext import Updater, CommandHandler
import os
import random

quote_file = "quotes.txt"



# Your bot token (from BotFather)
TOKEN = os.environ.get("ACCESS_TOKEN")
PORT = int(os.environ.get('PORT', 5000))
LINES = []

def get_lines():
	print('getlines')
	with open(quote_file) as file:
		lines = (line for line in file.readlines() if line)
		print(lines)
		return lines

def get_random_quote():
	return random.choice(LINES)

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=("Привет %s! Что сегодня тебе скажет Фойлар? Набирай /foilar" % update.message.from_user.name))

def quote(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=get_random_quote())

def main():
	LINES = get_lines()
	updater = Updater(TOKEN);
	dp = updater.dispatcher

	# Define all the commands that the bot will receive
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("foilar", quote))

	
	


	updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
	updater.bot.setWebhook('https://testforf.herokuapp.com/' + TOKEN)
	
	# Start the bot
	updater.start_polling()	
	print("================================")
	print("========= Bot Running ==========")
	print("================================")
	# Start the Bot
	
	updater.idle()


if __name__ == "__main__":
	main()
