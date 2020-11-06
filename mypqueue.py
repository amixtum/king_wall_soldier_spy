class PriorityQueue(object):
  def __init__(self):
    self.q = []
  
  def enqueue(self, key, value):
    self.q.append((key, value))
    self.q.sort(key=lambda x : x[0])
  
  def dequeue(self):
    return self.q.pop(0)[1]

  def change_key(self, value, new_key):
    for index in range(len(self.q)):
      if self.q[index][1] == value:
        self.q[index] = (new_key, value)
        self.q.sort(key=lambda x : x[0])

  def __len__(self):
    return len(self.q)