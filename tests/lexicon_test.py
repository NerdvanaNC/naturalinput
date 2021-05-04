from naturalinput.lexicon import Lexicon

def test_direction():
  lexicon = Lexicon()
  assert lexicon.scan("north") == ("direction", "north")