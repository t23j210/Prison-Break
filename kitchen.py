# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Kitchen(Room_Base):
    def __init__(self, screen, lock_flag):
        super().__init__(screen, lock_flag)
        self.img_room = pygame.image.load("res/kitchen/kitchen.png")
        self.zoom_refrigerator = pygame.image.load("res/kitchen/zoom_refrigerator.png")
        self.item_battery = pygame.image.load("res/kitchen/item_battery.png")
        self.item_page2 = pygame.image.load("res/kitchen/item_page2.png")
        self.zoom_state = 0
        
    def click_event(self, x, y):
        if self.zoom_state == 0:
            if (90 < x < 170) and (265 < y < 405):
                self.zoom_state = 1
            else:
                self.zoom_state = 0
        elif self.zoom_state == 1:
            is_inside = (333 < x <685) and (55 < y <640)
            if not is_inside:
                self.zoom_state = 0
            
    def draw(self):
        self.screen.blit(self.img_room, (0,0))
        if self.zoom_state == 1:
           self.screen.blit(self.zoom_refrigerator, (0,0))