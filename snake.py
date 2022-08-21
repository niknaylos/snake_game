import pygame
import time
import random
import threading
 
pygame.init()
 
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
magenta = ((255,0,230))
dis_width = 400
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption(f'Snake game.')
 
clock = pygame.time.Clock()

snake_block = 10

 
font_style = pygame.font.SysFont("robotomono", 25)
score_font = pygame.font.SysFont("robotomono", 35)
 
 
def Your_score(score):
    value = score_font.render(str(f'Your score: {score}'), True, magenta)
    dis.blit(value, [0, 250])
def difficulty(snake_speed):
    value = score_font.render(str(f'Snake speed: {snake_speed}'), True, magenta)
    dis.blit(value, [200, 250])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, magenta, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    snake_speed = 12
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    # blockerx = round(random.randrange(0, dis_width - 10) / 10.0) * 10.0
    # blockery = round(random.randrange(0, dis_height - 10) / 10.0) * 10.0
    # blocker2x = round(random.randrange(0, dis_width - 10) / 10.0) * 10.0
    # blocker2y = round(random.randrange(0, dis_height - 10) / 10.0) * 10.0


 
    while not game_over:
        pygame.display.set_caption(f'Your score: {Length_of_snake-1}')
        while game_close == True:
            pygame.display.set_caption('Game Over')
            dis.fill(black)
            message("    C to play again, Q to quit", magenta)
            Your_score(Length_of_snake - 1)
            difficulty(snake_speed)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        # pygame.draw.rect(dis, red, [blockerx, blockery, snake_block, snake_block])
        # pygame.draw.rect(dis, red, [blocker2x, blocker2y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        # Your_score(Length_of_snake - 1)
        # difficulty(snake_speed)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            # print('Blocked at', x1,y1)
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            Length_of_snake += 1
            snake_speed += 1
        # if x1 == blockerx or y1 == blockery:
        #     print('blocked at', x1, y1)
        # if Length_of_snake >= 2:
        
        
        
        
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()