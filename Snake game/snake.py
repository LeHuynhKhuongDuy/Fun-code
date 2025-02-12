import pygame
import random

running = True

width = 600
height = 400 

block_size = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

snake_pos = [95, 55]
snake_body = [[95, 55], [85, 55], [75, 55]]
snake_body_size = block_size / 2

food_pos = [random.randrange(1, (width//block_size)) * block_size,
            random.randrange(1, (height//block_size)) * block_size]

direction = "RIGHT"

def show_game_over():
    win.fill((0, 0, 0))  # Black background
    text = pygame.font.("You Lose!", True, RED)
    win.blit(text, (width//3, height//3))  # Position text at the center
    pygame.display.flip()  # Update the display
    pygame.time.delay(2000)  # Pause for 2 seconds before quitting
    pygame.quit()
    quit()

pygame.init()

win = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w and direction != "DOWN": 
                direction = "UP"
            elif event.key == pygame.K_s and direction != "UP": 
                direction = "DOWN"
            elif event.key == pygame.K_a and direction != "RIGHT": 
                direction = "LEFT"
            elif event.key == pygame.K_d and direction != "LEFT": 
                direction = "RIGHT"

        if event.type == pygame.QUIT:
            running = False
            
    if direction == "LEFT":
        snake_pos[0] -= block_size 
    elif direction == "RIGHT":
        snake_pos[0] += block_size 
    elif direction == "UP":
        snake_pos[1] -= block_size
    elif direction == "DOWN":
        snake_pos[1] += block_size
    
    # if snake_pos[0] > width:
    #     snake_pos[0] = snake_pos[0] - width
    # if snake_pos[0] < 0:
    #     snake_pos[0] = snake_pos[0] + width
    # if snake_pos[1] > height:
    #     snake_pos[1] = snake_pos[1] - height
    # if snake_pos[1] < 0:
    #     snake_pos[1] = snake_pos[1] + height
    # above become below
    snake_pos[0] = snake_pos[0] % width
    snake_pos[1] = snake_pos[1] % height

    snake_body.insert(0, [snake_pos[0], snake_pos[1]])
    if snake_pos == [food_pos[0] + 5, food_pos[1] + 5]:
        food_pos = [random.randrange(1, (width//block_size)) * block_size,
                    random.randrange(1, (height//block_size)) * block_size]
    else:
        snake_body.pop()

    if snake_pos in snake_body[1:]:
        show_game_over()

    win.fill(BLACK)
    for block in snake_body:
        pygame.draw.circle(win, GREEN, (block[0], block[1]), snake_body_size)
    
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))

    pygame.display.update()

    clock.tick(5)


pygame.quit()
