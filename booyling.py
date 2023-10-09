from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_shar(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed



win_width = 700
win_height = 500
FPS = 60
clock= time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption('Boyling')
background = transform.scale(image.load('FON.png'),(win_width, win_height))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))

    display.update()
