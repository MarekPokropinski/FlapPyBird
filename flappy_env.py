from gym import Env
from gym.spaces import Box, Discrete
import flappy
from flappy import mainGame, main
import pygame

# OBS_SIZE = (72, 100)
OBS_SIZE = (64, 64)

class FlappyEnv(Env):
    def __init__(self):
        super().__init__()
        self.action_space = Discrete(2)
        self.observation_space = Box(0, 1, shape=(*OBS_SIZE, 3))
        self.flappy_game = None
        self.surface = pygame.Surface(OBS_SIZE)
        main()

    def step(self, action):
        screen, reward, done = self.flappy_game.send(action)
        return self.getState(screen), reward, done, {}

    def render(self, mode='human', close=False):
        flappy.render()

    def reset(self):
        self.flappy_game = mainGame()
        screen, _, _ = next(self.flappy_game)
        return self.getState(screen)

    def getState(self, screen):
        rect = pygame.Rect(54, 2, 288-54, 400)
        sub = screen.subsurface(rect)
        scaled = pygame.transform.scale(sub, OBS_SIZE, self.surface)
        pixels = pygame.surfarray.pixels3d(self.surface).copy()
        obs = pixels/255
        return obs