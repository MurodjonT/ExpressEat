import requests





def telegram_bot_sendtext(bot_message):

	bot_token = '5130152396:AAGiHy6qCBX9Yc8cxEyhsbn1Twzk_pdWL5E'
	bot_chatID = '1129151347'
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode = Markdown&text=' + bot_message
	response = requests.get(send_text)


	return response.json()



# Create your tests here.
