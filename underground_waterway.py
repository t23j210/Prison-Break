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
        self.zoom_underground_waterway = pygame.image.load("res/underground_waterway/zoom_underground_waterway.png")
        self.zoom_door2 = pygame.image.load("res/underground_waterway/zoom_door2.png")
        self.zoom_password = pygame.image.load("res/underground_waterway/zoom_password.png")
        self.item_flame = pygame.image.load("res/underground_waterway/item_flame.png")
        self.zoom_state = 0
        
    def click_event(self, x, y):
        if self.zoom_state == 0:
            if (507 < x < 564) and (296 < y < 392):
                self.zoom_state = 1
            elif (348 < x < 692) and (531 < y < 748):
                self.zoom_state = 2
            else:
                self.zoom_state = 0
        elif self.zoom_state == 1:
            if (574 < x < 646) and (342 < y < 448):
                self.zoom_state = 3
            else:
                self.zoom_state = 0
        elif self.zoom_state == 2:
            is_inside = (175 < x < 910) and (243 < y < 643)
            if not is_inside:
                self.zoom_state = 0
        elif self.zoom_state == 3:
            is_inside = (378 < x < 696) and (128 < y < 669)
            if not is_inside:
                self.zoom_state = 1
                
    def draw(self):
        self.screen.blit(self.img_room, (0, 0))
        if self.zoom_state == 1:
            self.screen.blit(self.zoom_door2, (0, 0))
        elif self.zoom_state == 2:
            self.screen.blit(self.zoom_underground_waterway, (0, 0))
        elif self.zoom_state == 3:
            self.screen.blit(self.zoom_password, (0, 0))