from random import randrange
from constants import INITIAL_GUESSES, COLORS, CODE_LENGTH

class Game:

  guesses = INITIAL_GUESSES
  currentGuess = []
  secretCode = []

  def __init__(self):
    self.gameStart()

  def generateSecretCode(self, length = CODE_LENGTH):
    self.secretCode = []
    for _ in range(4):
      print(_)
      self.secretCode.append(randrange(len(COLORS)))

  def checkCurrentGuess(self):
    if self.guesses == 0:
      self.endGame()
    
    hits = 0
    for index in range(CODE_LENGTH):
      if self.currentGuess[index] == self.secretCode[index]:
        hits += 1

    print('-----------------')
    print('number of hits:' + str(hits))
    print('-----------------')

    if hits == 4:
      print('CONTRATULATIONS!')
      self.endGame()

    self.currentGuess = []

  def endGame(self):
    self.guesses = 0
    print('SECRET CODE WAS ' + str(self.secretCode))
    print('GAME OVER')

  def gameStart(self):
    self.generateSecretCode(5)
    print(self.secretCode)

    while self.guesses > 0 :
      self.recieveGuessFromUser()
      self.checkCurrentGuess()    

  def recieveGuessFromUser(self):
    print('Enter code:')
    self.guesses -= 1

    for _ in range(CODE_LENGTH):
      color = int(input())

      if color == -1:
        self.endGame()
        return

      self.currentGuess.append(color)

