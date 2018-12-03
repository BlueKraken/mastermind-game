from random import randrange
from functools import reduce
from constants import INITIAL_GUESSES, COLORS, CODE_LENGTH, DEBUG_MODE, PROD_MODE

class Game:

  guesses = 0
  currentGuess = []
  secretCode = []
  codeLenght = 0
  mode = ''

  def __init__(self, codeLength = CODE_LENGTH, mode = PROD_MODE, initialGuesses = INITIAL_GUESSES):
    self.codeLenght = codeLength
    self.mode = mode
    self.guesses = initialGuesses

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
    
    hits = []

    for index in range(len(self.secretCode)):
      if self.secretCode[index] == self.currentGuess[index]:
        hits.append(self.currentGuess[index])

    concurrencies = 0

    for digit in COLORS:
      digitInHit = hits.count(digit)
      
      aviableInSecret = self.secretCode.count(digit) - digitInHit
      digitInGuess = self.currentGuess.count(digit) - digitInHit

      if digitInGuess > 0 and aviableInSecret > 0:
        if digitInGuess == aviableInSecret:
          concurrencies += digitInGuess
          
        elif aviableInSecret > digitInGuess:
          concurrencies += digitInGuess
        else:
          concurrencies += aviableInSecret

    self.currentGuess = []
    return {'hits': len(hits), 'concurrencies': concurrencies}

  def showFeedback(self, hits, concurrencies):
    if hits == self.codeLenght:
      print('CONTRATULATIONS YOU WON!')
      self.endGame()

    else:
      print('-----------------')
      print('number of hits: ' + str(hits))
      print('number of concurrencies: ' + str(concurrencies))
      print('-----------------')

  def endGame(self):
    self.guesses = 0
    print('SECRET CODE WAS ' + str(self.secretCode))
    print('GAME OVER')

  def start(self):
    self.generateSecretCode()

    print('GO!')

    while self.guesses > 0 :
      self.recieveGuessFromUser()
      feedback = self.checkCurrentGuess()
      self.showFeedback(feedback['hits'], feedback['concurrencies'])

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
