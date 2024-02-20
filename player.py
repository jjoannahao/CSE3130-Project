"""
title: player class, including paddle and score
author: joanna hao
date-created: 2024-02-05
"""
import pygame
from my_sprite import Box


class Player(Box):
    def __init__(self, WIDTH=75, HEIGHT=15):
        Box.__init__(self, WIDTH, HEIGHT)
        self.__SCORE = 0

    # --- modifiers --- #
    def updateScore(self, VALUE):
        self.__SCORE += VALUE

    def ADmove(self, KEY_PRESSES):
        """
        horizontally move paddle based on A and D
        :param KEY_PRESSES: list[int]
        :return:
        """
        if KEY_PRESSES[pygame.K_d] == 1:  # if D pressed
            self.setX(self.getX() + self.getSpeed()*1.25)
            self.setDirX(1)
        if KEY_PRESSES[pygame.K_a] == 1:  # if A pressed
            self.setX(self.getX() - self.getSpeed()*1.25)
            self.setDirX(-1)
        self.setPOS(self.getX(), self.getY())

    def checkHorizontalBounds(self, MAX_X, MIN_X=0):
        """
        checking whether obj going beyond screen
        :param MAX_X: int
        :param MIN_X: int
        :return: None
        """
        if self.getX() > MAX_X - self.getWidth():
            self.setX(MAX_X - self.getWidth())
        if self.getX() < MIN_X:
            self.setX(MIN_X)
        self.setPOS(self.getX(), self.getY())

    # --- accessors --- #
    def getScore(self):
        return self.__SCORE
