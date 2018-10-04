from random import randrange
from constants import INITIAL_GUESSES, COLORS, CODE_LENGTH, DEBUG_MODE

class Game:

  guesses = INITIAL_GUESSES
  currentGuess = []
  secretCode = []

  def __init__(self):
    self.gameStart()

  def generateSecretCode(self, length = CODE_LENGTH):
    self.secretCode = []
    for _ in range(CODE_LENGTH):
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
      print('CONTRATULATIONS!')
      self.endGame()

    else:
      print('-----------------')
      print('number of hits: ' + str(hits))
      print('number of concurrencies: ' + str(concurrencies))
      print('-----------------')

    self.currentGuess = []

  def endGame(self):
    self.guesses = 0
    print('SECRET CODE WAS ' + str(self.secretCode))
    print('GAME OVER')

  def gameStart(self):
    self.generateSecretCode(5)

    if DEBUG_MODE:
      print(self.secretCode)

    while self.guesses > 0 :
      self.recieveGuessFromUser()
      self.checkCurrentGuess()    

  def recieveGuessFromUser(self):
    print('Enter %d digit code: ' % (CODE_LENGTH))
    self.guesses -= 1

    #TODO: must be able to provide the full sequence in one line
    for _ in range(CODE_LENGTH):
      self.currentGuess.append(int(input()))

