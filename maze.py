import random

def create_maze(rows,coloms):
    maze = []
    # grid creation
    if rows % 2 == 0 :
        rows += 1
    if coloms % 2 == 0 :
        coloms += 1
    
    for _ in range(rows):
        temp = []
        for _ in range(coloms):
            temp.append(' ')
        maze.append(temp)
    
    for row in range(1,rows,2):
        for colom in range(coloms):
            maze[row][colom] = '■'
    for colom in range(1,coloms,2):
        for row in range(rows):
            maze[row][colom] = '■'        
    
    #finding the number of cells 
    row = 0
    for i in range(rows):
        if maze[i][0] == ' ':
            row += 1
    colom = 0        
    for i in range(coloms):
        if maze[0][i] == ' ':
            colom += 1
    cells = row * colom

    #
    visited = [[0,0]]
    route = [[0,0]]  
    r = 0   
    position = [0,0] #row,colom
    

    while len(visited) < cells:
        #find near cells
        near_cells = [] 
        if position[0] != 0:
            if [position[0]-2,position[1]] not in visited  :
                near_cells.append([position[0]-2,position[1],'up'])
        if  position[0] != rows - 1 :
            if [position[0]+2,position[1]] not in visited :
                near_cells.append([position[0]+2,position[1],'down'])
        if position[1] != 0 :
            if [position[0],position[1]-2] not in visited :
                near_cells.append([position[0],position[1]-2,'left'])
        if position[1] != coloms - 1 :
            if [position[0],position[1]+2] not in visited :
                near_cells.append([position[0],position[1]+2,'right']) 
        
        #  move
        if len(near_cells) != 0 :
            rand_num = random.randint(0,len(near_cells)-1)

            direction = near_cells[rand_num][2]
            if direction == 'up' :
                maze[position[0]-1][position[1]] = ' '
            elif direction == 'down' :
                maze[position[0]+1][position[1]] = ' '
            elif direction == 'left' :
                maze[position[0]][position[1]-1] = ' '
            elif direction == 'right' :
                maze[position[0]][position[1]+1] = ' '                  

            position[0] = near_cells[rand_num][0]
            position[1] = near_cells[rand_num][1]
            visited.append([position[0],position[1]]) 
            route.append([position[0],position[1]])
            r += 1 
        elif len(route) != 0:
            route.pop()
            r -= 1

            position[0] = route[r][0]
            position[1] = route[r][1] 

    maze[0][0] = '•'
    maze[rows-1][coloms-1] = '!'
    return maze , rows , coloms  


class MAZE:

    def __init__(self, rows , coloms , array=None):

        if array is None:

            self.array , self.rows , self.coloms = create_maze(rows,coloms)
            self.p_row = 0
            self.p_colom = 0

        else:
            self.coloms = coloms
            self.rows = rows    
            for i in range(rows):  
                for j in range(coloms):
                    if array[i][j] == '•' :   
                        self.p_row = i
                        self.p_colom = j
                        self.array = array
                        break 

    def show(self):
        for i in range(self.rows):
            for j in range(self.coloms):
                print(self.array[i][j], end=' ')
            print()
    
    #      TO DO
    #reset maze //have the player play again in the same maze
    #resized the maze

    def change_maze(self,array=None):
        if array is None:
            
            self.array , self.rows , self.coloms = create_maze(self.rows,self.coloms)
            self.p_row = 0
            self.p_colom = 0

        else:
            self.coloms = len(array[0])
            self.rows = len(array)    
            for i in range(self.rows):  
                for j in range(self.coloms):
                    if array[i][j] == '•' :   
                        self.p_row = i
                        self.p_colom = j
                        self.array = array
                        break 

            
    def move_up(self): 
        if self.p_row != 0 :
            if self.array[self.p_row-1][self.p_colom] == ' ':
                self.array[self.p_row-1][self.p_colom] = '•'
                self.array[self.p_row][self.p_colom] = ' '
                self.p_row = self.p_row - 1
                return False   
            elif self.array[self.p_row-1][self.p_colom] == '!':
                self.array[self.p_row-1][self.p_colom] = '•'     
                self.array[self.p_row][self.p_colom] = ' '
                self.p_row = self.p_row - 1
                return True
            else:
                print("you can't go into the wall")
                return False
        else:
            print("you can't go outside the maze")
            return False
    
    def move_down(self):
        if self.p_row != self.rows - 1 :
            if self.array[self.p_row+1][self.p_colom] == ' ':
                self.array[self.p_row+1][self.p_colom] = '•'
                self.array[self.p_row][self.p_colom] = ' '
                self.p_row = self.p_row + 1  
                return False 
            elif self.array[self.p_row+1][self.p_colom] == '!':
                self.array[self.p_row+1][self.p_colom] = '•'     
                self.array[self.p_row][self.p_colom] = ' '
                self.p_row = self.p_row + 1
                return True
            else:
                print("you can't go into the wall")
                return False
        else:
            print("you can't go outside the maze")
            return False

    def move_left(self):
        if self.p_colom != 0 :
            if self.array[self.p_row][self.p_colom-1] == ' ':
                self.array[self.p_row][self.p_colom-1] = '•'
                self.array[self.p_row][self.p_colom] = ' '
                self.p_colom = self.p_colom-1
                return False 
            elif self.array[self.p_row][self.p_colom-1] == '!':
                self.array[self.p_row][self.p_colom-1] = '•'
                self.array[self.p_row][self.p_colom] = ' '
                self.p_colom = self.p_colom-1
                return True
            else:
                print("you can't go into the wall")
                return False
        else:
            print("you can't go outside the maze")
            return False        
    

    def move_right(self):
        if self.p_colom != self.coloms - 1 :
            if self.array[self.p_row][self.p_colom + 1] == ' ':
                self.array[self.p_row][self.p_colom+1] = '•'
                self.array[self.p_row][self.p_colom] = ' '
                self.p_colom = self.p_colom+1
                return False 
            elif self.array[self.p_row][self.p_colom+1] == '!':
                self.array[self.p_row][self.p_colom+1] = '•'
                self.array[self.p_row][self.p_colom] = ' '
                self.p_colom = self.p_colom+1
                return True
            else:
                print("you can't go into the wall")
                return False
        else:
            print("you can't go outside the maze") 
            return False


def game(maze):
    win = False
    print('player = • | wall = ■ | destination = ! ')
    print('W=up | S=down | D=right | A=left ') 
    while win == False:
        maze.show()  
        print('------------------------------------------------')
        commant = input().lower()
        if commant == 'w':
            win = maze.move_up()
        elif commant == 's':
            win = maze.move_down()
        elif commant == 'a':
            win = maze.move_left()
        elif commant == 'd' :
            win = maze.move_right()
        elif commant == 'change'  :
            maze.change_maze()          
        
        if win == True :
            maze.show()  
            print('------------------------------------------------')
            print('==========WIN==========')
            commant = input().lower()
        if commant == 'change' :
            win = False
            maze.change_maze() 



maze27 = MAZE(27,27)
game(maze27) 
