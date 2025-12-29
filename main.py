# Basic cube collision in Pygame

# Imports
import pygame

# Initialize
pygame.init()

WIDTH = 1000
HEIGHT = 800 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

fps = 60
timer = pygame.time.Clock()

# game variables
wall_thickness = 10
cube_speed = 10

# cube class
class Cube:
    def __init__(self, x_pos, y_pos, width, height, color, x_speed, y_speed, id):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.old_rect = self.rect.copy()
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.id = id

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def check_movement(self):

        # ball movement based on keys
        # self.x_speed = x_push
        # self.y_speed = y_push

        # handle wall collision
        # left wall
        if self.rect.left < wall_thickness:
            self.rect.left = wall_thickness

        # right wall
        if self.rect.right > WIDTH - wall_thickness:
            self.rect.right = WIDTH - wall_thickness

        # top wall
        if self.rect.top < wall_thickness:
            self.rect.top = wall_thickness

        # bottom wall
        if self.rect.bottom > HEIGHT - wall_thickness:
            self.rect.bottom = HEIGHT - wall_thickness


    # update pos for cube 1
    def update_pos(self, keys):
        self.old_rect = self.rect.copy()

        if keys[pygame.K_a]:
            self.rect.x -= cube_speed
        if keys[pygame.K_d]:
            self.rect.x += cube_speed
        if keys[pygame.K_w]:
            self.rect.y -= cube_speed
        if keys[pygame.K_s]:
            self.rect.y += cube_speed

    # update pos for cube 2
    def update_pos2(self, keys):
        self.old_rect = self.rect.copy()

        if keys[pygame.K_LEFT]:
            self.rect.x -= cube_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += cube_speed
        if keys[pygame.K_UP]:
            self.rect.y -= cube_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += cube_speed

# wall drawing function
def draw_walls():
    left = pygame.draw.line(screen, 'white', (0,0), (0,HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'white', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'white', (0,0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'white', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list

# handle cube collision
def handle_cube_collision(cube_a, cube_b):
    if not cube_a.rect.colliderect(cube_b.rect): # if cubes aren't colliding
        return

    # revert both cubes to their last valid pos (simple collision handling)
    cube_a.rect = cube_a.old_rect
    cube_b.rect = cube_b.old_rect


# instances of cube class
cube1 = Cube(300, 200, 50, 50, 'orange', 0, 0, 1)
cube2 = Cube(600, 400, 100, 100, 'red', 0, 0, 2)


# main game loop
run = True 
while run:
    timer.tick(fps)
    screen.fill('black')

    # draw walls
    walls = draw_walls()

    # get keyboard input
    keys = pygame.key.get_pressed()

    # move cubes
    cube1.update_pos(keys)
    cube2.update_pos2(keys)

    # handle wall collision
    cube1.check_movement()
    cube2.check_movement()

    # collision response
    handle_cube_collision(cube1, cube2)

    # draw cubes
    cube1.draw()
    cube2.draw()

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if player quits
            run = False # end game
    
    pygame.display.flip() # draw onto screen
pygame.quit() # end program

