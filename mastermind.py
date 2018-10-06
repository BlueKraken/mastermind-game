from game import Game
from constants import DEBUG_MODE, PROD_MODE

print('***********************************')
print('WELCOME TO THE MASTERMIND GAME v0.1')
print('***********************************')

print('repo: https://github.com/BlueKraken/mastermind-game\n')

print('To exit at any point use "ctr + z" and hit enter\n')

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