from telegram.ext import Updater, CommandHandler
from engine import get_random_quote
from environment_variables import get_env

# Your bot token (from BotFather)
TOKEN = get_env("ACCESS_TOKEN")
PORT = get_env('PORT')

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=("Hi %s. Send me /quote command to get a random quote from "
														  "me!" %
														  update.message.from_user.name))

def quote(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=get_random_quote())

def main():
	updater = Updater(TOKEN);
	dp = updater.dispatcher

	# Define all the commands that the bot will receive
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("foilar", quote))

	# Start the bot
	updater.start_polling()
	print("================================")
	print("========= Bot Running ==========")
	print("================================")
	# Start the Bot
	
	updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
	updater.bot.setWebhook('https://testforf.herokuapp.com/' + TOKEN)
	updater.idle()


if __name__ == "__main__":
	main()
