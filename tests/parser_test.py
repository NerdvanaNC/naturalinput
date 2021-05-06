from naturalinput.lexicon import Lexicon
from naturalinput.parser import Sentence

def test_parser_no_subject():
  lexicon = Lexicon()
  sentence = Sentence()

  test_sentence = lexicon.scan("run north")
  sentence.parse(test_sentence)
  
  assert sentence.subject == "player"
  assert sentence.verb == "run"
  assert sentence.object == "north"

def test_parser_with_subject():
  lexicon = Lexicon()
  sentence = Sentence()

  test_sentence = lexicon.scan("bear eat princess")
  sentence.parse(test_sentence)

  assert test_sentence == [("noun", "bear"), ("verb", "eat"), ("noun", "princess")]
  assert sentence.subject == "bear"
  assert sentence.verb == "eat"
  assert sentence.object == "princess"