import telebot
import time
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
    def start(message):
      bot.reply_to(
        message, 
        'Hai, perkenalkan namaku KuisIn Bot. Aku adalah bot untuk bermain kuis pengetahuan umum. Ketik /play untuk bermain'
      )

    # Play
    @bot.message_handler(commands=['play'])
    def play(message):
      chat_id = message.chat.id
      total_question = 3

      for i in range(0, total_question+1):
        # Get question and correct answer
        if i != total_question:
          question = play_controller.get_question()
          correct_answer = play_controller.get_correct_answer(question.get_id()).get_text()

        if i > 0:
          t = 5

          # Set timer
          while t:
            time.sleep(1)
            t -= 1

          if i == total_question:
            bot.send_message(
              chat_id, "Yah, waktunya sudah habis"
            )
            play_controller.clear_quest_id_list()

            return

          bot.send_message(
            chat_id, question.get_text()
          )
        else:
          bot.send_message(
            chat_id, question.get_text()
          )

    bot.polling()
    
main = Main()
main.main()