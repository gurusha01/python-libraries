from pygame import mixer
import pygame as pg
import random

pg.init()
screen=pg.display.set_mode((600,600))
pg.display.set_caption("save me")
mixer.music.load("msc.mp3")
mixer.music.play(-1)
green=(0,100,0)
red=(100,0,0)
grey=(100,100,100)          



spx=random.randint(20,25)
spy=random.randint(20,25)
ballx=random.randint(0,200)
bally=random.randint(0,200)                 


font=pg.font.Font('freesansbold.ttf',32)
textx=10
texty=10
score=0
life=5

def show(x,y,score,life):
    score_f=font.render("score:" + str(score)+" Life:" +str(life),True,(255,255,255))
    screen.blit(score_f,(x,y))

playerimg=pg.image.load('board.png')

playerx=200
playery=500
plxc=0


def player(x,y):
    screen.blit(playerimg, (x,y))

    
def ball(x,y):
    screen.blit(pg.image.load('ball.png'),(x,y))


def collission(bally,ballx,playery,playerx):
    if playery+25>=bally>=playery-25 and playerx+100 >= ballx >= playerx-10:
        return True
    else :
        return False
    

def game_intro():
    intro=True
    while intro:
        screen.fill((0,0,100))
        w=pg.image.load('w.png')
        screen.blit(w,(50,150))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                intro=False
        overfont=pg.font.Font('freesansbold.ttf',32)
        GO1=overfont.render( "welcome to save the ball game ",True,(255,0,0))
        screen.blit(GO1,(0,0))

        mouse=pg.mouse.get_pos()
        click=pg.mouse.get_pressed()
        if 100+150 > mouse[0] > 100 and 100+50> mouse[1] > 100:
            pg.draw.rect(screen,grey,(100,100,150,50))
            if click[0] == 1:
                gameloop(ballx,bally,spx,spy,5,0,playerx,playery)
        else:
            pg.draw.rect(screen,green,(100,100,150,50))
            
        if 350+150 > mouse[0] > 350 and 100+50> mouse[1] > 100:
            pg.draw.rect(screen,grey,(350,100,150,50))
            if click[0] == 1:
                intro=False        
        else:
            pg.draw.rect(screen,red,(350,100,150,50))
        if intro==False:
            pg.quit()
        Overfont=pg.font.Font('freesansbold.ttf',25)   
        t11=Overfont.render( "play ",True,(255,0,0))
        screen.blit(t11,(110,110))
        overfont2=pg.font.Font('freesansbold.ttf',25)
        t12=overfont2.render( "quit",True,(255,0,0))
        screen.blit(t12,(360,110))
        
        pg.display.update()








def gameloop(ballx,bally,spx,spy,life,score,playerx,playery):       
    running=True
    while running: 
        screen.fill((0,0,0))
        w=pg.image.load('forest.png')
        screen.blit(w,(0,100))
        plxc=0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    plxc=-100
                if event.key == pg.K_RIGHT:
                    plxc=100
            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                    plxc=0
        if ballx <=0 :
            spx*=-1
            ballx+=10
        elif ballx>=540:
            spx*=-1
            ballx-=10
        elif bally<=0 :
            spy*=-1
            bally+=10
        if collission(bally,ballx,playery,playerx):
            spy*=-1
            score+=1
        if bally>=600:
            life-=1
            ballx=random.randint(0,200)
            bally=random.randint(0,200)
        show(0,0,score,life)
        playerx+=plxc
        if(playerx<=0):
            playerx=0
        if playerx >= 475:
            playerx=475
        player(playerx,playery)
        ballx+=spx
        bally+=spy
        ball(ballx, bally)
        over_font=pg.font.Font('freesansbold.ttf',32)
        GO=over_font.render("GAME OVER" ,True,(255,0,0))
        if life==0:
            screen.blit(GO,(200,200))
            running=False
            screen.fill((0,0,0))
        pg.display.update()
        pg.time.delay(100)

game_intro()
pg.quit()
