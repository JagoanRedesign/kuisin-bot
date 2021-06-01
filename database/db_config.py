import mysql.connector

class DbConfig:
  def __init__(self):
    super().__init__()

  def get_db(self):
    db = mysql.connector.connect(
      host='localhost',
      user='root',
      password='',
      database='kuisin'
    )

    return db