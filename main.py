import pygame, sys, random

pygame.init()

clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 400
FPS = 60

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN = pygame.surface.Surface((WIDTH,HEIGHT))

pygame.display.set_caption("Lil Tuan Nghia")

map = pygame.image.load("./Asset/other/map.png")

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.state = "idle"
        self.id = 1

        self.game_over = False
        self.asset_dir = f"./Asset/dino/Dino{self.id}.png"

        self.image = pygame.image.load(self.asset_dir)
        self.rect = self.image.get_rect()
        self.rect.topleft = [22, 228]

        self.idle_time = 0
        self.duck_time = 0
        self.vel = 0
        self.jump_state = 0
        self.jump = False

    def update(self):
        if self.state == "start":
            self.id = 0

        elif self.state == "idle":
            if self.idle_time < 4:
                self.id = 1
                self.idle_time += 1
            elif self.idle_time < 10:
                self.id = 2
                self.idle_time += 1
            else:
                self.idle_time = 0
                self.id = 1

        elif self.state == "jump":
            self.id = 3

        elif self.state == "duck":
            if self.duck_time < 4:
                self.id = 4
                self.duck_time += 1
            elif self.duck_time < 10:
                self.id = 5
                self.duck_time += 1
            else:
                self.duck_time = 0
                self.id = 4

        if self.state == "duck":
            self.rect.y = 262
            self.state = "idle"
        elif self.state == "idle":
            self.rect.y = 228

        self.asset_dir = f"./Asset/dino/Dino{self.id}.png"
        self.image = pygame.image.load(self.asset_dir)

        if self.rect.y == 227 or self.rect.y == 224:
            self.jump_state = 0
            self.rect.y = 228
            self.state = "idle"

        if not self.game_over:
            key = pygame.key.get_pressed()

            if key[pygame.K_w] or key[pygame.K_SPACE] or key[pygame.K_UP]:
                if self.jump_state == 0 and not self.state == "jump":
                    self.vel = -20
                    self.jump_state = 1
                    self.state = "jump"
            elif key[pygame.K_s] or key[pygame.K_LSHIFT] or key[pygame.K_DOWN]:
                if not self.state == "duck" and self.jump_state == 0:
                    self.state = "duck"
                    print("Duck!")

        if self.state == "jump" and self. jump_state != 0:
            if self.jump_state == 1:
                self.vel += 1
            if self.vel == 1 and self.jump_state == 1:
                self.jump_state = 2
            if self.jump_state == 2:
                self.vel += 1
            self.rect.y += self.vel

player_gr = pygame.sprite.Group()

player = Player()

player_gr.add(player)

game_over = False

while True:

    DISPLAY.fill(pygame.color.Color("white"))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    DISPLAY.blit(map,[0,300])
    player_gr.update()
    player_gr.draw(DISPLAY)

    clock.tick(FPS)
    pygame.display.update()
