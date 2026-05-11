import pygame
import math

pygame.init()

screen_size=[800,400]
screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE)

def draw_ray(x0,y0,x,y):
    pygame.draw.line(screen,(255,255,255),(x0,y0),(x,y),3)

class compute_equation:
    def __init__(self,start,x,y):
        self.start=start
        self.x0=self.start+(screen_size[0]//2)
        self.y0=screen_size[1]//2
        self.x=self.start+screen_size[0]//2
        self.y=screen_size[1]//2
        self.xeqn=x
        self.yeqn=y
        self.t=0

    def reset(self):
        self.x0=self.start+(screen_size[0]//2)
        self.y0=screen_size[1]//2
        self.x=screen_size[0]//2
        self.y=screen_size[1]//2
        self.t=0

    def ray(self):
        pygame.draw.line(screen,(255,255,255),(self.x0,self.y0),(self.x,self.y),3)
    
    def draw_ray(self):
        self.t+=1
        t=self.t
        x=eval(self.xeqn)
        self.x=x+self.start+screen_size[0]//2
        y=eval(self.yeqn)
        self.y=(screen_size[1]//2)-y
        self.ray()
        self.x0=self.x
        self.y0=self.y

line1=compute_equation(-640,'t', '100*math.sin(x/20)')

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.VIDEORESIZE:
            screen_size[0]=event.w
            screen_size[1]=event.h
            line1.reset()

    pygame.draw.line(screen, (100,100,100), (0,screen_size[1]//2), (screen_size[0],screen_size[1]//2), 2)
    pygame.draw.line(screen, (100,100,100), (screen_size[0]//2,0), (screen_size[0]//2,screen_size[1]), 2)

    line1.draw_ray()

    pygame.display.flip()
    pygame.display.set_caption(f'{screen_size[0]} x {screen_size[1]}')

pygame.quit()