from telegram.ext import Updater, CommandHandler
from engine import get_random_quote
import os


# Your bot token (from BotFather)
TOKEN = os.environ.get("ACCESS_TOKEN")
PORT = int(os.environ.get('PORT', 5000))
GOOGLE_ID = os.environ.get("GOOGLE_ID")


def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=("привет %s. Набирай /foilar и лови мудрость!"
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
	
	file7 = drive.CreateFile({'id': GOOGLE_ID})
	content = file7.GetContentString()
	print(content)
	print("================================")
	print("========= Bot Running ==========")
	print("================================")
	# Start the Bot
	
	updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
	updater.bot.setWebhook('https://testforf.herokuapp.com/' + TOKEN)
	updater.idle()


if __name__ == "__main__":
	main()
