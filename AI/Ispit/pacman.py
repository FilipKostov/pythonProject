from AI.searching_framework.informed_search import *
from AI.searching_framework.uninformed_search import *
from AI.searching_framework.utils import Problem


class GhostOnSkates(Problem):
    def __init__(self, initial, walls, n, goal=None):
        super().__init__(initial,goal)
        self.walls=walls
        self.n=n
    @staticmethod
    def check_valid(new_state, walls, n):
        if new_state in walls:
            return False
        x,y=new_state
        if x<0 or x>n-1 or y<0 or y>n-1:
            return False
        return True

    def successor(self, state):
        successors=dict()
        x,y=state
        for i in range(3):
            new_state=(x,y+i+1)
            if self.check_valid(new_state, self.walls, self.n):
                successors[f'Gore {i+1}']=new_state
        for i in range(3):
            new_state = (x + i + 1, y)
            if self.check_valid(new_state, self.walls, self.n):
                successors[f'Desno {i+1}']=new_state

        return successors
    def h(self, node):
        x,y=node.state
        gx,gy=self.goal
        menx_distance=abs(gx-x)+abs(gy-y)
        menx_distance=menx_distance/3
        return menx_distance
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state==self.goal
    def actions(self, state):
        return self.successor(state).keys()
if __name__=="__main__":
    n=int(input())
    num_walls=int(input())
    ghost_pos=(0,0)
    pacman=(n-1, n-1)
    walls=list()
    for i in range(num_walls):
        wall_coor=input()
        wall_str=wall_coor.split(",")
        wall=list()
        wall.append(int(wall_str[0]))
        wall.append(int(wall_str[1]))
        walls.append(tuple(wall))

    walls=tuple(walls)

    problem = GhostOnSkates(ghost_pos, walls, n, pacman)
    result=astar_search(problem)
    print(result.solution())
    #result=breadth_first_graph_search(problem)
    #result.solution()