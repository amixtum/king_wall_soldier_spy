class Vertex(object):
  def __init__(self, value):
    self.value = value
    self.previsit_function = None
    self.postvisit_function = None

  def previsit(self):
    if self.previsit_function is not None:
      self.previsit_function()

  def postvisit(self):
    if self.postvisit_function is not None:
      self.postvisit_function()
  
  def set_previsit(self, fn):
    self.previsit_function = fn
    
  def set_postvisit(self, fn):
    self.postvisit_function = fn
  
  def __str__(self):
    return str(self.value)

  def __eq__(self, other):
    return self is other

  def __hash__(self): # hack!!
    return 0