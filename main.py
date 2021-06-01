import telebot
from controller.play_controller import PlayController

class Main:
  bot_token = '1895994173:AAEOIlOIpYt-8sx5SVu_-cp0smhkVfRO668'

  def __init__(self):
    super().__init__()
    
  def main(self):
    # Create bot
    bot = telebot.TeleBot(self.bot_token)
    
    # Controllers
    play_controller = PlayController()
 
    # Message Handlers
    # Start message
    @bot.message_handler(commands=['start'])
    def display_welcome_msg(message):
      bot.reply_to(
        message, 
        'Hai, perkenalkan namaku KuisIn Bot. Aku adalah bot untuk bermain kuis pengetahuan umum. Ketik /play untuk bermain'
      )

    # Play
    @bot.message_handler(commands=['play'])
    def play(message):
      chat_id = message.chat.id
      question = play_controller.get_question()

      bot.send_message(chat_id, question)

    bot.polling()

main = Main()
main.main()