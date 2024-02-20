"""
title: text class
author: joanna hao
date-created: 2024-02-07
"""
import pygame


class Text:
    """
    create text object to put on the screen
    """
    def __init__(self, TEXT, SIZE=48, FAMILY="Arial"):
        self.__TEXT = TEXT
        self.__FONT_FAMILY = FAMILY
        self.__FONT_SIZE = SIZE
        self.__FONT_COLOUR = (0, 255, 0)
        self.__FONT = pygame.font.SysFont(self.__FONT_FAMILY, self.__FONT_SIZE)
        self.__SURFACE = self.__FONT.render(self.__TEXT, 1, self.__FONT_COLOUR)
        self.__X = 0
        self.__Y = 0
        self.__POS = (self.__X, self.__Y)

    # --- modifiers --- #
    def setPOS(self, X, Y):
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setColour(self, TUPLE):
        self.__FONT_COLOUR = TUPLE
        self.__SURFACE = self.__FONT.render(self.__TEXT, 1, self.__FONT_COLOUR)

    # --- accessors --- #
    def getSurface(self):
        return self.__SURFACE

    def getPOS(self):
        return self.__POS

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def getWidth(self):
        return self.__SURFACE.get_width()

    def getHeight(self):
        return self.__SURFACE.get_height()

