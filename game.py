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
    concurrencies = 0

    for index in range(CODE_LENGTH):
      if self.currentGuess[index] == self.secretCode[index]:
        hits += 1
      else:
        # FIXME: be more declarative
        exists = False
        for secretColor in self.secretCode:
          if self.currentGuess[index] == secretColor:
            exists = True
        
        if exists:
          concurrencies += 1

    if hits == CODE_LENGTH:
      print('CONTRATULATIONS!')[0, 0, 3, 1]
      self.endGame()

    else:
      print('-----------------')
      print('number of hits: ' + str(hits))
      print('number of concurrencies: ' + str(concurrencies))
      print('-----------------')

    self.currentGuess = []

  # FIXME: todo must be terminating (to lazily )
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

      self.currentGuess.append(color)

