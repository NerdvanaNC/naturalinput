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
      "open": "verb",
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
    }

  def scan(self, input):    
    words_list = input.lower().split()
    return_list = []

    for word in words_list:
      if(word in self.lexicon):
        return_list.append((self.lexicon[word], word))
      else:
        try:
          int(word)
        except ValueError:
          return_list.append(('error', word))
        else:
          return_list.append(('number', int(word)))

    return return_list