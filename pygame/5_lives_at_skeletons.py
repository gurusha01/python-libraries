import pygame as pg
import random
import math
from pygame import mixer

pg.init()#to initialise pygame
screen=pg.display.set_mode((600,600))#creates the screen and takes arguments as width and height of the screen
mixer.music.load("msc.mp3")
mixer.music.play(-1)
background = pg.image.load('gvy.jpg')

over_font=pg.font.Font('freesansbold.ttf',32)
GO=over_font.render("GAME OVER" ,True,(255,0,0))
#title and icon
pg.display.set_caption("halloween")
icon=pg.image.load('tt.jpg')
pg.display.set_icon(icon)

score_value=0
font=pg.font.Font('freesansbold.ttf',32)
textx=10
texty=10
life=5

def show(x,y):
    score=font.render("score:" + str(score_value)+" Life:" +str(life),True,(255,255,255))
    screen.blit(score,(x,y))
#player
playerimg=pg.image.load('ssk.png')

playerx=200
playery=400
plxc=0

def player(x,y):
    screen.blit(playerimg, (x,y))
    
#fireball
fbimg=pg.image.load('b.png')
fbx=random.randint(0,550)
fby=random.randint(0,150)
fbcy=1

def fireball(x,y):
    screen.blit(fbimg, (x,y))

def dist(x1,x2,y1,y2):
    dd=math.sqrt(math.pow(x1-x2,2)+math.pow(y2-y1,2))
    if dd<=20.0 :
        return True
    else:
        return False
     
#game loop
running=True
while running:
    #filling color in screen RGB       
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                plxc=-2
            if event.key == pg.K_RIGHT:
                plxc=2
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                plxc=0
        
    playerx+=plxc
    if playerx<=0:
        playerx=0
    elif playerx>=460:
        playerx=460
    col=dist(fbx,playerx,fby,playery)
    if col:
        score_value+=1
        fbx=random.randint(0,400)
        fby=random.randint(0,150)
        
    player(playerx,playery)
    show(textx,texty)
    fby+=fbcy
    if fby>=550 :
        life-=1
        fbx=random.randint(0,400)
        fby=random.randint(0,150)
    if life<=0:
        screen.blit(GO,(200,200))
        running=False
    fireball(fbx,fby)
    pg.display.update()
