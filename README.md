# BOYLING
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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.y < win_height-80:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.y > 5:
            self.rect.x -= self.speed

win_width = 700
win_height = 500
FPS = 60
clock= time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption('kegloFON')
background = transform.scale(image.load('FONDLAboylinga.jpg'),(win_width, win_height))
run = True
speed_x =3
speed_y =3
finish = False
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(' Player 1 LOSE!', True, (180,0,0))
y_pla = 350
sbeiKEG = Player('boll1.png', 250, y_pla, 10, 105, 75)
 

kegs = sprite.Group()
X_KEG=150
Y_KEG=50
for i in range(1,7):
    KEG = GameSprite('KEGLA.png', X_KEG, Y_KEG,10, 55, 100 )
    X_KEG+=55
    Y_KEG+=10
    kegs.add(KEG)


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key==K_SPACE:
                sbeiKEG.rect.y -= sbeiKEG.speed
                if sbeiKEG.rect.y <= 0:
                    sbeiKEG.kill()


                
    window.blit(background, (0, 0))
    kegs.draw(window)




    
    sbeiKEG.reset()
    KEG.reset()
    sbeiKEG.update_l()
    display.update()
    time.delay(50)
