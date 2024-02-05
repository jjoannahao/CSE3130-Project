"""
title: window class
author: joanna hao
date-created: 2024-02-05
"""
import pygame


class Window:
    """
    creates the window that will load the game
    """

    def __init__(self, TITLE, WIDTH=800, HEIGHT=600, FPS=30):  # put in default values (efficiency)
        self.__TITLE = TITLE
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__FPS = FPS
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)
        self.__CLOCK = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIM)  # like layers in photoshop
        self.__SURFACE.fill((50, 50, 50))  # grey background
        pygame.display.set_caption(self.__TITLE)

    def updateFrame(self):
        self.__CLOCK.tick(self.__FPS)
        pygame.display.flip()

    def clearScreen(self):
        self.__SURFACE.fill((50, 50, 50))

    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT
