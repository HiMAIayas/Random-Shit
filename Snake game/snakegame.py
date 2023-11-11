import pygame
import random

class Node:
    def __init__(self,posX,posY):
        self.posX=posX
        self.posY=posY
        self.next=None
        self.prev=None
class Snake:
    def __init__(self,posX,posY,size=10): #actually is size-1 งง why?
        self.head=Node(posX,posY)
        
        cur=self.head
        cur.next=Node(posX-10,posY)
        cur.next.prev=self.head
        if size!=2:cur=cur.next
        for i in range(2,size):
            cur.next=Node(posX-10*i,posY)
            cur.next.prev=cur.prev.next
            if i!=size-1:
                cur=cur.next
                
        self.tail=cur.prev.next
        self.color=(0,255,0) #green
        
        
def searchAndDrawSnake(player:Snake,posX,posY):
    cur=player.head.next
    valid=True
    while cur:
        pygame.draw.rect(dis,player.color,[cur.posX,cur.posY,9,9])
        if posX==cur.posX and posY==cur.posY:valid=False
        cur=cur.next
    return valid
        
def drawFood(foodList:list):
    for pos in foodList:
        pygame.draw.rect(dis,(255,0,0),[pos[0],pos[1],9,9])
        
def respawnFood(foodList:list,pos:tuple): #TODO respawn food that is not the same pos as cur_food and snakeNode position
    foodList.remove(pos)
    while True:
        rand_X=random.randint(0,screensize[0]/10)*10
        rand_Y=random.randint(0,screensize[1]/10)*10
        foodPos = (rand_X,rand_Y)
        if foodPos not in foodList:
            foodList.append(foodPos)
            break
    
pygame.init() #start
screensize=(800,600)   #
dis=pygame.display.set_mode(screensize)
pygame.display.update()
pygame.display.set_caption('Snake game Test')

#init setting
game_close=False
start=False
clock = pygame.time.Clock()
delta_X=0
delta_Y=0
player=Snake(screensize[0]/2,screensize[1]/2)
speed=20

#generate food
foodNumber=10
foodList=list()
while foodNumber>0:
    rand_X=random.randint(0,screensize[0]/10)*10
    rand_Y=random.randint(0,screensize[1]/10)*10
    foodPos = (rand_X,rand_Y)
    if foodPos not in foodList:
        foodList.append(foodPos)
        foodNumber-=1

searchAndDrawSnake(player,0,0)
drawFood(foodList)
pygame.display.update()

while not start: #TODO At start, display only one block of snake
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            start=True
            game_close=True
            break
        elif event.type==pygame.KEYDOWN:
            if   event.key==pygame.K_LEFT :delta_X, delta_Y = -10,0
            elif event.key==pygame.K_RIGHT:delta_X, delta_Y = 10,0
            elif event.key==pygame.K_UP   :delta_X, delta_Y = 0,-10
            elif event.key==pygame.K_DOWN :delta_X, delta_Y = 0,10
            start=True
            break
    

while not game_close:
    for event in pygame.event.get():  #event such as cursor position, onClick, etc
        if event.type==pygame.QUIT:
            game_close=True
            break
        elif event.type==pygame.KEYDOWN:
            if   event.key==pygame.K_LEFT :
                if delta_X!=10: delta_X, delta_Y = -10,0
            elif event.key==pygame.K_RIGHT: 
                if delta_X!=-10:delta_X, delta_Y = 10,0
            elif event.key==pygame.K_UP   : 
                if delta_Y!=10: delta_X, delta_Y = 0,-10
            elif event.key==pygame.K_DOWN : 
                if delta_Y!=-10:delta_X, delta_Y = 0,10
    
    old_head=player.head
    new_head=Node(old_head.posX+delta_X, old_head.posY+delta_Y)
    old_head.prev=new_head
    new_head.next=player.head
    player.head=new_head

    curX=new_head.posX
    curY=new_head.posY
    
    if (curX,curY) in foodList:  #doesnt delete tail node when eating food
        respawnFood(foodList,(curX,curY))
        speed+=1 
    else:
        player.tail=player.tail.prev
        player.tail.next=None
        
    if curX >= screensize[0] or curX <0 or curY >= screensize[1] or curY < 0:
        game_close=True
    
    dis.fill((0, 0, 0))
    if not searchAndDrawSnake(player,curX,curY):
        game_close=True
            
    drawFood(foodList)
    pygame.display.update()
    clock.tick(speed) #snakespeed
    
pygame.quit()
quit()
