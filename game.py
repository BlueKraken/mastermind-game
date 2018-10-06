from random import randrange
from constants import INITIAL_GUESSES, COLORS, CODE_LENGTH, DEBUG_MODE, PROD_MODE

class Game:

  guesses = INITIAL_GUESSES
  currentGuess = []
  secretCode = []
  codeLenght = 0
  mode = ''

  def __init__(self, codeLength = CODE_LENGTH, mode = PROD_MODE):
    self.codeLenght = codeLength
    self.mode = mode

    self.generateSecretCode()
    self.gameStart()

  def generateSecretCode(self):
    print('Generating secret code')
    self.secretCode = []
    for _ in range(self.codeLenght):
      self.secretCode.append(randrange(len(COLORS)))

    message = 'Code generated!'

    if self.mode == DEBUG_MODE:
      message += ' code: ' + str(self.secretCode)

    print(message)

  def checkCurrentGuess(self):
    if self.guesses == 0:
      self.endGame()
    
    hits = 0
    concurrencies = 0

    for index in range(self.codeLenght):
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

    if hits == self.codeLenght:
      print('CONTRATULATIONS YOU WON!')
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
    print('GO!')

    while self.guesses > 0 :
      self.recieveGuessFromUser()
      self.checkCurrentGuess()    

  def recieveGuessFromUser(self):
    print('Enter a %d digit code: ' % (self.codeLenght))
    self.guesses -= 1

    #TODO: must be able to provide the full sequence in one line
    for _ in range(self.codeLenght):
      self.currentGuess.append(int(input()))