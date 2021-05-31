import mysql.connector
from model.database.db_config import DbConfig

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

      for question in result:
        return question
    except Exception as e:
      print(e)
