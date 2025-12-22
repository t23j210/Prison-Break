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
        self.zoom_no_needlever = pygame.image.load("res/workshop/zoom_no_needlever.png")
        self.zoom_board = pygame.image.load("res/workshop/zoom_board.png")
        self.zoom_board2 = pygame.image.load("res/workshop/zoom_board2.png")
        self.item_map = pygame.image.load("res/workshop/item_map.png")
        self.item_page1 = pygame.image.load("res/workshop/item_page1.png")
        self.item_no_needlever = pygame.image.load("res/workshop/item_no_needlever.png")
        self.item_needle = pygame.image.load("res/workshop/item_needle.png")
        self.zoom_board3 = pygame.image.load("res/workshop/zoom_board3.png")
        self.zoom_board4 = pygame.image.load("res/workshop/zoom_board4.png")
        self.zoom_state = 0
        self.item_sdriver_state = 0
        self.next_room = 2
        
    def click_event(self, x, y):
        if self.zoom_state == 0:
            if (763 < x < 841) and (313 < y < 347):
                if self.item_get[4]:
                    self.zoom_state = 4
                elif self.item_get[12]:
                    self.zoom_state = 4
                else:
                    self.zoom_state = 1
            elif (256 < x < 350) and (244 < y < 338):
                if self.item_get[11]:
                    self.zoom_state = 5
                elif self.item_get[12]:
                    self.zoom_state = 5
                else:
                    self.zoom_state =2
            elif (896 < x < 989) and (210 < y < 331):
                if self.item_get[3]:
                    self.zoom_state = 6
                else:
                    self.zoom_state = 3
            elif (46 < x < 136) and (206 < y < 310):
                if self.item_get[5]:
                    self.zoom_state = 8
                else:
                    self.zoom_state = 7
            elif (938 < x < 1010) and (692 < y < 753):
                        self.next_room = 1       
                
        elif self.zoom_state == 1:
            if (430 < x < 920) and (455 < y < 719):
                if not self.item_get[4]:
                    self.item_get[4] = True
                    self.zoom_state = 4
            
            is_inside = (430 < x < 920) and (455 < y < 719) 
            if not is_inside:
                self.zoom_state = 0
        
        elif self.zoom_state == 2:
            if (380 < x < 680) and (527 < y < 720):
                if not self.item_get[11]:
                    self.item_get[11] = True
                    self.zoom_state = 5

            is_inside = (380 < x < 680) and (527 < y < 720) 
            if not is_inside:
                self.zoom_state = 0
                
        elif self.zoom_state == 3:
            if (302 < x < 590) and (344 < y < 520):
                if not self.item_get[3]:
                    self.item_get[3] = True
                    self.zoom_state = 6

            is_inside = (302 < x < 590) and (344 < y < 520)
            if not is_inside:
                self.zoom_state = 0

        elif self.zoom_state == 4:
            is_inside = (430 < x < 920) and (455 < y < 719) 
            if not is_inside:
                self.zoom_state = 0
        
        elif self.zoom_state == 5:
            is_inside = (380 < x < 680) and (527 < y < 720) 
            if not is_inside:
                self.zoom_state = 0
        
        elif self.zoom_state == 6:
            is_inside = (302 < x < 590) and (344 < y <520)
            if not is_inside:
                self.zoom_state = 0
        
        elif self.zoom_state == 7:
            if (699 < x < 906) and (352 < y < 502):
                if not self.item_get[5]:
                    self.item_get[5] = True
                    self.zoom_state = 8

            is_inside = (699 < x < 906) and (352 < y < 502)
            if not is_inside:
                self.zoom_state = 0

        elif self.zoom_state == 8:
            is_inside = (699 < x < 906) and (352 < y < 502)
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
        
        elif self.zoom_state == 4:
            self.screen.blit(self.zoom_no_drillver, (0, 0))

        elif self.zoom_state == 5:
            self.screen.blit(self.zoom_no_needlever, (0, 0))
        
        elif self.zoom_state == 6:
            self.screen.blit(self.zoom_board2, (0, 0))
        
        elif self.zoom_state == 7:
            self.screen.blit(self.zoom_board3, (0, 0))
        
        elif self.zoom_state == 8:
            self.screen.blit(self.zoom_board4, (0, 0))
            
    def next_state(self):
        next = self.next_room
        self.next_room = 2
        return next
 