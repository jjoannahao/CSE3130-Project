"""
title: main brickbreaker file
author: joanna hao
date-created: 2024-02-05
"""
import pygame
from my_sprite import *
from window import Window
from ball import Ball
from text import Text
from player import Player
from brick import Brick
from image import ImageSprite

if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Brick Breaker")

    # ----- inputs ----- # -> initialize objects on screen
    # menu text
    MENU_ON = True
    WELCOME = Text("Welcome to Brickbreaker!", 35)
    MENU = Text("""
1. Start New Game
2. See Instructions
    """, 25)
    # game items
    LVL1, LVL2 = True, False
    BALL = Ball(15, 15)
    PLAYER_PADDLE = Player(WINDOW.getWidth()//8)
    TITLE = Text("BRICK BREAKER!", 25)
    TITLE_BG = Box(WINDOW.getWidth(), TITLE.getHeight())
    SCORE = Text("Score: ", 25)
    POINTS = Text(str(PLAYER_PADDLE.getScore()), 25)
    HEALTH = [ImageSprite("heart.png"), ImageSprite("heart.png"), ImageSprite("heart.png")]
    PRESS_START = Text("Press SPACE to start game", 25)

    # ----- processing ----- #
    # menu objects

    # game objects
    PLAYER_PADDLE.setPOS(
        WINDOW.getWidth() // 2 - PLAYER_PADDLE.getWidth() // 2,
        WINDOW.getHeight() - PLAYER_PADDLE.getHeight() * 4
    )
    BALL_START_POS = (WINDOW.getWidth()//2 - BALL.getWidth()//2, PLAYER_PADDLE.getY() - BALL.getHeight()*3)
    BALL.setPOS(BALL_START_POS[0], BALL_START_POS[1])
    BALL.setColour((255, 0, 0))
    PRESS_START.setPOS(WINDOW.getWidth()//2 - PRESS_START.getWidth()//2, BALL.getY() - PRESS_START.getHeight()*2)
    PRESS_START.setColour((255, 255, 255))
    LVL1_BRICKS = []
    for i in range(6):  # rows
        for j in range(6):  # bricks in each row
            LVL1_BRICKS.append(Brick(WINDOW.getWidth()//8, WINDOW.getHeight()//16))
            LVL1_BRICKS[-1].setY(LVL1_BRICKS[-1].getHeight()*(i+2)*1.2)
            if i % 2 == 0:  # even row
                LVL1_BRICKS[-1].setX(LVL1_BRICKS[-1].getWidth()*(j+1) + LVL1_BRICKS[-1].getWidth()//16*(j+1))
            else:
                LVL1_BRICKS[-1].setX(LVL1_BRICKS[-1].getWidth()*(j+0.5) + LVL1_BRICKS[-1].getWidth()//16*(j+1))

    # Title Bar Objects
    TITLE.setPOS(WINDOW.getWidth() // 2 - TITLE.getWidth() // 2, 0)
    TITLE.setColour((255, 255, 255))
    TITLE_BG.setColour((0, 0, 0))
    SCORE.setPOS(0, 0)
    SCORE.setColour((255, 255, 255))
    POINTS.setPOS(SCORE.getWidth(), 0)
    POINTS.setColour((255, 255, 255))
    for i in range(3):
        HEALTH[i].setScale(0.1)
        HEALTH[i].setPOS(WINDOW.getWidth() - HEALTH[i].getWidth()*(i+1) - HEALTH[i].getWidth()//4*(i+1), 0)

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
                # see instructions
                # blit instructions #
                PROCEED = pygame.key.get_focused()
                if PROCEED:  # if any key hit
                    # remove menu text #
                    MENU_ON = False
                    pass
        """

        # while True:
        #     KEYS = pygame.key.get_pressed()
        #     if pygame.K_SPACE in KEYS:
        #         PRESS_START.setPOS(0-PRESS_START.getWidth(), 0-PRESS_START.getHeight())
        #         break
        # game:
        if PLAYER_PADDLE.isCollision(BALL.getSurface(), BALL.getPOS()):
            if PLAYER_PADDLE.getY() <= BALL.getY() <= PLAYER_PADDLE.getY() + PLAYER_PADDLE.getHeight():  # if side of paddle hit
                if BALL.getGoingRight():
                    BALL.setDirX(-1)
                else:
                    BALL.setDirX(1)
            else:
                BALL.setDirY(-1)
        for i in range(len(LVL1_BRICKS)):
            if BALL.isCollision(LVL1_BRICKS[i].getSurface(), LVL1_BRICKS[i].getPOS()):
                BALL.setDirY(1)  # going down
                # check X, Y to see which way deflects
                if BALL.getY() < LVL1_BRICKS[i].getY()+LVL1_BRICKS[i].getHeight():
                    pass

        BALL.bounceX(WINDOW.getWidth())
        BALL.bounceY(WINDOW.getHeight(), TITLE.getHeight())
        KEYS_PRESSED = pygame.key.get_pressed()
        PLAYER_PADDLE.ADmove(KEYS_PRESSED)
        PLAYER_PADDLE.checkHorizontalBounds(WINDOW.getWidth())

        # ----- outputs ----- #
        WINDOW.clearScreen()
        # title bar objects
        WINDOW.getSurface().blit(TITLE_BG.getSurface(), TITLE_BG.getPOS())
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        WINDOW.getSurface().blit(TITLE.getSurface(), TITLE.getPOS())
        WINDOW.getSurface().blit(SCORE.getSurface(), SCORE.getPOS())
        WINDOW.getSurface().blit(POINTS.getSurface(), POINTS.getPOS())

        for i in range(3):
            WINDOW.getSurface().blit(HEALTH[i].getSurface(), HEALTH[i].getPOS())

        # game objects
        WINDOW.getSurface().blit(PRESS_START.getSurface(), PRESS_START.getPOS())
        WINDOW.getSurface().blit(PLAYER_PADDLE.getSurface(), PLAYER_PADDLE.getPOS())
        if LVL1:  # LEVEL 1 objects
            for i in range(36):
                WINDOW.getSurface().blit(LVL1_BRICKS[i].getSurface(), LVL1_BRICKS[i].getPOS())

        elif LVL2:  # LEVEL 2 objects
            pass

        WINDOW.updateFrame()
