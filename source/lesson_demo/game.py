import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
d_2tube = 150
tube_velocity = 2
bird_drop_velocity = 0
gravity = 0.6
score = 0
font = pygame.font.SysFont('san', 20)
font1 = pygame.font.SysFont('san', 30)
x_bird = 50
y_bird = 350
tube1_x = 400
tube2_x = 600
tube3_x = 800
tube_width = 50
tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)
background_img = pygame.image.load('background.png')
background_img = pygame.transform.scale(background_img, (400, 600))
sand_img = pygame.image.load('sand.png')
sand_img = pygame.transform.scale(sand_img, (400, 30))
bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img, (35, 35))
tube_img = pygame.image.load('tube.png')
tube_op_img = pygame.image.load('tube_op.png')
tube1_pass = False
tube2_pass = False
tube3_pass = False
pausing = False
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    screen.blit(background_img, (0, 0))
    bird = screen.blit(bird_img, (x_bird, y_bird))
    tube1_img = pygame.transform.scale(tube_img, (tube_width, tube1_height))
    tube1 = screen.blit(tube1_img, (tube1_x, 0))
    tube2_img = pygame.transform.scale(tube_img, (tube_width, tube2_height))
    tube2 = screen.blit(tube2_img, (tube2_x, 0))
    tube3_img = pygame.transform.scale(tube_img, (tube_width, tube3_height))
    tube3 = screen.blit(tube3_img, (tube3_x, 0))
    tube_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600 - tube1_height + d_2tube))
    tube1_op = screen.blit(tube_op_img, (tube1_x, tube1_height + d_2tube))
    tube2_op = screen.blit(tube_op_img, (tube2_x, tube2_height + d_2tube))
    tube3_op = screen.blit(tube_op_img, (tube3_x, tube3_height + d_2tube))
    tube1_x -= tube_velocity
    tube2_x -= tube_velocity
    tube3_x -= tube_velocity
    if tube1_x < -tube_width:
        tube1_x = 550
        tube1_height = randint(100, 400)
        tube1_pass = False
    if tube2_x < -tube_width:
        tube2_x = 550
        tube2_height = randint(100, 400)
        tube2_pass = False
    if tube3_x < -tube_width:
        tube3_x = 550
        tube3_height = randint(100, 400)
        tube3_pass = False
    score_txt = font.render(' Score:' + str(score), True, RED)
    sand = screen.blit(sand_img, (0, 570))
    screen.blit(score_txt, (5, 5))
    y_bird += bird_drop_velocity
    bird_drop_velocity += gravity
    if tube1_x + tube_width <= x_bird and tube1_pass is False:
        score += 1
        tube1_pass = True
    if tube2_x + tube_width <= x_bird and tube2_pass is False:
        score += 1
        tube2_pass = True
    if tube3_x + tube_width <= x_bird and tube3_pass is False:
        score += 1
        tube3_pass = True
    tubes = [tube1, tube2, tube3, tube1_op, tube2_op, tube3_op, sand]
    for tube in tubes:
        if bird.colliderect(tube):
            tube_velocity = 0
            bird_drop_velocity = 0
            game_over_txt = font1.render('Game Over, Loser! Score:' + str(score), True, RED)
            screen.blit(game_over_txt, (85, 260))
            space_txt = font.render(" Press Space to play again, baby!", True, BLUE)
            screen.blit(space_txt, (120, 290))
            pausing = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_drop_velocity = 0
                bird_drop_velocity -= 7
                if pausing:
                    x_bird = 50
                    y_bird = 350
                    tube1_x = 400
                    tube2_x = 600
                    tube3_x = 800
                    tube_velocity = 2
                    score = 0
                    pausing = False
    pygame.display.flip()
pygame.quit()
