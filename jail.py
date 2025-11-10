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
        self.close_safe = pygame.image.load("res/jail/zoom_under_bed(2)")
        
    def click_event(self, x, y):
        pass
            
    def draw(self):
        self.screen.blit(self.img_room, (0, 0))
        if self.lock_flag[0] == False:
            self.lock_screen.blit(self.close_safe, [440,213])
