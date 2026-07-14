class NumberGuessAI:

    def __init__(self):
        self.reset()

    def reset(self):
        self.low = 1
        self.high = 100
        self.guess = (self.low + self.high) // 2
        self.attempts = 1

    def get_guess(self):
        return self.guess

    def get_attempts(self):
        return self.attempts

    def too_low(self):
        self.low = self.guess + 1
        self.guess = (self.low + self.high) // 2
        self.attempts += 1

    def too_high(self):
        self.high = self.guess - 1
        self.guess = (self.low + self.high) // 2
        self.attempts += 1