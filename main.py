import telebot
from controller.play_controller import PlayController

class Main:
  def __init__(self):
    super().__init__()
    
  def main(self):
    # Create bot
    bot = telebot.TeleBot('1895994173:AAEOIlOIpYt-8sx5SVu_-cp0smhkVfRO668')
 
    # Start message
    @bot.message_handler(commands=['start'])
    def display_welcome_msg(message):
      bot.reply_to(
        message, 'Hai, perkenalkan namaku KuisIn Bot. Aku adalah bot untuk bermain kuis. Ketik /play untuk bermain'
      )

    # Controllers
    play_controller = PlayController()

    # Play
    @bot.message_handler(commands=['play'])
    def play(message):
      play_controller.play()

    bot.polling()

main = Main()
main.main()