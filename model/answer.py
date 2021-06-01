class Answer:
  def __init__(self, id, answer):
    self._id = id
    self._answer = answer

  def set_id(self, id):
    self._id = id

  def get_id(self):
    return self._id

  def set_answer(self, answer):
    self._answer = answer

  def get_answer(self):
    return self._answer