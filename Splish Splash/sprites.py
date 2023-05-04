import pygame
from settings import *
from random import choice, randint


class BG(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        bg_image = pygame.image.load('../Splish Splash/assets/environment/background.png').convert()
        full_ht = bg_image.get_height() * scale_factor
        full_wd = bg_image.get_width() * scale_factor
        full_size = pygame.transform.scale(bg_image, (full_wd, full_ht))

        self.image = pygame.Surface((full_wd * 2, full_ht))
        self.image.blit(full_size, (0, 0))
        self.image.blit(full_size, (full_wd, 0))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.position = pygame.math.Vector2(self.rect.topleft)

    def update(self, dtime):
        self.position.x -= 300 * dtime
        if self.rect.centerx <= 0:
            self.position.x = 0
        self.rect.x = round(self.position.x)


class Ground(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        self.sprite_type = 'ground'

        surf_ground = pygame.image.load(r'..\Splish Splash\assets\environment\ground.png').convert_alpha()
        self.image = pygame.transform.scale(surf_ground, pygame.math.Vector2(surf_ground.get_size()) * scale_factor)
        self.rect = self.image.get_rect(bottomleft=(0, WINDOW_HEIGHT))
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dtime):
        self.position.x -= 360 * dtime
        if self.rect.centerx <= 0:
            self.position.x = 0
        self.rect.x = round(self.position.x)


class Omen(pygame.sprite.Sprite):
    def __init__(self, groups, scaling):
        super().__init__(groups)

        self.import_frames(scaling)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midleft=(WINDOW_WIDTH / 20, WINDOW_HEIGHT / 2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.gravity = 600
        self.direction = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.jump_sound = pygame.mixer.Sound(r'..\Splish Splash\assets\sounds\jump.wav')
        self.jump_sound.set_volume(0.3)

    def import_frames(self, scaling):
        self.frames = []
        for i in range(3):
            surf = pygame.image.load(f'../Splish Splash/assets/omen/f{i}.png').convert_alpha()
            scaled_surface = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scaling)
            self.frames.append(scaled_surface)

    def apply_gravity(self, dtime):
        self.direction += self.gravity * dtime
        self.pos.y += self.direction * dtime
        self.rect.y = round(self.pos.y)

    def jump(self):
        self.jump_sound.play()
        self.direction = -400

    def animate(self, dtime):
        self.frame_index += 10 * dtime
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def rotate(self):
        rotated_omen = pygame.transform.rotozoom(self.image, -self.direction * 0.06, 1)
        self.image = rotated_omen
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dtime):
        self.apply_gravity(dtime)
        self.animate(dtime)
        self.rotate()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        self.sprite_type = 'obstacle'

        dir_choice = choice(('up', 'down'))
        surf = pygame.image.load(f'../Splish Splash/assets/obstacles/{choice((0, 1))}.png').convert_alpha()
        self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)

        x = WINDOW_WIDTH + randint(40, 100)
        if dir_choice == 'up':
            y = WINDOW_HEIGHT + randint(10, 50)
            self.rect = self.image.get_rect(midbottom=(x, y))
        else:
            y = randint(-50, -10)
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(midtop=(x, y))
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dtime):
        self.pos.x -= 400 * dtime
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -100:
            self.kill()