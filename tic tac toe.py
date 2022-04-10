import pygame, sys
from pygame.locals import *
import math
import random
pygame.init()

# Screen
WIDTH = 500
ROWS = 3
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")
screen = pygame.display.set_mode((500, 500),0,32)
click = False

# Images
X_IMAGE = pygame.transform.scale(pygame.image.load("Images/x.png"), (150, 150))
X_WIN = pygame.transform.scale(pygame.image.load("Images/x win.png"), (250, 250))
O_IMAGE = pygame.transform.scale(pygame.image.load("Images/o.png"), (150, 150))
O_WIN = pygame.transform.scale(pygame.image.load("Images/o win.png"), (250, 250))
DRAW_PIC = pygame.transform.scale(pygame.image.load("Images/draw.png"), (250, 250))
TITLE = pygame.transform.scale(pygame.image.load("Images/Title.png"), (500, 500))
MULTI = pygame.transform.scale(pygame.image.load("Images/multiplayer.png"), (200, 200))
CPU_E = pygame.transform.scale(pygame.image.load("Images/cpu.png"), (200, 200))
CPU_H = pygame.transform.scale(pygame.image.load("Images/exit.png"), (200, 200))


 #main menu
def main_menu():
    while True:
 
        screen.fill((230, 230, 230))
        screen.blit(TITLE, (0,-150))

 
        mx, my = pygame.mouse.get_pos()
	#create buttons
        button_1 = pygame.Rect(150, 175, 200, 60)
        button_2 = pygame.Rect(150, 275, 200, 60)
        button_3 = pygame.Rect(150, 375, 200, 60)
        button_1stroke = pygame.Rect(147, 172.5, 207.5, 67.5)
        button_2stroke = pygame.Rect(147, 272.5, 207.5, 67.5)
        button_3stroke = pygame.Rect(147, 372.5, 207.5, 67.5)
	#add functions to buttons
        if button_1.collidepoint((mx, my)):
            if click:
                multi()
        if button_2.collidepoint((mx, my)):
            if click:
                pvcpu()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()


        pygame.draw.rect(screen, (107, 107, 107), button_1stroke)
        pygame.draw.rect(screen, (255, 255, 255), button_1)
        pygame.draw.rect(screen, (107, 107, 107), button_2stroke)
        pygame.draw.rect(screen, (255, 255, 255), button_2)
        pygame.draw.rect(screen, (107, 107, 107), button_3stroke)
        pygame.draw.rect(screen, (255, 255, 255), button_3)

        screen.blit(MULTI, (150,120))
        screen.blit(CPU_E, (150,220))
        screen.blit(CPU_H, (150,320))

#if exit or escape, exit program
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()

#create the grid for the playing board
def draw_grid():
	gap = WIDTH // ROWS

	# Starting points
	x = 0
	y = 0

	for i in range(ROWS):
		x = i * gap

		pygame.draw.line(win, (200, 200, 200), (x, 0), (x, WIDTH), 3)
		pygame.draw.line(win, (200, 200, 200), (0, x), (WIDTH, x), 3)

def initialize_grid():
	dis_to_cen = WIDTH // ROWS // 2

	# Initializing the array
	board = [[None, None, None], [None, None, None], [None, None, None]]

	for i in range(len(board)):
		for j in range(len(board[i])):
			x = dis_to_cen * (2 * j + 1)
			y = dis_to_cen * (2 * i + 1)

			# Adding centre coordinates
			board[i][j] = (x, y, "", True)


	return board

#play a multiplayer game
def play(board):
	global x_turn, o_turn, images

	# Mouse position
	m_x, m_y = pygame.mouse.get_pos()

	for i in range(len(board)):
		for j in range(len(board[i])):
			x, y, char, can_play = board[i][j]

			# Distance between mouse and the centre of the square
			dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

			# If it's inside the square
			if dis < WIDTH // ROWS // 2 and can_play:
				if x_turn:  # If it's X's turn
					images.append((x, y, X_IMAGE))
					x_turn = False
					o_turn = True
					board[i][j] = (x, y, 'x', False)

				elif o_turn:  # If it's O's turn
					images.append((x, y, O_IMAGE))
					x_turn = True
					o_turn = False
					board[i][j] = (x, y, 'o', False)
#pick a random x coordinate
def pick_random_square_x():
	r1 = random.randint(1, 3)
	if r1 == 1:
		x = 83
	elif r1 == 2:
		x = 249
	elif r1 == 3:
		x = 415
	return (x)

#pick a random y coordinate
def pick_random_square_y():
	r2 = random.randint(1, 3)
	if r2 == 1:
		y = 83
	elif r2 == 2:
		y = 249
	elif r2 == 3:
		y = 415
	return (y)

#random computer player move
def comp_cpu_easy(board):
	global x_turn, o_turn, images
	# Mouse position
	count = 0
	o_went = True
	while o_went:
		count = count + 1
		if o_turn:
			m_x = pick_random_square_x()
			m_y = pick_random_square_y()
		for i in range(len(board)):
			for j in range(len(board[i])):
				x, y, char, can_play = board[i][j]

				# Distance between mouse and the centre of the square
				dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

				# If it's inside the square
				if dis < WIDTH // ROWS // 2 and can_play:
					if o_turn:  # If it's X's turn
						images.append((x, y, O_IMAGE))
						x_turn = True
						o_turn = False
						board[i][j] = (x, y, 'o', False)
						o_went = False
		if(count > 25):
			break
				
#Player move against cpu
def play_cpu_easy(board):
	global x_turn, o_turn, images

	# Mouse position
	m_x, m_y = pygame.mouse.get_pos()

	for i in range(len(board)):
		for j in range(len(board[i])):
			x, y, char, can_play = board[i][j]

			# Distance between mouse and the centre of the square
			dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

			# If it's inside the square
			if dis < WIDTH // ROWS // 2 and can_play:
				if x_turn:  # If it's X's turn
					images.append((x, y, X_IMAGE))
					x_turn = False
					o_turn = True
					board[i][j] = (x, y, 'x', False)
					comp_cpu_easy(board)
	
		
			


# Checking if someone has won
def has_won(board):
	# Checking columns
	for col in range(len(board)):
		if (board[0][0][2] == board[1][0][2] == board[2][0][2]) and board[2][0][2] != "":
			show(board[0][0][2].upper())
			return True
		if (board[0][1][2] == board[1][1][2] == board[2][1][2]) and board[2][1][2] != "":
			show(board[0][1][2].upper())
			return True
		if (board[0][2][2] == board[1][2][2] == board[2][2][2]) and board[2][2][2] != "":
			show(board[0][2][2].upper())
			return True

	# Checking rows
	for row in range(len(board)):
		if (board[0][0][2] == board[0][1][2] == board[0][2][2]) and board[0][0][2] != "":
			show(board[0][0][2].upper())
			return True
		if (board[1][0][2] == board[1][1][2] == board[1][2][2]) and board[1][0][2] != "":
			show(board[1][0][2].upper())
			return True
		if (board[2][0][2] == board[2][1][2] == board[2][2][2]) and board[2][0][2] != "":
			show(board[2][0][2].upper())
			return True

	# Checking diagonal
	if (board[0][0][2] == board[1][1][2] == board[2][2][2]) and board[0][0][2] != "":
		show(board[0][0][2].upper())
		return True
	if (board[0][2][2] == board[1][1][2] == board[2][0][2]) and board[0][2][2] != "":
		show(board[0][2][2].upper())
		return True

	return False

#if there is a draw
def drawGame(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j][2] == "":
				return False

	show("draw")
	return True

#display win or draw
def show(content):
	pygame.time.delay(500)
	win.fill((255, 255, 255))
	if(content == "X"):
		win.blit(X_WIN, ((WIDTH - X_WIN.get_width()) // 2, (WIDTH - X_WIN.get_height()) // 2))
	if(content == "O"):
		win.blit(O_WIN, ((WIDTH - O_WIN.get_width()) // 2, (WIDTH - O_WIN.get_height()) // 2))
	if(content == "draw"):
		win.blit(DRAW_PIC, ((WIDTH - DRAW_PIC.get_width()) // 2, (WIDTH - DRAW_PIC.get_height()) // 2))
	pygame.display.update()
	pygame.time.delay(2000)

#render the images
def render():
	win.fill((255, 255, 255))
	draw_grid()

	# Drawing X's and O's
	for image in images:
		x, y, IMAGE = image
		win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

	pygame.display.update()

#play a multiplayer game mode
def multi():
	global x_turn, o_turn, images, draw

	images = []

	run = True

	x_turn = True
	o_turn = False

	board = initialize_grid()

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				play(board)

		render()

		if has_won(board) or drawGame(board):
			run = False

#play a player vs compuer game mode
def pvcpu():
	global x_turn, o_turn, images, draw

	images = []

	run = True

	x_turn = True
	o_turn = False

	board = initialize_grid()

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				play_cpu_easy(board)

		render()

		if has_won(board) or drawGame(board):
			run = False

main_menu()