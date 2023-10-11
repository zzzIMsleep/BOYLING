#https://github.com/zzzIMsleep/BOYLING.git
from pygame import *
from random import randint
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
class Ball(GameSprite):
    def update(self):
        if e.type == KEYUP:
            if e.key==K_SPACE:
                self.rect.y -= self.speed
                self.rect.x -= self.speed
                if self.rect.y <= 0:
                    self.kill()
                    self.speed=0
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
finish = False
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(' Player 1 LOSE!', True, (180,0,0))
y_pla = 350
sbeiKEGs = sprite.Group()
sbeiKEG = Ball('boll1.png', 250, y_pla, randint(1,10), 105, 75)
sbeiKEGs.add(sbeiKEG)

 

kegs = sprite.Group()
X_KEG=150
Y_KEG=50
for i in range(1,7):
    KEG = GameSprite('KEGLA.png', X_KEG, Y_KEG,10, 55, 100 )
    X_KEG+=55
    Y_KEG+=10
    kegs.add(KEG)
kegl_score=0
font.init()
font1 = font.SysFont('Times New Roman', 40)
win = font1.render('СТРАЙК ',1,(123,46,86))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key==K_k: #создать мяч
                sbeiKEG = Ball('boll1.png', 250, y_pla, randint(1,10), 105, 75)
                sbeiKEGs.add(sbeiKEG)
                
                

    
       

                
    window.blit(background, (0, 0))
    sbeiKEGs.update()
    sbeiKEGs.draw(window)
    kegs.update()
    kegs.draw(window)
    sprites_list = sprite.groupcollide(sbeiKEGs, kegs, False, True)
    for keg in sprites_list:
        kegl_score = kegl_score + 1
    if kegl_score ==6:
        window.blit(win,(200,200))
    text = font1.render('Счёт '+str(kegl_score),1,(23,246,86))
    window.blit(text,(0,10))
    display.update()
    time.delay(50)

