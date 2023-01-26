import telebot

TOKEN = 'insert token here'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    bot.reply_to(message, "Line 2?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.infinity_polling()
