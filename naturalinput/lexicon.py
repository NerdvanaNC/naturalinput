class Lexicon(object):
  def __init__(self):
    self.lexicon = {
      "north": "direction",
      "east": "direction",
      "west": "direction",
      "south": "direction",
      "up": "direction",
      "right": "direction",
      "left": "direction",
      "down": "direction",
      "back": "direction",
      "go": "verb",
      "stop": "verb",
      "kill": "verb",
      "eat": "verb",
      "the": "stop",
      "in": "stop",
      "of": "stop",
      "from": "stop",
      "at": "stop",
      "it": "stop",
      "door": "noun",
      "bear": "noun",
      "princess": "noun",
      "cabinet": "noun"
      # numbers can be anything from 0 - 9
      # this exception handled in the scan method
    }

  def scan(self, input):    
    # take input and split by spaces
    words_list = input.lower().split()

    # take resulting list and loop through our lexicon
    # to see which word is which type

    for word in words_list:
      if(self.lexicon[word] != None):
        return (self.lexicon[word], word)


    # numbers either return an int(number) or raise an exception

    # try except int() ? exception > return None 