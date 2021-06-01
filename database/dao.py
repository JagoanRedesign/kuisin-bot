import mysql.connector
from database.db_config import DbConfig
from model.question import Question

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
      query = "SELECT * FROM question WHERE id=" + str(id)
      self.cursor.execute(query)

      result = self.cursor.fetchall()

      for item in result:
        question = Question(
          item[0],
          item[1],
          item[2]
        )
        
        return question.get_question()
    except Exception as e:
      print(e)
