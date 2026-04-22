import pygame
import random
##
pygame.init() # import and start pygame activity

W = 720
H = 720 # screen config stuff
grid_size = 18
cell_size = W/grid_size

fruit_pos = [0,0]
snake = [] # the snake array
snake_dir = [1,0] # x y velocitys
state = 1 # states of the game
# 1 means running, -1 means lose, 2 means victory
def create_snake(x, y): # create the snake
    if x < 3:
        raise ValueError("X inválido, x >= 3");

    snake.append([x-3,y])
    snake.append([x-2,y]) # create the snake
    snake.append([x-1,y])
    snake.append([x,y])
def render(): # render the game
    for x in range(grid_size):
        for y in range(grid_size):
            if [x,y] == fruit_pos:
                pygame.draw.rect(screen, (255,0,0), (cell_size*x, cell_size*y, cell_size, cell_size))
                continue;
            
            for i in range(len(snake)): # if cell has snake, draw snake
                if snake[i] == [x,y]:
                    pygame.draw.rect(screen, (0,80 + (255-80)*i / len(snake),0), (cell_size*x, cell_size*y, cell_size, cell_size))
def step():
    global state
    first_piece = snake[0]

    for i in range(len(snake)):
        if i < len(snake)-1:
            snake[i] = snake[i+1]
        else:
            snake[i] = [snake[i][0] + snake_dir[0], snake[i][1] + snake_dir[1]]
            if snake.count(snake[i]) >= 2:
                state = -1
                return

            if snake[i][0] > grid_size-1:
                snake[i][0] = 0
            elif snake[i][0] < 0:
                snake[i][0] = grid_size-1
            elif snake[i][1] > grid_size-1:
                snake[i][1] = 0
            elif snake[i][1] < 0:
                snake[i][1] = grid_size-1
        
    
    if fruit_pos in snake:
        snake.insert(0, first_piece)
        generate_fruit()
    
def handle_keys_down(e):
    global snake_dir
    match e:
        case pygame.K_s:
            snake_dir = [0,1]
        case pygame.K_w:
            snake_dir = [0,-1]
        case pygame.K_a:
            snake_dir = [-1,0]
        case pygame.K_d:
            snake_dir = [1,0]
def generate_fruit():
    is_on_snake = True
    global fruit_pos
    while is_on_snake:
        x = random.randint(0,grid_size)
        y = random.randint(0,grid_size)

        if not [x,y] in snake:
            is_on_snake = False
            fruit_pos = [x,y]

screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
running = True

create_snake(5,5)
generate_fruit()

while running and state == 1: # while running do all stuff
    for event in pygame.event.get(): # handling quit event
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            handle_keys_down(event.key)
    screen.fill("black") # clean the screen

    #

    render()
    step()

    #

    pygame.display.flip() # update the display
    clock.tick(15) # set to 60 fps

pygame.quit() # end pygame activity