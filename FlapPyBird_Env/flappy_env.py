from gym import Env
from gym.spaces import Box, Discrete
from FlapPyBird_Env.flappy import mainGame, main, render, showScore
import pygame

class FlappyEnv(Env):
    def __init__(self, obs_size= (64, 64)):
        super().__init__()
        self.action_space = Discrete(2)
        self.observation_space = Box(0, 1, shape=(*obs_size, 3))
        self.flappy_game = None
        self.surface = pygame.Surface(obs_size)
        self.screen = None
        self.obs_size = obs_size
        main()

    def step(self, action):
        screen, reward, done = self.flappy_game.send(action)
        self.screen = screen
        return self.getState(screen), reward, done, {}

    def render(self, mode='human', close=False):
        if mode =='human':
            render()
        else:
            showScore()
            rotated = pygame.transform.rotate(self.screen, 90)
            flipped = pygame.transform.flip(rotated, False, True)
            pixels = pygame.surfarray.pixels3d(flipped).copy()
            return pixels

    def reset(self):
        self.flappy_game = mainGame()
        screen, _, _ = next(self.flappy_game)
        return self.getState(screen)

    def getState(self, screen):
        rect = pygame.Rect(54, 2, 288-54, 400)
        sub = screen.subsurface(rect)
        self.surface = sub
        pixels = pygame.surfarray.pixels3d(self.surface).copy()
        return pixels