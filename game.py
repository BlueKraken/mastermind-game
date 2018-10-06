from random import randrange
from functools import reduce
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

  # hacer utilizando TDD? está peluoo :C
  # o pensamiento más lógico, menos apegado a la implementación.
  # Estoy cegado por los ciclos
  def checkCurrentGuess(self):
    if self.guesses == 0:
      self.endGame()
    
    hits = list(map(lambda x: False, range(self.codeLenght)))
    concurrencies = hits.copy()

    for index in range(self.codeLenght):
      if self.currentGuess[index] == self.secretCode[index]:
        hits[index] = True

      else:
        # FIXME: be more declarative
        existsInCode = False
        for secretColor in self.secretCode:
          if self.currentGuess[index] == secretColor:
            existsInCode = True
        
        if existsInCode and hits[index] == False and concurrencies[index] == False:
          concurrencies[index] = True

    hitsQuantity = countTrue(hits)
    concurrenciesQuantity = countTrue(concurrencies)

    if hitsQuantity == self.codeLenght:
      print('CONTRATULATIONS YOU WON!')
      self.endGame()

    else:
      print('-----------------')
      print('number of hits: ' + str(hitsQuantity))
      print('number of concurrencies: ' + str(concurrenciesQuantity))
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

    self.endGame()

  def recieveGuessFromUser(self):
    print('Enter a %d digit code: ' % (self.codeLenght))
    self.guesses -= 1

    #TODO: catch non valid input error and ask again
    self.currentGuess = self.parseGuessInput(input())

  def parseGuessInput(self, userInput):
    userInput = userInput.strip()

    return list(map(lambda x: int(x), userInput))

def countTrue(collection):
  return reduce(lambda acc, curr: acc + 1 if curr else acc, collection, 0)
