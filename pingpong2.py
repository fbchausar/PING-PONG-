# Mengimpor semua modul dari pygame
from pygame import*

#kelas induk untuk sprite
class Gamesprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,wight,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight,height))
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.player_y))
#kelas player yang merupakan turunan dari gamesprite
class Player(Gamesprite):
    def update_r(self):# update pergerakan ke kanan
        keys = key.get_pressed()#mendapat status tombol yang ditekan
        if keys[K_UP] and self.rect.rect.y >5:
            self.rect.y +=self.speed#menggerakkan sprite keatas
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed#menggerakkan sprite ke bawah
#update pergerakan pemain ke kiri(w,s)
    def update_1(self):
        keys = keys.get_pressed()#mendapat status tombol yg ditekan
        #jika tombol w ditekan dan spriyte msih diatas layar
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed#menggerakkan sprite keatas
        #jika tombol s ditekan dansprite masih dibawah layar
        if keys[K_s] and self.rect.y < win_height -80:
            self.rect.y += self.speed#menggerakkan sprite kebawah
#pengaturan untuk latar belakang dan ukuran layar
back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

#variabel utk mengontrol status permainan
game = True #flag utk status permainan, game dimulai
finish = False #flag utk status selesai, permainan blm selesai
clock = time.clock() #menyiapkan objek clock untuk mengontrol FPS
FPS = 60# Frame per second, kecepetan permainan

#membuat objek raket (player) dan bola(gamesprite)
racket1 = Player('racket_png', 30,200,4,50,150) #pemain 1
racket2 = Player('racket_png, ',520,200,4,50,150) # pemain 2
ball = Gamesprite('tenis_ball.png',200,200,4,50,50) #bola

#inisialisasi font untuk menampilkan teks
font.init() #menginisialisai modul font
font = font.Font(None,35)#membuat font dgn ukuran 35
lose1 = font.render('PLAYER 1 LOSE', True,(180,0,0))#teks jika pemain 1 kalah
lose2 = font.render('PLAER 2 LOSE', True, (180,0,0))#teks jika pemain 2 kalah

speed_x = 3 #kecepatan bola secara horizontal
speed_y = 3 #kecepatan bola secara vertikal

#loop utama dalam permainan
while game:
    for e in event.get(): #memeriksa semua event yang terjadi
        if e.type == QUIT:#jika pengguna menekan tombol keluar
            game = False#mengakhiri game
    
        if finish != True: #jika permainan belum selesai
            window.fill(back)#mengisi ulang layar dgn latr belakang
            racket1.update_1()#memperbarui posisis raket 1
            racket2.update_r()#memperbarui posisi raket 2
            ball.rect.x += speed_x#menggerakkan bola kearah sumbu x
            ball.rect.y += speed_y#menggerakkan bola kearah sumbu y
#jika bola bertabrakan dgn raket 1 atau 2
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1 #membalik arah bola kearah sumbu x
            speed_y *= 1 #membiarkan arah bola pada sumbu y tetap


#jika bola menyentuh batas atas atau bawah laayar, balikkan arah bola eacara vertikal
        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            speed_y *= -1 #membalik arah bola pada sumbu y
        
        #jika bola melewati raket 1(kiri), pemain 1 kalah
        if ball.rect.x < 0:
            finish = True#menandakan permainan selsai
            window.blit(lose1,(200,200))#menampilkan tulisan 'PLAYER 1 LOSE'
            game_over = True #status game over
        
        #jika bola melewati raket 2(kanan), player 2 kalah
        if ball.rect.x > win_width:
            finish = True#menandakan permainan selesai
            window.blit(lose2,(200,200))#menampilkan tulisan'PLAYER 2 LOSE'
            game_over = True#status game over
        
        racket1.reset()#mengembalikan raket 1
        racket2.reset()#mengembalikan raket2
        ball.reset()#mengembalikan bola

    #memperbarui tampilan layar
    display.update()
    clock.tick(FPS)


     





