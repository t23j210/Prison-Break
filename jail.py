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
        self.img_jail = pygame.image.load("res/jail/jail_no.png")
        self.zoom_under_bed = pygame.image.load("res/jail/zoom_under_bed.png")
        self.zoom_key = pygame.image.load("res/jail/zoom_key.png")
        self.close_safe = pygame.image.load("res/jail/zoom_under_bed(2).png")
        self.zoom_toilet = pygame.image.load("res/jail/zoom_toiret.png")
        self.item_diary = pygame.image.load("res/jail/item_diary.png")
        self.item_key = pygame.image.load("res/jail/item_key.png")
        self.item_page = pygame.image.load("res/jail/item_page.png")
        self.zoom_state = 0
        
    def click_event(self, x, y):
        if self.zoom_state == 0:
            if (555 < x < 650) and (580 < y < 750):
                self.zoom_state = 1
            elif (240 < x < 300) and (520 < y < 650):
                self.zoom_state = 2
            else:
                self.zoom_state = 0
        elif self.zoom_state == 1:
            is_inside = (162 < x < 918) and (324 < y < 716)
            if not is_inside:
                self.zoom_state = 0
        elif self.zoom_state == 2:
            is_inside = (333 < x < 675) and (182 < y < 710)
            if not is_inside:
                self.zoom_state = 0

    def draw(self):
        self.screen.blit(self.img_room, (0,0))
        if self.zoom_state == 1:
            self.screen.blit(self.zoom_under_bed, (0,0))
        elif self.zoom_state == 2:
            self.screen.blit(self.zoom_key, (0,0))
