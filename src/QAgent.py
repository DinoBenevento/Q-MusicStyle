class QAgent():

    def __init__(self, instrument):

        self.gamma = 0.75  # Discount factor
        self.alpha = 0.9  # Learning rate
        self.instrument = instrument
        self.Q = [[], [], []]
