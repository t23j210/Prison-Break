# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:23:51 2020

@author: Ozaki
"""
import pygame
from room_base import Room_Base

class Start(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.screen = screen
        self.lock_flag = lock_flag
        self.item_get = item_get
        self.item_use = item_use
        self.start = pygame.image.load("res/start/start.png")
        pygame.mixer.init(frequency = 44100)
        pygame.mixer.music.load("res/music/music.mp3")
        pygame.mixer.music.set_volume(0.2)
        self.play_music = False
        self.next_room = 0
        self.zoom_state = 0
    

    def click_event(self, x, y):
        if self.zoom_state == 0:
            if (373 < x < 661) and (476 < y < 561):
                self.next_room = 1
                pygame.mixer.music.stop()

    def draw(self):
        self.screen.blit(self.start, (0, 0))

    def do(self):
        if self.play_music == False:
            pygame.mixer.music.play(-1)
            self.play_music = True

    def next_state(self):
        next = self.next_room #次の部屋
        self.next_room = 0
        return next
