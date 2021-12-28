
#importing the required libraries


from pyamaze import maze,agent,textLabel
from queue import PriorityQueue
#for heuristic function manhataan distance is used
#function h is used to calculate heuristic function
#heuristic is the estimate cost from particular node to the goal
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m):
    start=(m.rows,m.cols)
    '''
    g_score is the actual cost of path from start node torespective node
    f_score is the sum of g_score and the the heuristic function of that particular node

    initially as h_score and g_score are unknown its initialized with the infinity
    '''
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))
    '''
    priority queue is used for the implementing the a star algorithm where priority is given to f_score of particular node
    '''
    open=PriorityQueue()
    open.put((f_score[start],h(start,(1,1)),start))
    aPath={}
     
     # cols--> No. of columns of the maze
      #  Need to pass just the two arguments. The rest will be assigned automatically
       # maze_map--> Will be set to a Dicationary. Keys will be cells and
        #            values will be another dictionary with keys=['E','W','N','S'] for
         #           East West North South and values will be 0 or 1. 0 means that 
          #          direction(EWNS) is blocked. 1 means that direction is open.
       # grid--> A list of all cells
       # path--> Shortest path from start(bottom right()) to goal(by default top left(1,1))
        #        It will be a dictionary
       
       # _agents-->  A list of aganets on the maze
     
    while not open.empty():
        currCell=open.get()[2]
        #if the current cell is the goal we end our process
        if currCell==(1,1):
            break
        for d in 'ESNW':

            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))
                #if the new g_score and f_score are less than the previous one then we update the previous one with new one
                #and add it in the queue
                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    '''
    after performing the above steps we get path in reversed direction which will be reversed
    '''                
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(10,10)
    m.CreateMaze()
    path=aStar(m)

    a=agent(m,footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'A Star Path Length',len(path)+1)

    m.run()