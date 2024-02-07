"""
title: brick class
author: joanna hao
date-created: 2024-02-05
"""
import pygame
from my_sprite import Box


class Brick(Box):
    def __init__(self, WIDTH=1, HEIGHT=1):
        Box.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOUR)
