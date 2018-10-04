GREEN = 'GREEN'
BLUE = 'BLUE'
YELLOW = 'YELLOW'
RED = 'RED'

INITIAL_GUESSES = 5

class Game:

  guesses = INITIAL_GUESSES
  currentGuess = []

  def __init__(self):
    self.guess = []
    self.gameStart()

  def generateSecretCode(self, length = 4):
    return []

  def giveFeedback(self, colors):
    if self.guesses == 0:
      self.endGame()

  def endGame(self):
    return

  def gameStart(self):

    self.secretCode = self.generateSecretCode()

    while self.guesses > 0 :
      self.guess = self.recieveGuessFromUser()
      self.giveFeedback(self)

    print('GAME OVER')

  def recieveGuessFromUser(self):
    print('Enter code')
    self.guesses -= 1
    return []

def gamePyTest():
  Game()

gamePyTest()