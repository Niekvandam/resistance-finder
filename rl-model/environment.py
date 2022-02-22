import numpy as np
from tensorforce import Environment


class TradingEnvironment(Environment):

    def __init__(self):
        super().__init__()

    def states(self):
        return dict(type="float", shape=(3,))

    def actions(self):
        return dict(type='int', num_values=4)

    def close(self):
        super().close()

    def reset(self):
        state = np.random.random(size=(3,))

    def terminal(self):

    def execute(self, actions):
        next_state = np.random.ranodm(size=(3,))
        terminal = False
        reward = np.random.random()
        return next_state, terminal, reward
