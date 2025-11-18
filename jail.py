# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Jail(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
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
        self.item_sdriver_state = 0
        
    def click_event(self, x, y):
        if self.zoom_state == 0:
            if (555 < x < 650) and (580 < y < 750):
                self.zoom_state = 1
            elif (240 < x < 300) and (520 < y < 650):
                if self.item_get[1] == True:
                    self.zoom_state = 3
                else:
                    self.zoom_state = 2
            else:
                self.zoom_state = 0
        elif self.zoom_state == 1:
            is_inside = (162 < x < 918) and (324 < y < 716)
            if not is_inside:
                self.zoom_state = 0
        elif self.zoom_state == 2:
            if (478 < x < 539) and (470 < y < 604):
                if self.item_sdriver_state == 0:
                    self.item_sdriver_state = 1
                    self.item_get[1] = True
                self.zoom_state = 3
            else:
                self.item_sdriver_state = 0
                self.zoom_state = 0
        elif self.zoom_state == 3:
            if (0 < x < 1024) and (0 < y < 768):
                self.zoom_state = 0
    def draw(self):
        self.screen.blit(self.img_room, (0,0))
        if self.zoom_state == 1:
            self.screen.blit(self.zoom_under_bed, (0,0))
        elif self.zoom_state == 2:
            self.screen.blit(self.zoom_key, (0, 0))
        elif self.zoom_state == 3:
            self.screen.blit(self.zoom_toilet, (0, 0))
