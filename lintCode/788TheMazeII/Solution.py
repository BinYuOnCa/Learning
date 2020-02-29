from collections import deque 

class Walker: 
    tx, ty = 0, 0
    rows, cols = 0, 0
    maze = []
    
    def __init__(self, x, y, dx, dy ):
        self.x = x
        self.y = y 
        self.dx = dx
        self.dy = dy 
             
        self.steps = 0 
   
    def __str__(self):
        return '({},{})-({},{})'.format(
                self.x, self.y, self.dx, self.dy)
                
                
    def position(self):
        return (self.x, self.y)
        
    def direction(self):
        return (self.dx, self.dy)
    
    def isValid(self):
        if self.x < 0 or self.y <0 or self.x >= self.rows or self.y>= self.cols:
            return False
        if self.maze[self.x][self.y] == 1:
            return False 
        return True 
        
    def move(self):
        self.x += self.dx 
        self.y += self.dy 
        
    def back(self):
        self.x -= self.dx 
        self.y -= self.dy 
        
    def nextStep(self):
        self.move()
        ret = (self.x, self.y, self.dx, self.dy) if self.isValid() else None
        self.back()
        
        return ret  
        
    def turnLeft(self):
        self.x += self.dy 
        self.y += self.dx 
        
        ret = (self.x, self.y, self.dy, self.dx) if self.isValid() else None

        self.x -= self.dy 
        self.y -= self.dx 
        
        
        return ret 
        
    def turnRight(self):
        self.x -= self.dy 
        self.y -= self.dx 
        
        ret = (self.x, self.y, -self.dy, -self.dx) if self.isValid() else None

        self.x += self.dy 
        self.y += self.dx 
        
        return ret 
        
    def isDone(self):
        if self.x != self.tx or self.y != self.ty:
            return False 
        self.move()
        if not self.isValid():
            return True 
        self.back()
        return False 
    
            
            
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # write your code here
        
        # bfs 
        Walker.maze = maze 
        
        Walker.rows, Walker.cols = len(maze), len(maze[0])
        Walker.tx, Walker.ty = destination[0], destination[1]

        steps = -1 
        
        visited = set()
        
        q = deque()

    #    print(Walker.maze)
        
        for d in ( (0,1), (1,0), (0,-1),(-1, 0)):
            w = Walker( start[0], start[1], d[0], d[1] )
            w.move()
            if w.isValid():
                w.back()
                q.append(w)
                visited.add(w.position())
        # self.showQ(steps, q)
        while q:
            steps += 1 
  
            # self.showQ(steps, q)
            for _ in range(len(q)):
                w = q.popleft()
                if w.isDone(): 
                    return steps   
                p = w.nextStep()
                if p :
                    nw = Walker( p[0],p[1],p[2],p[3] )
                    
                    if nw.position not in visited:
                        visited.add(nw.position)
                        q.append(nw)
                        # print('nextStep:{}'.format(nw))

                        continue 
                for p  in (w.turnLeft() ,  w.turnRight()):
                    # print('p:{}'.format(p))
                    if not p:
                        continue
                    wl = Walker( p[0],p[1],p[2],p[3]  )
                    if wl.position() not in visited:
                        visited.add(wl.position())
                        q.append(wl)
                        # print('L/R:{}'.format(wl))
                        

        return -1 
    
    def showQ(self, steps, q:deque):
        print('Step {}: ['.format(steps), end = ' ')
        for x in q:
            print(x, end = ';')
        print(']')
        
if __name__ == '__main__':
    tcs = ((6,                                                              # expected result
            [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],  # Maze 
            [0,4],                                                          # start 
            [0,0],                                                          # destination 
            ),  
          (6,
            [[0,0,0,1,1,1,1,1],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0]],
            [3,0],
            [1,2],
            6 
            ),
          )
          
    sol = Solution()
    
    for tc in tcs:
        ret = sol.shortestDistance( tc[1], tc[2], tc[3])
        if ret != tc[0] or True:
            print('Maze:{}\n From {} to {} Expected: {} Returned: {}'.format( tc[1],tc[2],tc[3],tc[0],ret ))
            

