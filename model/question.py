class Question:
  def __init__(self, id=0, text='', score=0):
    self._id = id
    self._text = text
    self._score = score
  
  def set_id(self, id):
    self._id = id

  def get_id(self):
    return self._id

  def set_text(self, text):
    self._text = text

  def get_text(self):
    return self._text

  def set_score(self, score):
    self._score = score

  def get_score(self):
    return self._score