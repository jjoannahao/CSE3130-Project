"""
title: box class for ball
author: joanna hao
date-created: 2024-02-05
"""
from my_sprite import Box
import pygame


class Ball(Box):
    def __init__(self, WIDTH=1, HEIGHT=1):
        Box.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOUR)
        self.__HIT_BOX = Box(self.getWidth()//2, self.getHeight()//2)
        self.__HIT_BOX.setPOS(
            self.getX() + self.getWidth() // 2 - self.__HIT_BOX.getWidth() // 2,
            self.getY() + self.getHeight() // 2 - self.__HIT_BOX.getHeight() // 2
        )

    # --- modifiers --- #


    # --- accessors --- #


if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Boxes Subclass")
    RED_BOX = Box(20, 20)
    RED_BOX.setPOS(WINDOW.getWidth()//2, WINDOW.getHeight()//2)
    RED_BOX.setColour((255, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(RED_BOX.getSurface(), RED_BOX.getPOS())
        WINDOW.updateFrame()

