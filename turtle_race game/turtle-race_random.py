import pygame as pg
import random

pg.init()
screen=pg.display.set_mode((600,600))
pg.display.set_caption("turtle race")
icon=pg.image.load('tt.jpg')
pg.display.set_icon(icon)
background = pg.image.load('bg1.png')
green=(0,100,0)
red=(100,0,0)
grey=(100,100,100)
turt=['tc.png','tb.png']
turx=[150,350]
tsp=[]
y=[500,500]
tsp.append(random.randint(20,500))
tsp.append(random.randint(20,500))
ans=-1
def turtle(y1,y2):
    screen.blit(pg.image.load(turt[0]),(turx[0],y1))
    screen.blit(pg.image.load(turt[1]),(turx[1],y2))

    
def game_intro():
    intro=True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                intro=False
        screen.blit(background, (50, 100))
        overfont=pg.font.Font('freesansbold.ttf',32)
        GO1=overfont.render( "welcome to turtle race : ",True,(255,0,0))
        screen.blit(GO1,(0,0))
        overfont2=pg.font.Font('freesansbold.ttf',32)
        GO12=overfont2.render( "select one turtle, ",True,(255,0,0))
        screen.blit(GO12,(0,50))

        mouse=pg.mouse.get_pos()
        click=pg.mouse.get_pressed()
        if 100+150 > mouse[0] > 100 and 100+50> mouse[1] > 100:
            pg.draw.rect(screen,grey,(100,100,150,50))
            if click[0] == 1:
                ans=0
                y[0]=500
                y[1]=500
                tsp[0]=random.randint(20,100)
                tsp[1]=random.randint(20,100)
                intro=False
                gameloop(ans)
        else:
            pg.draw.rect(screen,green,(100,100,150,50))
            
        if 350+150 > mouse[0] > 350 and 100+50> mouse[1] > 100:
            pg.draw.rect(screen,grey,(350,100,150,50))
            if click[0] == 1:
                ans=1
                y[0]=500
                y[1]=500
                tsp[0]=random.randint(20,100)
                tsp[1]=random.randint(20,100)
                intro=False
                gameloop(ans)
        else:
            pg.draw.rect(screen,red,(350,100,150,50))
        if intro==False:
            pg.quit()
        Overfont=pg.font.Font('freesansbold.ttf',25)   
        t11=Overfont.render( "colorful ",True,(255,0,0))
        screen.blit(t11,(110,110))
        overfont2=pg.font.Font('freesansbold.ttf',25)
        t12=overfont2.render( "black ",True,(255,0,0))
        screen.blit(t12,(360,110))
        
        pg.display.update()
      
def gameloop(ans):       
    running=True
    while running: 
        screen.fill((0,100,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
        y[0]-=tsp[0]
        y[1]-=tsp[1]
        y1=y[0]
        y2=y[1]
        turw="a"
        if y1<=0 or y2<=0:
            if(y1<=0) and ans==0:
                turw="YOU WIN"
            elif y2<=0 and ans==1:
                turw="YOU WIN"
            elif y2<=0 and ans==0:
                turw="YOU LOSE"
            elif y1<=0 and ans==1:
                turw="YOU LOSE"
            over_font=pg.font.Font('freesansbold.ttf',32)
            GO=over_font.render(turw ,True,(255,0,0))
            screen.blit(GO,(200,200))
            running=False
        turtle(y1,y2)
        pg.display.update()
        pg.time.delay(1000)
    
game_intro()
pg.quit()
