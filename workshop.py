# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Workshop(Room_Base):
    def __init__(self, screen, lock_flag):
        super().__init__(screen, lock_flag)
        self.img_room = pygame.image.load("res/workshop/workshop.png")
        self.zoom_drill_no_needlever.png = pygame.image.load("res/workshop/zoom_drill_no_needlever.png")
        self.zoom_no_drillver.png = pygame.image.load("res/workshop/zoom_no_drillver.png")
        self.zoom_needle.png = pygame.image.load("res/workshop/zoom_needle.png")
        self.zoom_no_needlever.png = pygame.image.load("res/workshop/zoom_no_needlever.png")
        self.zoom_board.png = pygame.image.load("res/workshop/zoom_board.png")
        
    def click_event(self, x, y):
        pass
            
    def draw(self):
        self.screen.blit(self.img_room, (0, 0))
        if self.lock_flag[3] == False:
            slef.screen.blit(slef.close_safe, [440, 213])
