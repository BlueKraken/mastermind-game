from constants import DEBUG_MODE, PROD_MODE, CODE_LENGTH, INITIAL_GUESSES
from game import Game

class Menu:
  mode = PROD_MODE
  codeLength = CODE_LENGTH
  initialGuesses = INITIAL_GUESSES

  def showMenu(self):
    validChoices = [1,2,3]
    choice = 0

    while validChoices.count(choice) == 0:
      print('----------------')
      print('1. Play')
      print('2. Instructions')
      print('3. Configuration')
      print('----------------')

      try:
        choice = int(input('Enter a choice: '))
        if validChoices.count(choice) == 0:
          raise ValueError
      except ValueError:
        print('Enter a valid choice')

      if choice == 1:
        self.startGame()
        self.showMenu()
      elif choice == 2:
        self.showInstructions()
        self.showMenu()
      elif choice == 3:
        self.configureGame()
        self.showConfiguration()
        self.showMenu()

  def startGame(self):
    game = Game(self.codeLength, self.mode, self.initialGuesses)
    game.start()

  def showInstructions(self):
    print('-------------')
    print('Instructions:')
    print('-------------')
    print(
      'Mastermind is a code-breaking game. The secret code\n'
      'is a number with only digits from 0 to 3, like:\n' +
      #TODO: make configurable dificulty
      '\n2203\n' + 
      '\n' +
      'The length of the code is configurable,\n' +
      'but note that normally this type of game \n' +
      'is played with a code of thength 4\n' +
      '\n' + 
      'Each time you guess, the program will give you feedback as follows:\n' +
      '\n'+
      '1. number of hits: number of digits that are in the correct position\n'+
      '2. number of concurrencies: number of digits that are part of the code,\n' +
      '   but are not in the right position\n')

    print('press enter to continue')
    input()

  def configureGame(self):
    self.codeLength = 0
    self.initialGuesses = 0

    print('1. Enter the length desired for the secret code (default is 4, minimum is 3):')
    try:
      self.codeLength = int(input())
      if(self.codeLength < 2):
        raise ValueError
    except ValueError:
      print('Using default')
      self.codeLength = CODE_LENGTH

    print('2. Enter the number of guesses you can make (default is 7, minimum is 3):')
    try:
      self.initialGuesses = int(input())
      if(self.initialGuesses < 2):
        raise ValueError
    except ValueError:
      print('Using default')
      self.initialGuesses = INITIAL_GUESSES

  def showConfiguration(self):
    print('\nGame configured as follows:')
    print('code length: ' + str(self.codeLength))
    print('Guesses: ' + str(self.initialGuesses))

    print('press enter to continue')
    input()