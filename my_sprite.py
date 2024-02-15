"""
title: abstract parent classes
author: joanna hao
date-created: 2024-02-05
"""
import pygame


class MySprite:
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPEED=5, COLOUR=(255, 255, 255)):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPEED = SPEED
        self._COLOUR = COLOUR
        self._SURFACE = pygame.Surface
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # --- modifier methods --- #
    def setDirX(self, VALUE):
        self.__DIR_X = VALUE

    def setDirY(self, VALUE):
        self.__DIR_Y = VALUE

    def setX(self, X):
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setPOS(self, X, Y):
        self.setX(X)
        self.setY(Y)

    def setColour(self, TUPLE):
        self._COLOUR = TUPLE

    def WASDmove(self, KEY_PRESSES):
        """
        move box based on WASD
        :param KEY_PRESSES: list[int]
        :return: None
        """
        # horizontal mv't
        if KEY_PRESSES[pygame.K_d] == 1:  # if D key pressed
            self.__X = self.__X + self.__SPEED
        if KEY_PRESSES[pygame.K_a] == 1:
            self.__X = self.__X - self.__SPEED

        # vertical mv't
        if KEY_PRESSES[pygame.K_w] == 1:
            self.__Y = self.__Y - self.__SPEED
        if KEY_PRESSES[pygame.K_s] == 1:
            self.__Y = self.__Y + self.__SPEED

        self.__POS = (self.__X, self.__Y)

    # --- accessor methods --- #
    def getSurface(self):
        return self._SURFACE

    def getPOS(self):
        return self.__POS

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def isCollision(self, SURFACE:pygame.Surface, POS):
        """
        testing whether the current sprite position is overlapping the given sprite's position
        :param SURFACE: surface object
        :param POS: tuple(int)
        :return: bool or tuple(bool, int, int)
        """
        WIDTH = SURFACE.get_width()
        HEIGHT = SURFACE.get_height()
        X = POS[0]
        Y = POS[1]

        if X >= self.__X - WIDTH and X <= self.__X + self._SURFACE.get_width():
            if Y >= self.__Y - HEIGHT and Y <= self.__Y + self._SURFACE.get_height():
                return True
        return False

    def isNorthCollision(self):
        pass

    def isEastCollision(self):
        pass

    def isSouthCollision(self):
        pass

    def isWestCollision(self):
        pass

    def getDirX(self):
        return self.__DIR_X

    def getDirY(self):
        return self.__DIR_Y

    def getSpeed(self):
        return self.__SPEED


class Box(MySprite):
    def __init__(self, WIDTH=1, HEIGHT=1):
        MySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOUR)

    # --- modifier --- #
    def setColour(self, TUPLE):
        MySprite.setColour(self, TUPLE)
        self._SURFACE.fill(self._COLOUR)  # polymorphism
