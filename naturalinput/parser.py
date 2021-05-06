class Sentence(object):
  def __init__(self):
    self.subject = "player" # the doer of every action; by default this is the player
    self.verb = None # the action taken by the subject
    self.object = None # the thing the action is taken on; or the direction that is actioned
  
  def parse(self, sentence):
    # sentence = [("noun", "bear"), ("verb", "run"), ("direction", "north")]

    for word in sentence:
      if word[0] == "noun" and self.subject == "player":
        self.subject = word[1]
      elif word[0] == "noun" and self.subject != "player":
        self.object = word[1]
      elif word[0] == "verb":
        self.verb = word[1]
      elif word[0] == "direction":
        self.object = word[1]
      elif word[0] == "stop":
        pass
      elif word[0] == "error":
        pass
      else:      
        raise ParserException("Invalid entry.")



class ParserException(Exception):
  def __init__(self, error):
    print(error)