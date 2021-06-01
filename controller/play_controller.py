import random
from database.dao import Dao

class PlayController:
  dao = Dao()
  quest_id_list = [0]

  def __init__(self):
    super().__init__()

  def random_quest_id(self, questions_len):
    id = random.randint(1, questions_len)

    for i in range(0, questions_len):
      if id == self.quest_id_list[i]:
        id = random.randint(1, questions_len)
        i = -1
    
    # Add question id to quest_id_list
    self.quest_id_list.append(id)

    return id

  def get_question(self):
    questions_len = self.dao.get_questions_length()

    # Random question id
    quest_id = self.random_quest_id(questions_len)

    return self.dao.get_question(quest_id)