from AI.searching_framework.informed_search import *
from AI.searching_framework.utils import Problem

class Ghost(Problem):
    def __init__(self, n, holes, initial, goal=None):
        super().__init__(initial,goal)
        self.grid=n
        self.holes=holes
    @staticmethod
    def check_valid(new_state,holes,grid):
        if new_state in holes:
            return False
        if new_state[0]>grid-1 or new_state[0]<0 or new_state[1]>grid-1 or new_state[1]<0:
            return False
        return True
    def successor(self, state):
        successors=dict()

        grid=self.grid
        holes=self.holes
        x,y=state
        for i in range(3):
            new_state=x,y+i+1
            if self.check_valid(new_state, holes, grid):
                successors[f'Gore {i+1}']=new_state
        for i in range(3):
            new_state=(x+i+1,y)
            if self.check_valid(new_state, holes, grid):
                successors[f'Desno {i+1}']=new_state


        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state==self.goal
    def h(self, node):
        x,y=node.state
        z, m=self.goal
        max=abs(x-z)+abs(y-m)
        return max
if __name__=='__main__':
    print('Vnesi razmer na table: ')
    n=int(input())
    print('Vnesi broj na precki: ')
    nro=int(input())
    ghost=(0,0)
    pacman=(n-1, n-1)
    holes=list()
    for i in range(nro):
        print(f'Vnesi koordinati na precka {i}: ')
        coord_x,coord_y=input().split(", ")
        coord_x=int(coord_x)
        coord_y=int(coord_y)
        holes.append((coord_x,coord_y))
    ghost=Ghost(n, tuple(holes), ghost, pacman)
    result=astar_search(ghost)
    print(result.solution())

