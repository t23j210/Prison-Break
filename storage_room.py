# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Storage_room(Room_Base):
    def __init__(self, screen, lock_flag):
        super().__init__(screen, lock_flag)
        self.img_room1 = pygame.image.load("res/storage_room/storage_room.png")
        self.img_room2 = pygame.image.load("res/storage_room/storage_room_no.png")
        self.zoom_door = pygame.image.load("res/storage_room/zoom_door1.png")
        self.zoom_state = 0
        
    def click_event(self, x, y):
        if self.zoom_state == 0:
            if (490 < x < 615) and (260 < 390):
                self.zoom_state = 1
                
        else:
            is_inside = (170 < x <890) and (10 < y <750)
            if not is_inside:
                self.zoom_state = 0
            
    def draw(self):
       if self.zoom_state == 0:
           self.screen.blit(self.img_room1, (0,0))
       else:
           self.screen.blit(self.zoom_door, (0,0))