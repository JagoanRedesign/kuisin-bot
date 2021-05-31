import telebot

# Create bot
bot = telebot.TeleBot('1895994173:AAEOIlOIpYt-8sx5SVu_-cp0smhkVfRO668')

@bot.message_handler(commands=['start'])
def display_welcome_msg(message):
    bot.reply_to(
        message, 'Hai, perkenalkan namaku KuisIn Bot. Aku adalah bot untuk bermain kuis'
    )

bot.polling()