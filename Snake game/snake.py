import pygame

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

direction = "RIGHT"

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
    print("-------------")
    print(snake_pos)
    snake_pos[0] = snake_pos[0] % width
    snake_pos[1] = snake_pos[1] % height
    print(snake_pos)
    
    snake_body.insert(0, [snake_pos[0], snake_pos[1]])
    snake_body.pop()

    win.fill(BLACK)
    for block in snake_body:
        pygame.draw.circle(win, GREEN, (block[0], block[1]), snake_body_size)
    

    pygame.display.update()

    clock.tick(5)


pygame.quit()
