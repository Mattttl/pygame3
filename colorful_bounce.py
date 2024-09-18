import pygame
import random

from pygame.sprite import Group

pygame.init()

Sprite_Color_Change_Event = pygame.USEREVENT +1
Backround_Color_Change_Event= pygame.USEREVENT + 2

Blue = pygame.Color('blue')
LBlue = pygame.Color('lightblue')
DBlue = pygame.Color('darkblue')
Yellow = pygame.Color('yellow')
Magenta = pygame.Color('magenta')
Orange = pygame.Color('orange')
White = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit= False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        
        if boundary_hit:
            pygame.event.post(pygame.event.Event(Sprite_Color_Change_Event))
            pygame.event.post(pygame.event.Event(Backround_Color_Change_Event))
    def change_color(self):
        self.image.fill(random.choice([Yellow,Magenta,Orange,White]))
def change_backround_color():
    global bg_color
    bg_color = random.choice([Blue,LBlue,DBlue])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(White,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Bounce")
bg_color = Blue
screen.fill(bg_color)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == Sprite_Color_Change_Event:
            sp1.change_color()
        elif event.type == Backround_Color_Change_Event:
            change_backround_color()
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit()