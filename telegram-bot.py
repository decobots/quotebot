import google.oauth2.credentials
import google_auth_oauthlib.flow

from telegram.ext import Updater, CommandHandler
from engine import get_random_quote
import os




# Your bot token (from BotFather)
TOKEN = os.environ.get("ACCESS_TOKEN")
PORT = int(os.environ.get('PORT', 5000))


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# The ID of a sample document.
DOCUMENT_ID = os.environ.get("GOOGLE_ID")






def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=("привет %s. Набирай /foilar и лови мудрость!"
														  "me!" %
														  update.message.from_user.name))

def quote(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=get_random_quote())

def main():
	flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
	'credentials.json',
	scopes=SCOPES)
	flow.redirect_uri = 'http://localhost:35655/'

	
	
	
	updater = Updater(TOKEN);
	dp = updater.dispatcher

	# Define all the commands that the bot will receive
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("foilar", quote))

	# Start the bot
	updater.start_polling()
	

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
