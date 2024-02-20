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


def Menu():
    """
    display Menu text objects
    :return: None
    """
    global WELCOME, INSTRUCTIONS, PROCEED
    WELCOME.setColour((255, 255, 255))
    WELCOME.setPOS(
        WINDOW.getWidth() // 2 - WELCOME.getWidth() // 2,
        WINDOW.getHeight() // 2 - WELCOME.getHeight() * 2
    )
    INSTRUCTIONS.setColour((255, 255, 255))
    INSTRUCTIONS.setPOS(
        WINDOW.getWidth() // 2 - INSTRUCTIONS.getWidth() // 2,
        WELCOME.getY() + WELCOME.getHeight() + INSTRUCTIONS.getHeight()
    )
    PROCEED.setColour((255, 255, 255))
    PROCEED.setPOS(
        WINDOW.getWidth() // 2 - PROCEED.getWidth() // 2,
        INSTRUCTIONS.getY() + INSTRUCTIONS.getHeight() + PROCEED.getHeight()
    )

    WINDOW.clearScreen()
    WINDOW.getSurface().blit(WELCOME.getSurface(), WELCOME.getPOS())
    WINDOW.getSurface().blit(INSTRUCTIONS.getSurface(), INSTRUCTIONS.getPOS())
    WINDOW.getSurface().blit(PROCEED.getSurface(), PROCEED.getPOS())
    WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Brick Breaker")

    # -------------------- INITIALIZE -------------------- #
    # menu text
    MENU_ON = True
    WELCOME = Text("Welcome to Brickbreaker!", 35)
    INSTRUCTIONS = Text("Use 'A' and 'D' to move your paddle. Have the ball collide with bricks, and don't let the ball touch the ground!", 15)
    PROCEED = Text("Press '1' to continue", 20)
    # game items
    GAME_START = False
    LVL1, LVL2 = True, False
    BRICKS_LEFT = 0
    WIN = False
    BALL = Ball(15, 15)
    PLAYER_PADDLE = Player(WINDOW.getWidth()//8)
    TITLE = Text("BRICK BREAKER!", 25)
    TITLE_BG = Box(WINDOW.getWidth(), TITLE.getHeight())
    SCORE = Text("Score: ", 25)
    POINTS = Text(str(PLAYER_PADDLE.getScore()), 25)
    HEALTH = [ImageSprite("heart.png"), ImageSprite("heart.png"), ImageSprite("heart.png")]
    HEALTH_COUNT = 3
    PRESS_START = Text("Press SPACE to play", 25)

    # -------------------- PROCESSING -------------------- #
    # game objects
    PLAYER_PADDLE.setPOS(
        WINDOW.getWidth() // 2 - PLAYER_PADDLE.getWidth() // 2,
        WINDOW.getHeight() - PLAYER_PADDLE.getHeight() * 4
    )
    BALL_START_POS = (WINDOW.getWidth()//2 - BALL.getWidth()//2, PLAYER_PADDLE.getY() - BALL.getHeight()*3)
    BALL.setPOS(BALL_START_POS[0], BALL_START_POS[1])
    BALL.setColour((255, 0, 0))
    PRESS_START.setPOS(
        WINDOW.getWidth()//2 - PRESS_START.getWidth()//2,
        BALL.getY() - PRESS_START.getHeight()*2
    )
    PRESS_START.setColour((255, 255, 255))
    LVL1_BRICKS, LVL2_BRICKS = [], []
    for i in range(6):  # rows
        for j in range(6):  # bricks in each row
            LVL1_BRICKS.append(Brick(WINDOW.getWidth()//8, WINDOW.getHeight()//16))
            LVL1_BRICKS[-1].setY(LVL1_BRICKS[-1].getHeight()*(i+2)*1.2)
            if i % 2 == 0:  # even row
                LVL1_BRICKS[-1].setX(LVL1_BRICKS[-1].getWidth()*(j+1) + LVL1_BRICKS[-1].getWidth()//16*(j+1))
            else:
                LVL1_BRICKS[-1].setX(LVL1_BRICKS[-1].getWidth()*(j+0.5) + LVL1_BRICKS[-1].getWidth()//16*(j+1))
    for i in range(6):
        for j in range(6):
            if j % 2 == 0:
                LVL2_BRICKS.append(Brick(WINDOW.getWidth()//12, WINDOW.getHeight()//16))
                LVL2_BRICKS[-1].setY(LVL2_BRICKS[-1].getHeight()*(i+2)*1.2)
                LVL2_BRICKS[-1].setX(LVL2_BRICKS[-1].getWidth()*(j+2.6)+LVL2_BRICKS[-1].getWidth())
    BRICKS_LEFT = len(LVL1_BRICKS)

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

    # ----- MAIN GAME ----- #
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # see instructions
                    MENU_ON = False
                elif event.key == pygame.K_SPACE:  # start new game
                    GAME_START = True

        if GAME_START:
            # remove start game text
            PRESS_START.setPOS(-1000, -1000)
            # collision checks
            if BALL.getY()+BALL.getHeight() >= WINDOW.getHeight():  # if ball hits ground
                # remove health
                for i in range(3-HEALTH_COUNT, -1, -1):
                    HEALTH[i].setPOS(-100, -100)
                HEALTH_COUNT -= 1
                # reset game objects
                BALL.setPOS(BALL_START_POS[0], BALL_START_POS[1])
                BALL.setDirX(1)
                PLAYER_PADDLE.setPOS(
                    WINDOW.getWidth() // 2 - PLAYER_PADDLE.getWidth() // 2,
                    WINDOW.getHeight() - PLAYER_PADDLE.getHeight() * 4
                )
                # text instructions
                PRESS_START.setPOS(
                    WINDOW.getWidth() // 2 - PRESS_START.getWidth() // 2,
                    BALL.getY() - PRESS_START.getHeight() * 2
                )
                GAME_START = False
                continue
            else:
                BALL.bounceX(WINDOW.getWidth())
                BALL.bounceY(WINDOW.getHeight(), TITLE.getHeight())
                KEYS_PRESSED = pygame.key.get_pressed()
                PLAYER_PADDLE.ADmove(KEYS_PRESSED)
                PLAYER_PADDLE.checkHorizontalBounds(WINDOW.getWidth())

            if PLAYER_PADDLE.isCollision(BALL.getSurface(), BALL.getPOS()):
                if PLAYER_PADDLE.getY() <= BALL.getY() <= PLAYER_PADDLE.getY()+PLAYER_PADDLE.getHeight():  # if side of paddle hit
                    BALL.setDirX(BALL.getDirX()*-1)
                else:
                    BALL.setDirY(-1)
                    if PLAYER_PADDLE.getDirX() == 1:
                        BALL.setDirX(1)
                    else:
                        BALL.setDirX(-1)

            if LVL1:
                for i in range(len(LVL1_BRICKS)):
                    if BALL.isCollision(LVL1_BRICKS[i].getSurface(), LVL1_BRICKS[i].getPOS()):
                        # update score
                        PLAYER_PADDLE.updateScore(10)
                        POINTS = Text(str(PLAYER_PADDLE.getScore()), 25)
                        POINTS.setPOS(SCORE.getWidth(), 0)
                        POINTS.setColour((255, 255, 255))
                        # update bricks
                        BRICKS_LEFT -= 1
                        if BRICKS_LEFT <= 0:
                            LVL1, LVL2 = False, True
                            BRICKS_LEFT = len(LVL2_BRICKS)
                            # reset game objects
                            BALL.setPOS(BALL_START_POS[0], BALL_START_POS[1])
                            BALL.setDirX(1)
                            PLAYER_PADDLE.setPOS(
                                WINDOW.getWidth() // 2 - PLAYER_PADDLE.getWidth() // 2,
                                WINDOW.getHeight() - PLAYER_PADDLE.getHeight() * 4
                            )
                            # text instructions
                            PRESS_START.setPOS(
                                WINDOW.getWidth() // 2 - PRESS_START.getWidth() // 2,
                                BALL.getY() - PRESS_START.getHeight() * 2
                            )
                            GAME_START = False
                            continue
                        # check deflection of ball
                        if LVL1_BRICKS[i].getY() <= BALL.getY() <= LVL1_BRICKS[i].getY()+LVL1_BRICKS[i].getHeight() and (BALL.getX() < LVL1_BRICKS[i].getX() or BALL.getX() > LVL1_BRICKS[i].getX()+LVL1_BRICKS[i].getWidth()-BALL.getWidth()/2):  # if sides of brick hit
                                BALL.setDirX(BALL.getDirX()*-1)
                        else:  # if top/bottom hit
                            BALL.setDirY(BALL.getDirY()*-1)
                        LVL1_BRICKS[i].setPOS(-1000, 1000)

            elif LVL2:
                for i in range(len(LVL2_BRICKS)):
                    if BALL.isCollision(LVL2_BRICKS[i].getSurface(), LVL2_BRICKS[i].getPOS()):
                        # update score
                        PLAYER_PADDLE.updateScore(10)
                        POINTS = Text(str(PLAYER_PADDLE.getScore()), 25)
                        POINTS.setPOS(SCORE.getWidth(), 0)
                        POINTS.setColour((255, 255, 255))
                        # update bricks
                        BRICKS_LEFT -= 1
                        if BRICKS_LEFT <= 0:
                            WIN = True
                            break
                        # check deflection of ball
                        if LVL2_BRICKS[i].getY() <= BALL.getY() <= LVL2_BRICKS[i].getY() + LVL2_BRICKS[i].getHeight() and (BALL.getX() < LVL2_BRICKS[i].getX() or BALL.getX() > LVL2_BRICKS[i].getX()+LVL2_BRICKS[i].getWidth() - BALL.getWidth() / 2):  # if sides of brick hit
                            BALL.setDirX(BALL.getDirX() * -1)
                        else:  # if top/bottom hit
                            BALL.setDirY(BALL.getDirY() * -1)
                        LVL2_BRICKS[i].setPOS(-1000, 1000)

        # ----- outputs ----- #
        WINDOW.clearScreen()
        # title bar objects
        WINDOW.getSurface().blit(TITLE_BG.getSurface(), TITLE_BG.getPOS())
        WINDOW.getSurface().blit(TITLE.getSurface(), TITLE.getPOS())
        WINDOW.getSurface().blit(SCORE.getSurface(), SCORE.getPOS())
        WINDOW.getSurface().blit(POINTS.getSurface(), POINTS.getPOS())
        for i in range(3):
            WINDOW.getSurface().blit(HEALTH[i].getSurface(), HEALTH[i].getPOS())
        # game objects
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        WINDOW.getSurface().blit(PRESS_START.getSurface(), PRESS_START.getPOS())
        WINDOW.getSurface().blit(PLAYER_PADDLE.getSurface(), PLAYER_PADDLE.getPOS())
        if MENU_ON:
            Menu()
        else:
            if LVL1:
                for i in range(len(LVL1_BRICKS)):
                    WINDOW.getSurface().blit(LVL1_BRICKS[i].getSurface(), LVL1_BRICKS[i].getPOS())
            elif LVL2:
                for i in range(len(LVL2_BRICKS)):
                    WINDOW.getSurface().blit(LVL2_BRICKS[i].getSurface(), LVL2_BRICKS[i].getPOS())
            if HEALTH_COUNT <= 0:
                print("\nYou lost :( \nTHANKS FOR PLAYING!")
                pygame.quit()
                exit()
        if WIN:
            print(f"\nYou won! Your final score is {PLAYER_PADDLE.getScore()}.\nTHANKS FOR PLAYING!")
            pygame.quit()
            exit()

        WINDOW.updateFrame()
