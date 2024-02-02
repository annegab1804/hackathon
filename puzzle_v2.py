import pygame
import copy
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
font_2 = pygame.font.Font(None, 20)

screen = pygame.display.set_mode((width, height+square_size))
screen.fill(blue)
pygame.display.set_caption("Puzzle Taquin")

def taquin(m_problem):
    dico = {}
    distance= 0
    queue = [[[1,2,3],[4,5,6],[7,8,0]]]
    dico[str(queue[0])] = ([],distance)
    while str(m_problem) not in dico.keys() :
        current_matrix = queue [0]
        new_matrices = new_configs (current_matrix)
        queue.pop(0)
        for i in new_matrices :
            if i not in queue and str(i) not in dico.keys():
                queue.append(i)
        for j in new_matrices:
            if str(j) not in dico.keys():
                path = [current_matrix] + dico[str(current_matrix)][0]
                dico[str(j)] = (path,dico[str(current_matrix)][1] + 1)
    return dico[str(m_problem)]
    
        

def new_configs(current_mat):
    for i in range (3):
        for j in range (3):
            if current_mat[i][j] == 0:
                position_0 = [i,j]
    possibilities = []
    if position_0[0] == 0:
        possibilities.append ([position_0[0] + 1, position_0[1]])
    if position_0[0] == 1:
        possibilities.append ([position_0[0] + 1, position_0[1]])
        possibilities.append ([position_0[0] - 1, position_0[1]])
    if position_0[0] == 2:
        possibilities.append ([position_0[0] - 1, position_0[1]])
    if position_0[1] ==0:
        possibilities.append ([position_0[0],position_0[1] + 1])
    if position_0[1] ==1:
        possibilities.append ([position_0[0], position_0[1] + 1])
        possibilities.append ([position_0[0], position_0[1] - 1])
    if position_0[1] ==2:
        possibilities.append ([position_0[0], position_0[1] - 1])
    new_matrices = []
    for k in possibilities:
        add_matrice = copy.deepcopy(current_mat)
        add_matrice[position_0[0]][position_0[1]] = add_matrice[k[0]][k[1]]
        add_matrice[k[0]][k[1]] = 0
        new_matrices.append(add_matrice)
    return new_matrices
    

def draw_puzzle(grid, moves):
    pygame.draw.rect(screen, white, (0,height, width, square_size))
    for line in range(1,3) :
        pygame.draw.line(screen, white, ((line) * square_size , 0), ((line)*square_size, height))
        pygame.draw.line(screen, white, (0,(line) * square_size), ( width, (line)*square_size))
    for line in range(lines):
        for column in range(columns):
            piece = grid[line][column]
            if piece != 0 :
                
                font = pygame.font.Font(None, 36)
                text = font.render(str(piece), True, white)
                text_position = text.get_rect(center=(column * square_size + square_size // 2, line * square_size + square_size // 2))
                screen.blit(text, text_position)

    phrase = f"Moves : {moves}"
    moves_surface = font_2.render(phrase, True, black)  
    moves_position = moves_surface.get_rect(center = (width//2, height + square_size//4))
    screen.blit(moves_surface, moves_position) 

    phrase2 = f"Optimal moves : {optimal_solution}"
    optimal_surface = font_2.render(phrase2, True, black)  
    optimal_position = optimal_surface.get_rect(center = (width//2, height + 2*square_size//3))
    screen.blit(optimal_surface, optimal_position)


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
    optimal_solution = taquin(grid)[1]
    moves = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                moves += 1

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

    






