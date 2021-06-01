import random
from database.dao import Dao

class PlayController:
  dao = Dao()
  quest_id_list = []

  def __init__(self):
    super().__init__()

  def random_quest_id(self, questions_len):
    id = random.randint(1, questions_len)

    if len(self.quest_id_list) > 0:
      i = 0
      while i < len(self.quest_id_list):
        if id == self.quest_id_list[i]:
          id = random.randint(1, questions_len)
          i = 0
        else:
          i += 1
    
    # Add question id to quest_id_list
    self.quest_id_list.append(id)

    return id

  def get_question(self):
    questions_len = self.dao.get_questions_length()

    # Random question id
    quest_id = self.random_quest_id(questions_len)

    return self.dao.get_question(quest_id)

  def clear_quest_id_list(self):
    self.quest_id_list.clear()

  def get_correct_answer(self, quest_id):
    return self.dao.get_correct_answer(quest_id)