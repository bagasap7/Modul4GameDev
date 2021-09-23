#Part E
import pygame
import sys
 
WIDTH,HEIGHT = 400, 400 # deklarasi layar yang akan dimunculkan
TITLE = "Smooth Movement"

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT)) #untuk menampilkan layar game
pygame.display.set_caption(TITLE)#untuk menampilkan judul di layar
clock = pygame.time.Clock() #berfungsi untuk memberikan waktu pada game saat di run
#==============================================================#

font_color = (0, 150, 250)
font_obj = pygame.font.Font('ariblk.ttf', 20) #berfungsi untuk memasukkan font dari local disk
text_obj = font_obj.render("Bagas Aditya Pramudana", True, font_color) #berfungsi untuk menampilkan font

#Part D
class Player:
    def __init__(self, x, y): #definisikan kordinant x dan y
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        # self.image = pygame.image.load(".png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (100, 60)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
        # self berfungsi untuk menyatakn variabel di dalam kelas Player
#==============================================================#

#Part F
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect) 
#==============================================================#

#Part A
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed and self.x >= 0: #berfungsi untuk memberikan batasan kepada objek agar tidak keluar dari laayr
            self.velX = -self.speed
        # berfungsi untuk memberikan batasan kepada objek agar tidak keluar dari laayr
        if self.right_pressed and not self.left_pressed and self.x <= 400:
            self.velX = self.speed
        # berfungsi untuk memberikan batasan kepada objek agar tidak keluar dari laayr
        if self.up_pressed and not self.down_pressed and self.y >= 0:
            self.velY = -self.speed
        # berfungsi untuk memberikan batasan kepada objek agar tidak keluar dari laayr
        if self.down_pressed and not self.up_pressed and self.y <= 400:
            self.velY = self.speed
            
        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)
#============================================================================#

#Part B
player = Player(WIDTH/2, HEIGHT/2)

while True: #berfungsi sebagai looping

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT: #gerakan ke kiri
                player.left_pressed = True
             if event.key == pygame.K_RIGHT: #gerakan ke kanan
                player.right_pressed = True
             if event.key == pygame.K_UP: #gerakan ke atas
                player.up_pressed = True
             if event.key == pygame.K_DOWN: #gerakan ke bawah
                player.down_pressed = True
         #berfungsi untuk memberikan gerakan kepada objek       
        if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT:
                player.left_pressed = False
             if event.key == pygame.K_RIGHT :
                player.right_pressed = False 
             if event.key == pygame.K_UP:
                player.up_pressed = False
             if event.key == pygame.K_DOWN:
                player.down_pressed = False
        #berfungsi untuk memberikan gerakan kepada objek
#============================================================================#

#Part C
    win.fill((255,255,255)) #membrikan warna pada background di layar
    pygame.draw.rect(win, (255, 0, 0), (0, 0, 400, 400), 1) #memberikan border di layar
    win.blit(text_obj, (50, 10))
    player.draw(win) #berfungsi memunculkan player

    player.update() #berfungsi mengupdate game
    pygame.display.flip()

    clock.tick(120) #memberikan waktu berjalan waktu

