from random import choice

class Coin:
    def __init__(self, states=['H','T']):
        self.states = states
        self.face = 'H'

    def flip(self):
        return choice(self.states)

