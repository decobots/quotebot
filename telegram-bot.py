from telegram.ext import Updater, CommandHandler
from engine import get_random_quote
import os


from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

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
	"""Shows basic usage of the Docs API.
	Prints the title of a sample document.
	"""
	creds = None
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.json'):
		creds = Credentials.from_authorized_user_file('token.json', SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
		    creds.refresh(Request())
		else:
		    flow = InstalledAppFlow.from_client_secrets_file(
			'credentials.json', SCOPES)
		    creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.json', 'w') as token:
		    token.write(creds.to_json())

	service = build('docs', 'v1', credentials=creds)

	# Retrieve the documents contents from the Docs service.
	document = service.documents().get(documentId=DOCUMENT_ID).execute()

	print('The title of the document is: {}'.format(document.get('title')))

	
	
	
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
