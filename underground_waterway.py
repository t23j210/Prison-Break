# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Underground_waterway(Room_Base):
    def __init__(self, screen, lock_flag):
        super().__init__(screen, lock_flag)
        self.img_room = pygame.image.load("res/underground_waterway/underground_waterway.png")
        self.zoom_underground_waterway("res/zoom_underground_waterway.png")
        self.zoom_door2("res/zoom_door2.png")
        self.zoom_password("res/zoom_password.png")
        self.zoom_state = 0
        
    def click_event(self, x, y):
        if
            
    def draw(self):
        self.screen.blit(self.img_room, (0, 0))
        if self.zoom == 1:
            self.screen.
