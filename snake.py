import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self) :
        #self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)] # we have to chnage this because as the snake starts moving it moves inside itself then it moves so we are changing it so that the game don't over when the snake just started moving
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0,0) # as we given (1,0) it means it will move to the right
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body): # here we only get the information about the single block but we want all the information we need the block before and the block after so we use enumerate, so the enumerate does is that it gives the index on what object we are inside of our list so index,block index is the index of object inside the list and block is the actual object
               block_rect = pygame.Rect(block.x * cell_size,block.y * cell_size,cell_size,cell_size)  # example index = 0 block = Vector2
               if index == 0:
                   screen.blit(self.head,block_rect) # her the surface is self.head_right and we need to put the surface in the specific postion so their is block_rect
               elif index == len(self.body) -1:
                   screen.blit(self.tail,block_rect)
               else:
                   previous_block: Vector2 = self.body[index +1] - block
                   next_block = self.body[index -1] - block
                   if previous_block.x == next_block.x: # example if [4,5],[4,6],[4,7] here the x coordinate are same so the snake is moving horizontally
                       screen.blit(self.body_vertical, block_rect)
                   elif previous_block.y == next_block.y:
                       screen.blit(self.body_horizontal, block_rect)
                   else:
                       if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                           screen.blit(self.body_tl,block_rect)





               #else:
                #pygame.draw.rect(screen,(150,100,100),block_rect)




    def update_tail_graphics(self):
            tail_relation = self.body[-2] - self.body[-1] #her we want ro see the last one and the last one that comes before it
            if tail_relation == Vector2(1, 0):
                self.tail = self.tail_left
            elif tail_relation == Vector2(-1, 0):
                self.tail = self.tail_right
            elif tail_relation == Vector2(0, 1):
                self.tail = self.tail_up
            elif tail_relation == Vector2(0, -1):
                self.tail = self.tail_down

    # for block in self.body: # here we only get the information about the single block but we want all the information we need the block before and the block after so we use enumerate
    # block_rect = pygame.Rect(block.x * cell_size,block.y * cell_size,cell_size,cell_size)
    # pygame.draw.rect(screen,(183,111,122),block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0] # if we want to know about which direction the snake is moving so we just did a small vector substraction between the elemwnt 0 and element 1 of the list so we will know which direction the snake is moving
        if head_relation == Vector2(1,0):
            self.head = self.head_left # we put a hard if statement confirming the head direction and implementing the snake head surface direction.
        elif head_relation == Vector2(-1,0):
            self.head = self.head_right
        elif head_relation == Vector2(0,1):
            self.head = self.head_up
        elif head_relation == Vector2(0,-1):
            self.head = self.head_down

        # her we will take the first 2 element of the list and keep it and then insert a element at the starting of the list which will have the direction to move
    # similarly this process will continue take the first 2 element of the list and them insert the first element to the desired direction, and the first element will be the previous list first element + the direction


    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] # here we are not removing any block we are taking 3 elements of the list so as we add another element in the front the snakes size will increase
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] # here first we need to copy the body of the snake but we only want the 2 element      Vector2(5,10),Vector2(6,10),Vector2(7,10)    so here only the  Vector2(5,10),Vector2(6,10) will remain ### removing the last element
            body_copy.insert(0,body_copy[0] + self.direction) # insert the elment at the  every beginning so here is (0,body_copy[0] + self.direction) so 0 index, and the value is body_copy[0] + self.direction . the body_copy[0] is the first elemenmt of the list and + self_direction which addes the direction to the list   ### inserting the head +direction
            self.body = body_copy[:] # saving the deleated and new inserted list to the original list

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)



class FRUIT:
    def __init__(self):
        self.randamize()
        # create an x and y position
        # draw a square
        #self.x = random.randint(0,cell_no - 1) # this the no of pixels fron x
        #self.y = random.randint(0,cell_no - 1) # this the no of pixels fron y
        #self.pos = Vector2(self.x,self.y) # we used vertor logic to move and locate
    def draw_fruit(self):
        # create a rectangle
        # draw the rectangle
        # we can multiply the cell piexl with the cell size to change the postion efficiently
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        screen.blit(apple,fruit_rect) # when ever we add a image in python it will be in its own surface so we use here apple as a surface
        #pygame.draw.rect(screen,(126,166,140),fruit_rect) #we have a fruit class so we dont need this rect
    def randamize(self): # it is a function, in main it will be called with a condition randamize the fruit positon after the snake its the fruit
        self.x = random.randint(0, cell_no - 1)
        self.y = random.randint(0, cell_no - 1)
        self.pos = Vector2(self.x, self.y)


# this main class will be the main fuction of the game which will initize and run the snake and fruit and the logic
class MAIN:
    def __init__(self):
        self.snake = SNAKE() # creating the snake object
        self.fruit = FRUIT() # creating the fruit object

    def update(self):
        self.snake.move_snake() # moving the snake
        self.check_collision() # check of collision
        self.check_fail() # cheacking where is the snake's head is it fail or not

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit() # drawing the fruit
        self.snake.draw_snake() # drawing the snake
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randamize() # reposition our fruit after the snake eats the fruit
            self.snake.add_block() # add a element to the snake as it eats the fruit
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos: # if the fruit occurs inside the snake it will be randamize easily
                self.fruit.randamize() # so our fruit will never be at the top of the body

    def check_fail(self): # their is a condition we put that snake's head or  self.snake.body[0] is between 0 <= or > cell_no then the sanke will be alive or else not
        if not 0 <= self.snake.body[0].x < cell_no: # now vector cannot be compared with the normal numbers do we use only the x coordinate to find where is the snake's head
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_no:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167,209,61)

        for row in range(cell_no):
            if row % 2 == 0:
                for col in range(cell_no): # here col is just a int like for i in range(___) its just a int that changes repeatedly
                    if col % 2 == 0: # putting it on the evev postions only
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

            else:
                for col in range(cell_no): # here col is just a int like for i in range(___) its just a int that changes repeatedly
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3) # we will use the length of the snake as a score so len function and we -3 because the size of the snake is 3 at starting
        score_surface = game_font.render(score_text,True,(56,74,12))# to display over the screen we use render and the true makes it a bit more beatiful text
        score_x = int(cell_size * cell_no - 60)
        score_y = int(cell_size * cell_no - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y)) # put the score_surface inside the score_rect and the postion wil be determined by score_x and score_y
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        screen.blit(apple,apple_rect)
        screen.blit(score_surface,score_rect)



pygame.mixer.pre_init(44100,-16,2,512) # making the sound with no delays
pygame.init()
cell_no = 20
cell_size = 40
screen = pygame.display.set_mode((cell_no*cell_size,cell_no*cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha() #load imports the image in python
game_font = pygame.font.Font(None,25)

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT # custom event that we will be in control of
pygame.time.set_timer(SCREEN_UPDATE,150) # this is the trigger of our custom event , so the screen will be refreshed ever 150 ms, so every 150 ms the SCREEN_UPDATE event will be triggered

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()


        if event.type == pygame.KEYDOWN: # this is a event that will take the input from the keyboard
            if event.key == pygame.K_UP: # K_UP pygame take theinput as when we press the up key of our key board
                if main_game.snake.direction.y != 1: # condition cannot go reverse
                    main_game.snake.direction = Vector2(0,-1) # Vector2(0,-1) means if up key is pressed then the snake will go up
            if event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)


    screen.fill((175,215,70))
    main_game.draw_elements() # taking from main function
    pygame.display.update()
    clock.tick(60)
