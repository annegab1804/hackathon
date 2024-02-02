
import pygame

import sys
import random

pygame.init()

clock = pygame.time.Clock()


# colors 
blue = (70, 130, 180)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
pink = (249, 66, 158)
purple = (216,191,216)

width, height = 300, 300
square_size = 100
lines, columns = 3, 3


font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((width, height))
screen.fill(blue)
pygame.display.set_caption("Puzzle Taquin")


def draw_puzzle(grid):
    for line in range(lines):
        for column in range(columns):
            piece = grid[line][column]
            if piece != 0:
                pygame.draw.rect(screen, purple, (column * square_size, line * square_size, square_size, square_size))
                pygame.draw.line(screen, white, ((line)*square_size,0), ((line)*square_size, height))
                pygame.draw.line(screen, white, (0,(column)*square_size), (width, (column)*square_size))
                
                font = pygame.font.Font(None, 36)
                text = font.render(str(piece), True, white)
                text_position = text.get_rect(center=(column * square_size + square_size // 2, line * square_size + square_size // 2))
                screen.blit(text, text_position)


def shuffle_puzzle():
    index=[]
    S = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(9):
        a = random.randint(0,2)
        b = random.randint(0,2)
        while [a,b] in index : 
            a = random.randint(0,2)
            b = random.randint(0,2)
        if [a,b] not in index :
            S[a][b]=i
            index.append([a,b])
    return S

def find_empty(grid):
    value = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j]==value :
                return i,j

def main():
    puzzle_solution = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  
    grid = shuffle_puzzle()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                x,y = find_empty(grid)

                if event.key == pygame.K_UP:
                    grid[x][y]=grid[x-1][y]
                    grid[x-1][y]=0

                elif event.key == pygame.K_DOWN:
                    grid[x][y]=grid[x+1][y]
                    grid[x+1][y]=0

                elif event.key == pygame.K_LEFT:
                    grid[x][y]=grid[x][y-1]
                    grid[x][y-1]=0

                elif event.key == pygame.K_RIGHT:
                    grid[x][y]=grid[x][y+1]
                    grid[x][y+1]=0

        screen.fill(purple) 
        draw_puzzle(grid)  
        pygame.display.flip()  

main()

    






