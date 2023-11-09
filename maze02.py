
def maze_solver():
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            print(maze[i][j], end=" ")
        print('\n')

def escape():
    current_cell = path[len(path) - 1]

    if current_cell == finish: # ถ้าเจอกับตำแหน่งสิ้นสุดจะ return maze กลับ
        print("Total Step = ")
        return

    if maze[current_cell[0] + 1][current_cell[1]] == ' ': # ถ้าตำแหน่งนั่นเท่ากับช่องว่างก็จะเดินไปแล้วเปลี่ยนเป็น S 
        maze[current_cell[0] + 1][current_cell[1]] = 'S' # ทิศใต้ (South)
        path.append([current_cell[0] + 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] + 1] == ' ': # ถ้าตำแหน่งนั่นเท่ากับช่องว่างก็จะเดินไปแล้วเปลี่ยนเป็น E 
        maze[current_cell[0]][current_cell[1] + 1] = 'E' # ทิศตะวันออก (East)
        path.append([current_cell[0], current_cell[1] + 1])
        escape()

    if maze[current_cell[0] - 1][current_cell[1]] == ' ': # ถ้าตำแหน่งนั่นเท่ากับช่องว่างก็จะเดินไปแล้วเปลี่ยนเป็น N
        maze[current_cell[0] - 1][current_cell[1]] = 'N' # ทิศเหนือ (North)
        path.append([current_cell[0] - 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] - 1] == ' ': # ถ้าตำแหน่งนั่นเท่ากับช่องว่างก็จะเดินไปแล้วเปลี่ยนเป็น W
        maze[current_cell[0]][current_cell[1] - 1] = 'W' # ทิศตะวันตก (Wast)
        path.append([current_cell[0], current_cell[1] - 1])
        escape()

    # ถ้าทางนั่นเป็นทางตันหรือตัดสินใจเดินทางผิดพลาด จะเดินย้อนรอยกลับ 
    # และเปลี่ยนตำแหน่งที่เดินไปแล้วเป็น จุด(.)
    current_cell = path[len(path) - 1]
    if current_cell != finish:
        cell_to_remove = path[len(path) - 1]
        path.remove(cell_to_remove)
        maze[cell_to_remove[0]][cell_to_remove[1]] = '.'
   

def get_starting_finishing_points():
    for i in range(len(maze)):

        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = [i ,j]
            elif maze[i][j] == 'E':
                finish = [i ,j]
                maze[i][j] = " "
            else: 
                return 0,0 # ถ้าไม่เจอ return 0,0 ออกไป
            
    #print(start)
    return start, finish

def get_maze():
    maze = []
    temp = []
    for i in f1.read().split("\n"):
        for j in i:
            temp.append(j)
        maze.append(temp)
        temp = []
    #print(maze)
    return maze
            

f1 = open("maze3.txt","r")
maze = get_maze()
 
start, finish = get_starting_finishing_points() #หาจุดเริ่มต้นแล้วจุดสิ้นสุด

if start == 0 and finish == 0: # ถ้าไม่จุดเริ่มต้นหรือจุดสิ้นสุด
    print("the maze has not found a starting point or an ending point.")
else:
    # เขาวงกตปรกติ
    path = [start]
    escape()
    print(maze_solver())