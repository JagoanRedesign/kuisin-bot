class Question:
  def __init__(self, id=0, question='', score=0):
    self._id = id
    self._question = question
    self._score = score
  
  def set_id(self, id):
    self._id = id

  def get_id(self):
    return self._id

  def set_question(self, question):
    self._question = question

  def get_question(self):
    return self._question

  def set_score(self, score):
    self._score = score

  def get_score(self):
    return self._score