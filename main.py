# -*- coding: utf-8 -*-
"""
@author: Ozaki
"""

import pygame
import sys
from jail import Jail
from workshop import Workshop
from kitchen import Kitchen
from storage_room import Storage_room
from underground_waterway import Underground_waterway

def main():
    pygame.init()
    screen = pygame.display.set_mode((1104,768))
    clock = pygame.time.Clock()
    
    lock_flag = [False, False, False, False, False, False, False]
    
    room_state = 0
    room_ctrl = [Jail(screen, lock_flag),
                 Workshop(screen, lock_flag),
                 Kitchen(screen, lock_flag),
                 Storage_room(screen, lock_flag),
                 Underground_waterway(screen, lock_flag),]
    
    while True:

        """ マウスカーソル位置 """
        x, y = pygame.mouse.get_pos()
        room_ctrl[room_state].pos_event(x, y)
        
        """ クリックイベント，キーイベント """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                room_ctrl[room_state].click_event(x, y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    room_state = (room_state - 1) % 5
                elif event.key == pygame.K_RIGHT:
                    room_state = (room_state + 1) % 5
                elif event.key == pygame.K_a:
                    lock_flag[0] = not lock_flag[0]
                elif event.key == pygame.K_b:
                    lock_flag[1] = not lock_flag[1]
                elif event.key == pygame.K_c:
                    lock_flag[2] = not lock_flag[2]
                elif event.key == pygame.K_d:
                    lock_flag[3] = not lock_flag[3]
                elif event.key == pygame.K_e:
                    lock_flag[4] = not lock_flag[4]
                elif event.key == pygame.K_f:
                    lock_flag[5] = not lock_flag[5]
                elif event.key == pygame.K_g:
                    lock_flag[6] = not lock_flag[6]

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        """ 処理 """
        room_ctrl[room_state].do()
        
        """ 描画 """
        room_ctrl[room_state].draw()
        pygame.display.update()
        
        clock.tick(30)
        
        
if __name__ == '__main__':
    main()
