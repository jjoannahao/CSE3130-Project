"""
title: image sprite class
author: joanna hao
date-created: 2024-02-13
"""
from my_sprite import *


class ImageSprite(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_NAME = IMAGE_FILE
        self._SURFACE = pygame.image.load(self.__FILE_NAME).convert_alpha()

    # --- modifier --- #
    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        adjust the scale of the image
        :param SCALE_X: float
        :param SCALE_Y: float
        :return: None
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SURFACE = pygame.transform.scale(self._SURFACE, (self._SURFACE.get_width()*SCALE_X,
                                                               self._SURFACE.get_height()*SCALE_Y))
