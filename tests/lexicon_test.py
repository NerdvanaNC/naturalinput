from naturalinput.lexicon import Lexicon

def test_direction():
  lexicon = Lexicon()
  assert lexicon.scan("north") == [("direction", "north")]
  assert lexicon.scan("north south west") == [
    ("direction", "north"),
    ("direction", "south"),
    ("direction", "west")
  ]

def test_verb():
  lexicon = Lexicon()
  assert lexicon.scan("go") == [("verb", "go")]
  assert lexicon.scan("go kill eat") == [
    ("verb", "go"),
    ("verb", "kill"),
    ("verb", "eat")
  ]

def test_stop():
  lexicon = Lexicon()
  assert lexicon.scan("the") == [("stop", "the")]
  assert lexicon.scan("the in from") == [
    ("stop", "the"),
    ("stop", "in"),
    ("stop", "from")
  ]

def test_noun():
  lexicon = Lexicon()
  assert lexicon.scan("door") == [("noun", "door")]
  assert lexicon.scan("bear princess cabinet") == [
    ("noun", "bear"),
    ("noun", "princess"),
    ("noun", "cabinet")
  ]

def test_mixed_words():
  lexicon = Lexicon()
  assert lexicon.scan("go north down kill") == [
    ("verb", "go"),
    ("direction", "north"),
    ("direction", "down"),
    ("verb", "kill")
  ]

def test_numbers():
  lexicon = Lexicon()
  assert lexicon.scan("123 34 3") == [
    ("number", 123),
    ("number", 34),
    ("number", 3)
  ]

def test_errors():
  lexicon = Lexicon()
  assert lexicon.scan("ibn batuta joota") == [
    ("error", 'ibn'),
    ("error", 'batuta'),
    ("error", 'joota')
  ]

def test_mixed_all():
  lexicon = Lexicon()
  assert lexicon.scan("go 3 steps north") == [
    ("verb", "go"),
    ("number", 3),
    ("error", "steps"),
    ("direction", "north")
  ]

  assert lexicon.scan("kill the Bear") == [
    ("verb", "kill"),
    ("stop", "the"),
    ("noun", "bear")
  ]
  
  assert lexicon.scan("open THE cabinet") == [
    ("verb", "open"),
    ("stop", "the"),
    ("noun", "cabinet")
  ]

  assert lexicon.scan("bear ESOTERIC wording") == [
    ("noun", "bear"),
    ("error", "esoteric"),
    ("error", "wording")
  ]