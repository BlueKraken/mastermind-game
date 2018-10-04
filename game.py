from random import randrange
from constants import INITIAL_GUESSES, COLORS

class Game:

  guesses = INITIAL_GUESSES
  currentGuess = []
  secret = []

  def __init__(self):
    self.gameStart()

  def generateSecretCode(self, length = 4):
    self.secretCode = []
    # for _ in range(4):
    #   self.secret.append(randrange(len(COLORS)))
    self.secret = randrange(5)

  def giveFeedback(self):
    if self.guesses == 0:
      self.endGame()

    if self.currentGuess == 'end game' or self.currentGuess == 'end' or self.currentGuess == '-1':
      self.endGame()

  def endGame(self):
    self.guesses = 0
    print('SECRET CODE WAS ' + str(self.secretCode))
    print('GAME OVER')

  def gameStart(self):
    self.secretCode = self.generateSecretCode()
    print(self.secretCode)

    while self.guesses > 0 :
      self.recieveGuessFromUser()
      self.giveFeedback()    

  def recieveGuessFromUser(self):
    print('Enter code:')
    self.guesses -= 1
    self.currentGuess = input()
