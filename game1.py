import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("shooters")
icon = pygame.image.load('mission-accomplished.png')
pygame.display.set_icon(icon)

basket = pygame.image.load('basket.png')
basketX = 370
basketY = 500
basket_move = 0

ball = pygame.image.load('ball.png')
ballX = random.randint(50, 750)
ballY = 20
ball_move = 0.2
ball_state = "ready"

score_val = 0
font = pygame.font.Font('freesansbold.ttf', 32)
tx = 10
ty = 10
over = pygame.font.Font('freesansbold.ttf', 64)


def show(x, y):
    score = font.render("Score :  " + str(score_val), True, (0, 0, 0))
    screen.blit(score, (x, y))


def game_over():
    over_text = over.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(basket, (x, y))


def enemy(x, y):
    global ball_state
    ball_state = "shoot"
    screen.blit(ball, (x, y))


def is_basket(ballx, bally, basketx, baskety):
    dist = math.sqrt(math.pow((ballx - basketx), 2) + math.pow((bally - baskety), 2))
    if dist <= 30:
        return True
    else:
        return False


running = True
while running:
    screen.fill((225, 225, 225))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                basket_move = -1
            if event.key == pygame.K_RIGHT:
                basket_move = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                basket_move = 0

    basketX += basket_move

    if basketX <= 6:
        basketX = 6
    elif basketX >= 730:
        basketX = 730

    ballY += ball_move

    if ballY >= 500:
        ballY = 2000
        game_over()

    shoot = is_basket(ballX, ballY, basketX, basketY)
    if shoot:
        ballY = 20
        ballX = random.randint(50, 750)
        score_val += 1

    player(basketX, basketY)
    enemy(ballX, ballY)
    show(tx, ty)
    pygame.display.update()


