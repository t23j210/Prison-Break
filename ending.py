# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:23:51 2020

@author: Ozaki
"""
import pygame
from room_base import Room_Base

class Ending(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.screen = screen
        self.lock_flag = lock_flag
        self.item_get = item_get
        self.item_use = item_use
        self.end = pygame.image.load("res/end/end.png")
        self.next_room = 6
        self.zoom_state = 0
    

    def click_event(self, x, y):
        if (0 < x < 1024) and (0 < y < 768):
            self.next_room = 0
    
    def draw(self):
        self.screen.blit(self.end, (0, 0))

    def next_state(self):
        next = self.next_room #次の部屋
        self.next_room = 6
        return next
