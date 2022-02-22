from os import environ
from tensorforce.agents import Agent
from tensorforce.environments import Environment
from environment import TradingEnvironment
from tensorforce.execution import Runner


class TradingModel:
    def __init__(self):
        self.balance = 10000
