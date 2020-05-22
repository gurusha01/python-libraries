import pygame as pg

pg.init()
screen=pg.display.set_mode((600,600))
pg.display.set_caption("tic-tac-toe")
screen.fill((255,255,255))
green=(0,100,0)
red=(100,0,0)
grey=(100,100,100)          



board=[[3,3,3],[3,3,3],[3,3,3]]

def end_b(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]==3):
                return False
    return True


def board_value(board):
    for row in range(3):
        if board[row][0]==board[row][1] and board[row][1]==board[row][2]:
            if (board[row][0]==1):
                return +10
            elif (board[row][0]==0):
                return -10
    for col in range(3):
        if board[0][col]==board[1][col] and board[1][col]==board[2][col]:
            if (board[0][col]==1):
                return +10
            elif (board[0][col]==0):
                return -10
    if (board[0][0]==board[1][1] and board[1][1]==board[2][2]):

        if (board[0][0]==1):
            return +10
        elif (board[0][0]==0):
            return -10

    if (board[0][2]==board[1][1] and board[1][1]==board[2][0]):

        if (board[0][2]==1):
            return +10
        elif (board[0][2]==0):
            return -10
    return 0



def minimax(board,depth,ismax):
    value=board_value(board)
    if(value!=0):
        return value
    if(end_b(board)):
        return 0
    if(ismax):
        b=-1000
        for i in range(3):
            for j in range(3):
                if board[i][j]==3:
                    board[i][j]=1
                    b=max(minimax(board,depth+1,False),b);
                    board[i][j]=3
        return b
    else:
        b=1000
        for i in range(3):
            for j in range(3):
                if board[i][j]==3:
                    board[i][j]=0
                    b=min(minimax(board,depth+1,True),b);
                    board[i][j]=3
        return b


def bestmove(board):
    b=-1000
    x=-1
    y=-1
    for i in range(3):
        for j in range(3):
            if(board[i][j]==3):
                board[i][j]=1
                val=minimax(board,0,False)
                board[i][j]=3
                if(val>b):
                    b=val
                    x=i
                    y=j
    #print(x)
    #print(y)
    if x > -1 and y> -1:
        board[x][y]=1

def draw_b(board):
    check=pg.image.load('check.png')
    cross=pg.image.load('cross.png')
    zero=pg.image.load('circle.png')
    screen.fill((255,255,255))
    screen.blit(check,(0,0))
    for i in range(3):
        for j in range(3):
            if board[i][j]==1:
                screen.blit(cross,(210*i,210*j))
            if board[i][j]==0:
                screen.blit(zero,(210*i,210*j))
    #print(board)
    pg.display.update()

def chance(board):
    #print("hi")
    intro=True
    while(intro):
        for event in pg.event.get():
            if event.type == pg.QUIT:
               intro=False
        mouse=pg.mouse.get_pos()
        click=pg.mouse.get_pressed()
        if(click[0]==1):
            i=int(mouse[0]/200)
            j=int(mouse[1]/200)
            board[i][j]=0
            intro=False
    pg.display.update()
    pg.time.delay(1000)


def win(value):
    pg.draw.rect(screen,(255,0,0),(300,300,150,150))
    if(value>0):
        ans="computer wins"
    elif value<0:
        ans="you win"
    else:
        ans="tie"
    Overfont=pg.font.Font('freesansbold.ttf',25)   
    t11=Overfont.render( ans,True,(255,255,0))
    screen.blit(t11,(310,310))
    pg.display.update()
    pg.time.delay(3000)
          
def gameloop(board):
    
    running=True
    while running:
        draw_b(board)
        w=pg.image.load('check.png')
        screen.blit(w,(0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
        while(not end_b(board)):
            chance(board)
            draw_b(board)
            bestmove(board)
            draw_b(board)
        if(end_b(board)):
            value=board_value(board)
            win(value)         
            running=False
        pg.display.update()
        pg.time.delay(100)

#enter game loop from here proceed to gameloop
def game_intro():
    intro=True
    while intro:
        screen.fill((0,0,100))
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
                gameloop(board)
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
        
#write instructions from hetre go to play ot not play loop
def instruction():
    intro=True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                intro=False
        screen.fill((255,255,255))
        overfont=pg.font.Font('freesansbold.ttf',32)
        GO1=overfont.render( "DO NOT DOUBLE CLICK ELSE",True,(255,0,0))
        screen.blit(GO1,(0,0))
        overfont=pg.font.Font('freesansbold.ttf',32)
        GO1=overfont.render( "YOUR CHANCE WILL BE SKIPPED ",True,(255,0,0))
        screen.blit(GO1,(0,50))
        mouse=pg.mouse.get_pos()
        click=pg.mouse.get_pressed()
        if 400+150 > mouse[0] > 400 and 400+50> mouse[1] > 400:
            pg.draw.rect(screen,grey,(400,400,150,50))
            if click[0] == 1:
                game_intro()
        else:
            pg.draw.rect(screen,green,(400,400,150,50))
            
        Overfont=pg.font.Font('freesansbold.ttf',25)   
        t11=Overfont.render( "GO ",True,(255,0,0))
        screen.blit(t11,(410,410))
        pg.display.update()


instruction()    
                   
pg.quit()
     
