import pygame
from support import import_folder

class ParticleEfect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        #Exp
        self.frameSpeedUnc = 1.0
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        #Actual state of the player is jumping
        if type == 'Jump':
            self.frames = import_folder('./graphics/Sprites/Dust_Part/jump')
        #When player that is on air lands to a tile
        if  type == 'Land':
            #import Land Particles
            self.frames = import_folder('./graphics/Sprites/Dust_Part/land')
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]
           # self.kill()
#Update all the methods of the player scri
    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift
