import copy

def taquin(m_problem):
    dico = {}
    queue_place_sorted = [([[1,2,3],[4,5,6],[7,8,0]],0)]
    dico[str(queue_place_sorted[0][0])] = ([],0)
    while str(m_problem) not in dico.keys() :
        current_matrix = copy.deepcopy(queue_place_sorted [0][0])
        new_matrices = new_configs (current_matrix)
        queue_place_sorted.pop(0)
        queue = [queue_place_sorted [b][0] for b in range(len(queue_place_sorted))]
        for i in new_matrices :
            if i not in queue and str(i) not in dico.keys():
                queue.append(i)
        queue_place = [(queue[a],place_distance(queue[a])) for a in range(len(queue))]
        queue_place_sorted = sorted(queue_place, key=lambda x: x[1])
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
    
def place_distance(matrix):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = matrix[i][j]
            if value != 3 * i + j + 1:
                distance+=1
    return distance

#print(taquin([[8,6,7],[5,0,1],[3,2,4]])) #30
    

#print(taquin([[6,1,7],[2,0,3],[5,4,8]])) #18

print(taquin([[6,1,3],[2,0,8],[4,7,5]])) #12

#print(taquin([[1,2,3],[4,5,6],[7,0,8]])) #1

#print(taquin([[1,2,3],[4,5,6],[0,7,8]])) #2

#print(taquin([[2,0,3],[1,5,6],[4,7,8]])) #5


