import pygame, sys, time
from settings import *
from sprites import BG, Ground, Omen, Obstacle


class Game:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Splish Splash')
        self.clock = pygame.time.Clock()
        self.active = True

        bg_height = pygame.image.load(r'..\Splish Splash\assets\environment\background.png').get_height()
        self.scaling = WINDOW_HEIGHT / bg_height

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        BG(self.all_sprites, self.scaling)
        Ground([self.all_sprites, self.collision_sprites], self.scaling)
        self.omen = Omen(self.all_sprites, self.scaling / 1.7)

        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

        self.font = pygame.font.Font(r'..\Splish Splash\assets\font\Spongeboy Me Bob.ttf', 40)
        self.score = 0
        self.start_offset = 0

        self.surf_menu = pygame.image.load(r'..\Splish Splash\assets\ui\omen_menu.png').convert_alpha()
        self.rect_menu = self.surf_menu.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3))

    def collisions(self):
        if pygame.sprite.spritecollide(self.omen, self.collision_sprites, False, pygame.sprite.collide_mask) \
                or self.omen.rect.top <= 0:
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type == 'obstacle':
                    sprite.kill()
            self.active = False
            self.omen.kill()

    def game_score(self):
        if self.active:
            self.score = (pygame.time.get_ticks() - self.start_offset) // 1250
            y = WINDOW_HEIGHT / 10
        else:
            y = WINDOW_HEIGHT / 3 + (self.rect_menu.height / 1.5)

        score_surf = self.font.render(str(self.score), True, 'mintcream')
        score_rect = score_surf.get_rect(midtop=(WINDOW_WIDTH / 2, y))
        self.win.blit(score_surf, score_rect)

    def run(self):
        last_time = time.time()
        while True:

            dtime = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.active:
                            self.omen.jump()
                        else:
                            self.omen = Omen(self.all_sprites, self.scaling / 1.7)
                            self.active = True
                            self.start_offset = pygame.time.get_ticks()

                if event.type == self.obstacle_timer and self.active:
                    Obstacle([self.all_sprites, self.collision_sprites], self.scaling * 1.1)

            self.win.fill('black')
            self.all_sprites.update(dtime)
            self.all_sprites.draw(self.win)
            self.game_score()

            if self.active:
                self.collisions()
            else:
                self.win.blit(self.surf_menu, self.rect_menu)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
