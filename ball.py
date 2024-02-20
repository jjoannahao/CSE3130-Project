"""
title: box class for ball
author: joanna hao
date-created: 2024-02-05
"""
from my_sprite import Box
import pygame


class Ball(Box):
    """
    creates the ball class, which player will bounce and which will hit bricks
    """
    def __init__(self, WIDTH=1, HEIGHT=1):
        Box.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOUR)
        self.__HIT_BOX = Box(self.getWidth()//2, self.getHeight()//2)
        self.__HIT_BOX.setPOS(
            self.getX() + self.getWidth() // 2 - self.__HIT_BOX.getWidth() // 2,
            self.getY() + self.getHeight() // 2 - self.__HIT_BOX.getHeight() // 2
        )
        if self.getDirX() == 1:
            self.__GOING_RIGHT = True
        else:
            self.__GOING_RIGHT = False

    # --- modifiers --- #
    def bounceX(self, MAX_X, MIN_X=0):
        self.setX(self.getX() + self.getSpeed()*self.getDirX())  # pos/neg changes whether moving left or right
        if self.getX() > MAX_X - self.getWidth():
            self.setDirX(-1)
        if self.getX() < MIN_X:
            self.setDirX(1)

    def bounceY(self, MAX_Y, MIN_Y=0):
        self.setY(self.getY() + self.getSpeed()*self.getDirY())
        if self.getY() > MAX_Y - self.getHeight():
            self.setDirY(-1)
        if self.getY() < MIN_Y:
            self.setDirY(1)

    # --- accessors --- #
    def getGoingRight(self):
        return self.__GOING_RIGHT

