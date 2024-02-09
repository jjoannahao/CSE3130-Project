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
from brick import Brick

if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Brick Breaker")

    # ----- inputs ----- # -> initialize objects on screen
    # menu text
    MENU_ON = True
    WELCOME = Text("Welcome to Brickbreaker!", 35)
    MENU = Text("""
1. Start New Game
2. See Leaderboard
3. See Instructions
    """, 25)
    # game items
    LVL1, LVL2 = True, False
    BALL = Ball(15, 15)
    PLAYER_PADDLE = Player()
    TITLE = Text("Brick Breaker", 25)
    SCORE = Text("Score: ", 25)
    POINTS = Text(str(PLAYER_PADDLE.getScore()), 25)

    # ----- processing ----- #
    # menu objects

    # game objects
    BALL.setPOS(WINDOW.getWidth() // 2, WINDOW.getHeight() // 2)
    BALL.setColour((255, 0, 0))
    PLAYER_PADDLE.setPOS(
        WINDOW.getWidth() // 2 - PLAYER_PADDLE.getWidth() // 2,
        WINDOW.getHeight() - PLAYER_PADDLE.getHeight() * 4
    )
    LVL1_BRICKS = []
    for i in range(1, 7):
        for j in range(1, 7):
            LVL1_BRICKS.append(Brick(75, 25))
            LVL1_BRICKS[-1].setPOS(

            )

    # Title Bar Objects
    TITLE.setPOS(WINDOW.getWidth() // 2 - TITLE.getWidth() // 2, 0)
    TITLE.setColour((255, 255, 255))
    SCORE.setPOS(0, 0)
    SCORE.setColour((255, 255, 255))
    POINTS.setPOS(SCORE.getWidth(), 0)
    POINTS.setColour((255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # menu:
        """
        while MENU_ON:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            INPUT_KEYS_HIT = pygame.key.get_pressed()
            if INPUT_KEYS_HIT[pygame.K_1]:
                # start new game
                pass
            elif INPUT_KEYS_HIT[pygame.K_2]:
                # see leaderboard
                pass
            elif INPUT_KEYS_HIT[pygame.K_3]:
                # see instructions
                # blit instructions #
                PROCEED = pygame.key.get_focused()
                if PROCEED:  # if any key hit
                    # remove menu text #
                    MENU_ON = False
                    pass
        """

        # game:
        BALL.bounceX(WINDOW.getWidth())
        BALL.bounceY(WINDOW.getHeight(), TITLE.getHeight())
        KEYS_PRESSED = pygame.key.get_pressed()
        PLAYER_PADDLE.ADmove(KEYS_PRESSED)
        PLAYER_PADDLE.checkHorizontalBounds(WINDOW.getWidth())

        # ----- outputs ----- #
        WINDOW.clearScreen()
        # --- blit objects on screen:
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        WINDOW.getSurface().blit(TITLE.getSurface(), TITLE.getPOS())
        WINDOW.getSurface().blit(SCORE.getSurface(), SCORE.getPOS())
        WINDOW.getSurface().blit(POINTS.getSurface(), POINTS.getPOS())
        WINDOW.getSurface().blit(PLAYER_PADDLE.getSurface(), PLAYER_PADDLE.getPOS())

        # LEVEL 1 objects
        if LVL1:
            for i in range(36):
                WINDOW.getSurface().blit(LVL1_BRICKS[i].getSurface(), LVL1_BRICKS[i].getPOS())
        # LEVEL 2 objects
        elif LVL2:
            pass

        WINDOW.updateFrame()
