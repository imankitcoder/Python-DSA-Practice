def maze_problem(maze):
    print('original maze')
    for i in maze:
        for j in i:
            print(j,end=' ')
        print()

    #to find the boundary
    row = len(maze)
    column = len(maze[0])


    result= [[0 for j in range(column)] for i in range(row)]


    #to check in proper boundary to check path in safe or not

    def is_safe(x,y):
        if x>=0 and x>=row:
            return False
        elif y>=0 and y>=column:
            return False
        elif maze[x][y] !=1:
            return False
        else:
            return True


    def solution(x,y):
        if x==row-1 and y==column-1:
            if maze[x][y] !=1 :
                return False
            result[x][y]=1
            return True


    def is_safe(x,y):
        result[x][y]=1
        if solution (x,y+1): #forward
            return True
        if solution(x+1,y):
            return True
    result[x][y]=0


    if solution(0,0):
        return result

    else:
        return 'No path found in Maze'





    maze= [
        [1,1,0,0,1,0,0,1]
        [1,1,0,0,1,0,0,1]
        [1,1,1,1,1,0,0,1]
        [1,1,0,1,1,1,1,1]
    ]

    res= maze_problem(maze)
    print()
    if isinstance(res,list):
        for i in res:
            for j in i:
                print(j,end= ' ')

            print()

    else:
        print(res)




    
    
    
    return result