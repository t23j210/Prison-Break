# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Jail(Room_Base):
    def __init__(self, screen, lock_flag):
        super().__init__(screen, lock_flag)
        self.img_room = pygame.image.load("res/jail/jail.png")
        self.zoom_under_bed = pygame.imge.load("res/jail/zoom_under_bed.png")
        self.zoom_key.png = pygame.imge.load("res/jail/zoom_key.png")
        self.close_safe = pygame.image.load("res/jail/zoom_under_bed(2).png")
        self.zoom_state = 0
        
    def click_event(self, x, y):
        if self.zoom_state == 0;
            if 555 < x < 650 and 580 < y < 750:
                self.zoom_state = 1
            elif 240 < 300 and 520 < y < 650:
                self.zoom_state = 2
            else:
                self.zoom_state = 0
        elif self.zoom_state == 1:
            if 100 < x < 200 and 100 < y < 200:
                self.zoom_state = 1
            else:
                self.zoom_state = 0
        elif self.zoom_state == 2:
            if 100 < x < 200 and 100 < y < 200:
                self.zoom_state = 2
            else:
                self.zoom_state = 0
                
    def draw(self):
        self.screen.blit(self.img_room, (0, 0))
        if self.zoom_state == 1:
            self.screen.blit(self.zoom_under_bed, (194, 360))
        elif self.zoom_state == 2:
            self.screen.blit(self.zoom_key, (495, 188))
        if self.lock_flag[0] == False:
            self.lock_screen.blit(self.close_safe, [440,213])
