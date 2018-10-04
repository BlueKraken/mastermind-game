import constants as CONST

class Game:

  guesses = CONST.INITIAL_GUESSES
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
    return input()
