"""
    Nom du fichier : main.py
    Nom du projet : SnakeV3
    Auteur : Thomas Stäheli
    Date : 14.08.2022
    Description : jeu du snake avec Pygame (sans image graphique)
"""

import pygame
from random import randint
from time import sleep

print("Author : Thomas Stäheli")
print("Date : 14.08.2022")
print("Game Started !")

pygame.init()
# Fonctionne uniquement avec les multiples de 10
sizeScreenX = 900
sizeScreenY = 900
scareSize = 50
difficulty = 9 # 11 = Impossible / 9 = Hard / 7 = normal / 5 = eazy
screen = pygame.display.set_mode((sizeScreenX, sizeScreenY))
pygame.display.set_caption("Snake V2")
font_name = pygame.font.match_font('arial')

screen.fill((255, 255, 255))

run = 1
x = 0
y = 1
timemoutChange = 10

snakeChangeX = -50
snakeChangeY = 0

# Creating separated table
snake = []
snake.append((int(sizeScreenX/2 - scareSize), int(sizeScreenY/2 - scareSize)))
snake.append((int(sizeScreenX/2), int(sizeScreenY/2 - scareSize)))

def interface():
    """
    Description : Draw the interface
    :return: None
    """
    cordX = 0
    cordY = 0
    # Size of a rectangle
    widthXY = scareSize
    switchColor = 1
    backToline = 1

    # Liste of 5 colors
    color = {
        1 : (7, 239, 235),
        2 : (30, 196, 220),
        3 : (54, 154, 205),
        4 : (77, 111, 190),
        5 : (102, 68, 175)
    }

    # Change the color for green setup
    """color = {
        1: 0x57D53B,
        2: 0x1B4f08,
        3: 0x096A09,
        4: 0x22780F,
        5: 0x3A9D23
    }"""

    # Matrice for the scare
    for i in range(int(sizeScreenY/widthXY)):
        for i in range(int(sizeScreenX/widthXY)):
            pygame.draw.rect(screen, color[switchColor], (cordX, cordY, cordX+widthXY, cordY+widthXY), 0)
            if switchColor >= 5:
                switchColor = 1
            else:
                switchColor += 1
            cordX += widthXY

        # Just to look better
        if backToline >= 5:
            backToline = 1
        else:
            backToline += 1

        # Adjust color to the next line
        switchColor = backToline
        cordX = 0
        cordY += widthXY

def randomApple():
    """
    Descirption : make a random spawn of the apple but not in the snake
    :return: apple cord X and apple cord Y in a tuple
    """
    fOccuped = 1
    while fOccuped:
        fOccuped = 0
        appleCordX = randint(0, sizeScreenY/scareSize - 1) * scareSize
        appleCordY = randint(0, sizeScreenY/scareSize - 1) * scareSize
        for body in snake:
            if body[x] == appleCordX and body[y] == appleCordY:
                fOccuped = 1
                break
    return (appleCordX, appleCordY)

def drawSnake(cordX, cordY):
    """
    Description : draw the body of one part of the snake (pixel)
    :param cordX: where the body start at X pos
    :param cordY: where the body start at Y pos
    :return: None
    """
    pygame.draw.rect(screen, "blue", (cordX, cordY, scareSize, scareSize), 0)
    pygame.draw.rect(screen, 'white', (cordX, cordY, scareSize, scareSize), 5)

def drawApple(cordX, cordY):
    """
    Description : draw a beautiful apple with pixel
    :param cordX: where the apple has to spawn in X cordonate
    :param cordY: where the apple has to spawn in Y cordonate
    :return: None
    """
    pygame.draw.rect(screen, "red", (cordX, cordY, scareSize, scareSize), 0)
    pygame.draw.rect(screen, "green", (cordX + 15, cordY + 15, scareSize - 25, scareSize - 25), 0)
    pygame.draw.rect(screen, 'black', (cordX, cordY, scareSize, scareSize), 1)
    pygame.draw.rect(screen, 'black', (cordX + 15, cordY + 15, scareSize - 25, scareSize - 25), 1)

def drawAllSnake():
    """

    :return:
    """
    for body in snake:
        drawSnake(body[x], body[y])

def drawText(surf, text, size, x, y, color):
    """
    Description : Draw a test where you want
    :param surf: surface where you want to draw your text
    :param text: enter your text
    :param size: size (10 = small, 50 = medium)
    :param x: where you want to place in X cordonate
    :param y: where you want to place in Y cordonate
    :return:
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

###################################################### MAIN ############################################################


screen.fill('black')
drawText(screen, "Press any keys and game will start.", 50, sizeScreenX/2, sizeScreenY/3, 'white')
pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            start = False
        if event.type == pygame.KEYDOWN:
            run = False
            start = True

interface()
appleCord = randomApple()
drawApple(appleCord[x], appleCord[y])
drawSnake(sizeScreenX/2 - scareSize, sizeScreenY/2 - scareSize)

pygame.display.update()
clock = pygame.time.Clock()
fPressed = 0
while start:
    # Traitement clavier
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        # Detect the Key press, state : pressed
        if event.type == pygame.KEYDOWN and fPressed == 0:
            # Go left
            fPressed = 1
            if event.key == pygame.K_a or event.key == pygame.K_LEFT and snakeChangeX == 0:
                snakeChangeX = -50
                snakeChangeY = 0
            # Go right
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT and snakeChangeX == 0:
                snakeChangeX = 50
                snakeChangeY = 0
            # Go up
            elif event.key == pygame.K_w or event.key == pygame.K_UP and snakeChangeY == 0:
                snakeChangeX = 0
                snakeChangeY = -50
            # Go down
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN and snakeChangeY == 0:
                snakeChangeX = 0
                snakeChangeY = 50
    fPressed = 0
    # Take old cordonate for the condition, if the apple is eaten
    lenSnake = len(snake)
    lastCoordonate = snake[lenSnake - 1]
    # Copy the cordonate of the body in front of him
    while lenSnake > 1:
        snake[lenSnake - 1] = snake[lenSnake - 2]
        lenSnake -= 1

    # Changing pos of head
    snake[0] = (snake[0][0] + snakeChangeX, snake[0][1] + snakeChangeY)

    # Check if apple is eaten
    if snake[0] == appleCord:
        print("MIAM")
        appleCord = randomApple()
        snake.append(lastCoordonate)

    # Check if the snake is already in this place
    lenSnake = len(snake)
    while lenSnake > 1:
        if snake[0] == snake[lenSnake - 1]:
            start = False
            break
        lenSnake -= 1
    # Check if he is not out of the map
    if snake[0][0] < 0 or snake[0][0] >= sizeScreenX or snake[0][1] < 0 or snake[0][1] >= sizeScreenY:
        start = False
    else:
        # Draw all the stuff needed
        interface()
        drawApple(appleCord[x], appleCord[y])
        drawAllSnake()
        drawText(screen, "Score : " + str(len(snake) - 2), 50, 100, 0, 'black')

    pygame.display.update()
    sleep(0.1)
    #clock.tick(difficulty)

print("Your score was : " + str(len(snake) - 2))
pygame.quit()
quit()