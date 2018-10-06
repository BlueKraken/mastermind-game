from game import Game
from constants import DEBUG_MODE, PROD_MODE

print('***********************************')
print('WELCOME TO THE MASTERMIND GAME v0.1')
print('***********************************')

print('repo: https://github.com/BlueKraken/mastermind-game\n')

print('To exit at any point use "ctr + z" and hit enter\n')

print('-------------')
print('Instructions:')
print('-------------')
print(
  'Mastermind is a code-breaking game. The secret code\n'
  'is a number with only digits from 0 to 5, like:\n' +
  #TODO: make configurable dificulty
  '\n2243\n' + 
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

print('Before we start, let\'s configure your game:\n')

print('1. Do you want to see the code at the start of the game for testing purposes? (y/n)')
mode = ''
while mode != PROD_MODE and mode != DEBUG_MODE:
  showSecretInput = input()
  if showSecretInput != 'y' and showSecretInput != 'n':
    print('Enter a valid response ("y" for yes, or "n" for no)')
  else: 
    mode = DEBUG_MODE if showSecretInput == 'y' else PROD_MODE

print('2. Enter the length desired for the secret code (default is 4, minimum is 3):')
codeLength = 0
while codeLength < 2:
  try:
    codeLength = int(input())
  except ValueError:
    print('Enter a valid length')

print('\nGame configured as follows:')
print('mode: ' + mode)
print('code length: ' + str(codeLength) + '\n')

print('press enter to start')
input()

Game(codeLength, mode)