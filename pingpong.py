from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x,player_y,player_speed,wight,height):
        super().__init__()
        self.image = transform.scale(image.load(player.image),(wight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y



    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#game scene:
back = (200,255,255)
win_width =600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game =False
    display.update()
    clock.tick(FPS)

