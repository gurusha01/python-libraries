import pygame as pg
import random

pg.init()
screen=pg.display.set_mode((255,290))
green=(0,100,0)
red=(100,0,0)
grey=(100,100,100)
white=(255,255,255)


grid=[]

for i in range(10):
    ls=[]
    for j in range(10):
        ls.append(0)
    grid.append(ls)

mines=10
vis=[]
for i in range(10):
    ls=[]
    for j in range(10):
        ls.append(0)
    vis.append(ls)

flagged=[]
loc=[]
def mine_loc_init(grid,mines):
    m=mines
    for i in range(m):
        x=random.randint(1,8)
        y=random.randint(1,8)
        if grid[x][y]==-1:
            m+=1
        else :
            loc.append([x,y])
            grid[x][y]=-1
                        
def place_mines(grid):
    for i in range(len(loc)):
        grid[loc[i][0]][loc[i][1]]=-1



def make_grid(grid,vis,flagged):
    for i in range (10):
        for j in range(10):
            pg.draw.rect(screen, white,(25*(i+1)-20,25*(j+1)-20,20,20))
            if vis[i][j]==1:
                pg.draw.rect(screen, green,(25*(i+1)-20,25*(j+1)-20,20,20))
            if vis[i][j]==1 and grid[i][j]>0:
                Overfont=pg.font.Font('freesansbold.ttf',15)   
                t11=Overfont.render( str(grid[i][j]),True,(255,0,0))
                screen.blit(t11,(25*(i+1)-20+2,25*(j+1)-20+2))
            if vis[i][j]==2 :
                pg.draw.rect(screen, red,(25*(i+1)-20,25*(j+1)-20,20,20))
                
    pg.display.update()

        
    
#assigning no of adj mines on i j cell of gird
def assign_num(grid,vis,flagged):
    for i in range(10):
        for j in range(10):
            if grid[i][j]==-1:
                grid[i+1][j]+=1
                grid[i+1][j+1]+=1
                grid[i+1][j-1]+=1
                grid[i-1][j]+=1
                grid[i-1][j+1]+=1
                grid[i-1][j-1]+=1
                grid[i][j-1]+=1
                grid[i][j+1]+=1
                place_mines(grid)

#loop to clear the selected area and show no of bombs
def sweep(grid,vis,i,j):
    if 0<=i<10 and 0<=j<10:
        if grid[i][j]==0:
            if not(vis[i][j]==1):
                vis[i][j]=1
                sweep(grid,vis,i,j+1)
                sweep(grid,vis,i,j-1)
                sweep(grid,vis,i+1,j)
                sweep(grid,vis,i-1,j)
                sweep(grid,vis,i+1,j+1)
                sweep(grid,vis,i+1,j-1)
                sweep(grid,vis,i-1,j+1)
                sweep(grid,vis,i-1,j-1)
        elif grid[i][j]>0:
            vis[i][j]=1

def win(vis):
    for i in range(10):
        for j in range(10):
            if vis[i][j]==0:
                return False
    return True
            
        
def gameloop(grid,vis,flagged):
    mine=10
    loose=False
    first_click=1
    running=True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
        make_grid(grid,vis,flagged)
        mouse=pg.mouse.get_pos()
        click=pg.mouse.get_pressed()
        if click[0] and first_click:
            first_click=0
            x=int(mouse[0]/25)
            y=int(mouse[1]/25)
            grid[x][y]=-1
            mine_loc_init(grid,mines)
            grid[x][y]=0
            assign_num(grid,vis,flagged)
            for i in range(10):
                print (grid[i])
                
        if(click[0]) and not first_click:
            x=int(mouse[0]/25)
            y=int(mouse[1]/25)
            if(grid[x][y]>=0):
                sweep(grid,vis,x,y)
            if grid[x][y]==-1:
                loose=True
        make_grid(grid,vis,flagged)
        if click[2]:
            x=int(mouse[0]/25)
            y=int(mouse[1]/25)
            if vis[x][y]==0:
                vis[x][y]=2
                mine-=1
            elif vis[x][y]==2:
                vis[x][y]=0
                mine+=1

            
        make_grid(grid,vis,flagged)
        sleep=pg.image.load('sleep.png')
        screen.blit(sleep,(125,260))

        
        if win(vis):
            smiley=pg.image.load('smiley.png')
            screen.blit(smiley,(125,260))
        if loose:
            sad=pg.image.load('sad.png')
            screen.blit(sad,(125,260))
            
        pg.display.update()
        pg.time.delay(100)



gameloop(grid,vis,flagged)

    


