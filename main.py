"""
title: main brickbreaker file
author: joanna hao
date-created: 2024-02-05
"""
import pygame
from window import Window
from ball import Ball
from text import Text
from player import Player

if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Brick Breaker")

    # ----- inputs ----- # -> initialize objects on screen
    BALL = Ball(15, 15)
    PLAYER_PADDLE = Player()
    TITLE = Text("Brick Breaker", 25)
    SCORE = Text("Score: ", 25)
    POINTS = Text(str(PLAYER_PADDLE.getScore()), 25)

    # ----- processing ----- #
    BALL.setPOS(WINDOW.getWidth() // 2, WINDOW.getHeight() // 2)
    BALL.setColour((255, 0, 0))
    TITLE.setPOS(WINDOW.getWidth() // 2 - TITLE.getWidth() // 2, 0)
    TITLE.setColour((255, 255, 255))
    SCORE.setPOS(0, 0)
    SCORE.setColour((255, 255, 255))
    POINTS.setPOS(SCORE.getWidth(), 0)
    POINTS.setColour((255, 255, 255))
    PLAYER_PADDLE.setPOS(
        WINDOW.getWidth()//2 - PLAYER_PADDLE.getWidth()//2,
        WINDOW.getHeight() - PLAYER_PADDLE.getHeight()*4
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        BALL.bounceX(WINDOW.getWidth(), TITLE.getWidth())
        BALL.bounceY(WINDOW.getHeight(), TITLE.getHeight())
        KEYS_PRESSED = pygame.key.get_pressed()
        PLAYER_PADDLE.ADmove(KEYS_PRESSED)
        PLAYER_PADDLE.checkHorizontalBounds(WINDOW.getWidth())

        # ----- outputs ----- #
        WINDOW.clearScreen()
        # blit objects on screen:
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        WINDOW.getSurface().blit(TITLE.getSurface(), TITLE.getPOS())
        WINDOW.getSurface().blit(SCORE.getSurface(), SCORE.getPOS())
        WINDOW.getSurface().blit(POINTS.getSurface(), POINTS.getPOS())
        WINDOW.getSurface().blit(PLAYER_PADDLE.getSurface(), PLAYER_PADDLE.getPOS())

        WINDOW.updateFrame()
