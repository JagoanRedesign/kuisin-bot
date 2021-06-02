import mysql.connector
from database.db_config import DbConfig
from model.question import Question
from model.answer import Answer

class Dao:
  db = DbConfig().get_db()
  cursor = db.cursor()

  def __init__(self):
    super().__init__()

  def get_questions_length(self):
    try:
      query = "SELECT * FROM question"
      self.cursor.execute(query)

      result = self.cursor.fetchall()

      return len(result)
    except Exception as e:
      print(e)

  def get_question(self, id):
    try:
      self.cursor.execute("SELECT * FROM question WHERE id=" + str(id))
      result = self.cursor.fetchone()

      question = Question(
          result[0],
          result[1],
          result[2]
        )

      return question
    except Exception as e:
      print(e)

  def get_correct_answer(self, quest_id):
    try:
      # Get answer id
      self.cursor.execute("SELECT answer FROM correct_answer WHERE question=" + str(quest_id))
      result_id = self.cursor.fetchone()

      # Get answer
      self.cursor.execute("SELECT * FROM answer WHERE id=" + str(result_id[0]))
      result_answer = self.cursor.fetchone()

      answer = Answer(
        result_answer[0],
        result_answer[1]
      )

      return answer
    except Exception as e:
      print(e)