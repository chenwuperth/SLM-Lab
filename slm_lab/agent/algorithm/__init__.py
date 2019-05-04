'''
The algorithm module
Contains implementations of reinforcement learning algorithms.
Uses the nets module to build neural networks as the relevant function approximators
'''

# expose all the classes
from .actor_critic import *
from .ddpg import *
from .dqn import *
from .hydra_dqn import *
from .ppo import *
from .random import *
from .reinforce import *
from .sarsa import *
from .sil import *
