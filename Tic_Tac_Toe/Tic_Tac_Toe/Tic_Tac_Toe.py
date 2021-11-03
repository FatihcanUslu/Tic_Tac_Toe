import pygame
import button
from pygame.locals import *
from pygame import mixer

pygame.init()

#lines of the game
def game_grid():
	grid_color=(150,50,78)
	for x in range(1,3):
		pygame.draw.line(screen,grid_color,(0,x*100),(300,x*100),line_width)
		pygame.draw.line(screen,grid_color,(x*100,0),(x*100,300),line_width)

#draw blocks of x and o			
def draw_blocks():
	x_pos=0
	for x in blocks:
		y_pos=0
		for y in x:
			if y==1:
				pygame.draw.line(screen,black,(x_pos*100+15,y_pos*100+15),(x_pos*100+85,y_pos*100+85),line_width)
				pygame.draw.line(screen,black,(x_pos*100+15,y_pos*100+85),(x_pos*100+85,y_pos*100+15),line_width)
			if y==-1:
				pygame.draw.circle(screen,black,(x_pos*100+50,y_pos*100+50),38,line_width)
			y_pos+=1
		x_pos+=1
	#print(blocks) #this is for the controlling our array if u want to see how it looks like delete the # in front of print(block)
		
#commong variables
clicked=False
player=1
player2=-1
blocks=[]
pos=[]
black=(0,0,0)
red=(255,0,0)
line_width=6
winner=0
game_over=False
font=pygame.font.SysFont(None,40)

for x in range(3):
	row = [0]*3
	blocks.append(row)
print(blocks)	

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tic Tac Toe")
icon=pygame.image.load(r'icons\tic.png')
pygame.display.set_icon(icon)
#background sound
mixer.music.load(r'sounds\background.mp3')
mixer.music.play(-1)
#load button images
start_img = pygame.image.load(r'icons\start_button.png')
exit_img = pygame.image.load(r'icons\exit_btn.png')
x_img = pygame.image.load(r'icons\x.png')
o_img = pygame.image.load(r'icons\o.png')
template_img=pygame.image.load(r'icons\template.png')
site_img=pygame.image.load(r'icons\black-square.png')
winner1_img=pygame.image.load(r'icons\winner1.png')
winner2_img=pygame.image.load(r'icons\winner2.png')
choose_img=pygame.image.load(r'icons\choose.png')
#create button instances
start_button = button.Button(340, 100, start_img, 0.8)
exit_button = button.Button(340, 250, exit_img, 0.8)
x_button = button.Button(2000, 2000, x_img, 0.8)
o_button = button.Button(2000, 2000, o_img, 0.8)
template_button = button.Button(2000, 2000, template_img, 0.6)
winner1_button = button.Button(2000, 2000, winner1_img, 0.1)
winner2_button = button.Button(2000, 2000, winner2_img, 0.1)
choose_button = button.Button(2000, 2000, choose_img, 1)
team="empty"

#game rule

def rule(team):
	if team=='x':
		print()

#for ending game with win or draw


def ending_game():
	y_pos=0
	global winner
	global game_over
	#////////////////////////////////////////if first player is x /////////////////////////////////////////////////
	if team=='x':
		for x in blocks:
			#for the columns
			if sum(x)==3:
				winner=1
				game_over =True
			if sum(x)==-3:
				winner=2
				game_over =True
			#for the rows
			if blocks[0][y_pos]+blocks[1][y_pos]+blocks[2][y_pos]==3:
				winner=1
				game_over =True
			if blocks[0][y_pos]+blocks[1][y_pos]+blocks[2][y_pos]==-3:
				winner=2
				game_over =True
			y_pos+=1
			#for the cross
		if blocks[0][0]+blocks[1][1]+blocks[2][2]==3 or blocks[2][0]+blocks[1][1]+blocks[0][2]==3:
			winner=1
			game_over =True
		if blocks[0][0]+blocks[1][1]+blocks[2][2]==-3 or blocks[2][0]+blocks[1][1]+blocks[0][2]==-3:
			winner=2
			game_over =True
	#////////////////////////////////////////////if first player is o ///////////////////////////////////////////////

	if team=='o':
		for x in blocks:
			#for the columns
			if sum(x)==3:
				winner=2
				game_over =True
			if sum(x)==-3:
				winner=1
				game_over =True
			#for the rows
			if blocks[0][y_pos]+blocks[1][y_pos]+blocks[2][y_pos]==3:
				winner=2
				game_over =True
			if blocks[0][y_pos]+blocks[1][y_pos]+blocks[2][y_pos]==-3:
				winner=1
				game_over =True
			y_pos+=1
			#for the cross
		if blocks[0][0]+blocks[1][1]+blocks[2][2]==3 or blocks[2][0]+blocks[1][1]+blocks[0][2]==3:
			winner=2
			game_over =True
		if blocks[0][0]+blocks[1][1]+blocks[2][2]==-3 or blocks[2][0]+blocks[1][1]+blocks[0][2]==-3:
			winner=1
			game_over =True
#show winner
def draw_winner(winner):
	winner_text='Player'+str(winner)+"wins!"
	win_img=font.render(winner_text,True,black)
	pygame.draw.rect(screen,red,(SCREEN_WIDTH // 2-100,SCREEN_HEIGHT // 2-60,200,50))
	screen.blit(win_img(SCREEN_WIDTH // 2-100,SCREEN_HEIGHT // 2-50))
	

#game loop
run = True
while run:	
	
	screen.fill((0, 255, 255))	
	
	if start_button.draw(screen):
		print('START')
		start_button.rect.topleft = (1200, 200)
		exit_button.rect.topleft = (1200, 200)
		x_button.rect.topleft = (150, 300)
		o_button.rect.topleft = (500, 300)
		choose_button.rect.topleft = (-120, 100)
			#	#	#
		#	0	0	0
		#	0	0	0
		#	0	0	0



	if exit_button.draw(screen):
		print('EXIT')		
		run = False
	
	if x_button.draw(screen):
			team='x'
			print(team)
			x_button.rect.topleft = (1500, 200)
			o_button.rect.topleft = (5000, 200)
			choose_button.rect.topleft = (1500, 200)
			game_grid()
	if o_button.draw(screen):
			team='o'
			print('o')
			x_button.rect.topleft = (1500, 200)
			o_button.rect.topleft = (5000, 200)
			choose_button.rect.topleft = (1500, 200)
	if choose_button.draw(screen):
			print()
	if team =='x' or team == 'o':
		game_grid()
		draw_blocks()
	if winner1_button.draw(screen) or winner==1:		
							
				winner1_button.rect.topleft = (300, 200)
	if winner2_button.draw(screen) or winner==2:		
		
				winner2_button.rect.topleft = (300, 200)
	#event handler
	for event in pygame.event.get():
		#quit game
		
		
		try:	
			#if event.type == pygame.QUIT:
				#run = False
			if game_over==0:
				if event.type == pygame.MOUSEBUTTONDOWN and clicked==False:
					clicked=True
					print(event)
					#for every click 
					#click_sound=mixer.Sound(r'sounds\click.mp3')
					#click_sound.play()
				if event.type == pygame.MOUSEBUTTONUP and clicked==True:
					clicked=False
					
					pos=pygame.mouse.get_pos()
					cell_x=pos[0]
					cell_y=pos[1]
					
				
					if blocks[cell_x // 100][cell_y // 100]== 0 and team=='x':							
							blocks[cell_x//100][cell_y//100]=player
							player*=-1
							ending_game()
					if blocks[cell_x // 100][cell_y // 100]== 0 and team=='o':							
							blocks[cell_x//100][cell_y//100]=player2
							player2*=-1
							ending_game()		
			#print(winner)		
		except:
			t=1					
		finally:
			t=1							
	pygame.display.update()

pygame.quit()









































