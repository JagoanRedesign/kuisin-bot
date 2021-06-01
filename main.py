import telebot
import time
from controller.play_controller import PlayController

class Main:
  bot = telebot.TeleBot('1895994173:AAEOIlOIpYt-8sx5SVu_-cp0smhkVfRO668')
  question = None
  user_score = 0
  is_correct = False
  
  # Controllers
  play_controller = PlayController()

  def __init__(self):
    super().__init__()
    
  def main(self):
    # Message Handlers
    # Start message
    @self.bot.message_handler(commands=['start'])
    def start(message):
      self.bot.reply_to(
        message, 
        'Hai, perkenalkan namaku KuisIn Bot. Aku adalah bot untuk bermain kuis pengetahuan umum. Ketik /play untuk bermain'
      )

    # Play
    @self.bot.message_handler(commands=['play'])
    def play(message):
      chat_id = message.chat.id
      self.question = None
      self.user_score = 0
      total_question = 3

      for i in range(0, total_question):
        self.is_correct = False

        # Get question
        self.question = self.play_controller.get_question()
        
        # Display question
        self.bot.send_message(
          chat_id, self.question.get_text()
        )

        # Get user answer and check it
        self.bot.register_next_step_handler(message, self.check_user_answer)

        # Set timer
        t = 20
        while t:
          if self.is_correct:
            break

          time.sleep(1)
          t -= 1

          if t == 10:
            self.bot.send_message(
              chat_id, 'Waktu tersisa 10 detik lagi'
            )

        if i == total_question-1:
          self.bot.send_message(
            chat_id, 'Permainan berakhir. Kamu mendapatkan score ' + str(self.user_score)
          )
          self.play_controller.clear_quest_id_list()
          
          return

    self.bot.polling()

  def check_user_answer(self, message):
    user_answer = message.text
    correct_answer = self.play_controller.get_correct_answer(self.question.get_id()).get_text()

    if user_answer.lower() == correct_answer.lower():
      self.user_score += self.question.get_score()
      self.is_correct = True
      

main = Main()
main.main()