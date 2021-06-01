class Answer:
  def __init__(self, id=0, text=''):
    self._id = id
    self._text = text

  def set_id(self, id):
    self._id = id

  def get_id(self):
    return self._id

  def set_text(self, text):
    self._text = text

  def get_text(self):
    return self._text