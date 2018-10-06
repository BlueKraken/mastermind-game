import unittest
from game import Game
from functools import reduce

class MyTests(unittest.TestCase):
  def test_checkCurrentGuess(self):
    game = Game()
    
    game.secretCode =   [1,2,3,3]
    game.currentGuess = [3,3,2,1]

    feedback = game.checkCurrentGuess()    
    self.assertEqual(feedback['hits'], 0)
    self.assertEqual(feedback['concurrencies'], 4)
unittest.main()