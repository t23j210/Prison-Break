import pygame

class PasslockControl:
    def __init__(self, screen, lock_flag):
        self.lock_flag = lock_flag
        self.screen = screen
        self.font = pygame.font.SysFont(None, 23)
        self.password = [0, 0, 0, 0]
        self.index = 0

def push_number(self, num):
    self.password[self.index] = num
    self.index = ( self.index + 1) % 4
    if self.index == 0:
        self.unlock()
        
def reset_password(self):
    self.password = [0, 0, 0, 0]

def unlock(self):
    if self.password == [0, 4, 8, 8]:
        self.lock_flag[6] = True 



def disp_password(self):
    code = self.font.render("{:d} {:d} {:d} {:d}".format(self.password[0], self.password[1], self.password[2], self.password[3], True, (0, 4, 8, 8)))
    self.screen.blit(code, [446, 191]) 

