# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Workshop(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.img_room = pygame.image.load("res/workshop/workshop.png")
        self.zoom_drill_no_needlever = pygame.image.load("res/workshop/zoom_drill_no_needlever.png")
        self.zoom_no_drillver = pygame.image.load("res/workshop/zoom_no_drillver.png")
        self.zoom_needle = pygame.image.load("res/workshop/zoom_needle.png")
        self.zoom_no_needlever = pygame.image.load("res/workshop/zoom_drill_no_needlever.png")
        self.zoom_board = pygame.image.load("res/workshop/zoom_board.png")
        self.zoom_board2 = pygame.image.load("res/workshop/zoom_board2.png")
        self.item_drill = pygame.image.load("res/workshop/item_drill.png")
        self.item_map = pygame.image.load("res/workshop/item_map.png")
        self.item_page1 = pygame.image.load("res/workshop/item_page1.png")
        self.zoom_state = 0
        
    def click_event(self, x, y):
        if self.zoom_state == 0:
            if (763 < x < 841) and (313 < y < 347):
                self.zoom_state = 1
            elif (256 < x < 350) and (244 < y < 338):
                self.zoom_state = 2
            elif (896 < x < 989) and (210 < y < 989):
                self.zoom_state = 3
        elif self.zoom_state == 1:
            is_inside = (433 < x < 940) and (422 < y < 719)
            if not is_inside:
                self.zoom_state = 0
        elif self.zoom_state == 2:
            is_inside = (380 < x < 680) and (527 < y < 720)
            if not is_inside:
                self.zoom_state = 0
        elif self.zoom_state == 3:
            is_inside = (284 < x < 721) and (148 < y < 543)
            if not is_inside:
                self.zoom_state = 0
                      
    def draw(self):
        self.screen.blit(self.img_room, (0, 0))
        if self.zoom_state == 1:
            self.screen.blit(self.zoom_drill_no_needlever, (0, 0))
        elif self.zoom_state == 2:
            self.screen.blit(self.zoom_needle, (0, 0))
        elif self.zoom_state == 3:
            self.screen.blit(self.zoom_board, (0, 0))
        