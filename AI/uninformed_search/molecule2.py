from AI.searching_framework.utils import Problem
from AI.searching_framework.uninformed_search import *
def move_left(x1,x2,y1,y2,z1,z2,obstacles):
    obstacles=list(obstacles)
    while x1>0 and [x1-1,x2] not in obstacles and [x1-1,x2]!=[y1,y2] and [x1-1,x2]!=[z1,z2]:
        x1-=1
    return x1
def move_right(x1,x2,y1,y2,z1,z2, obstacles):
    obstacles = list(obstacles)
    while x1<8 and [x1+1,x2] not in obstacles and [x1+1,x2]!=[y1,y2] and [x1+1,x2]!=[z1,z2]:
        x1+=1
    return x1
def move_up(x1,x2,y1,y2,z1,z2, obstacles):
    obstacles = list(obstacles)
    while x2<6 and [x1, x2+1] not in obstacles and [x1,x2+1]!=[y1,y2] and [x1,x2+1]!=[z1,z2]:
        x2+=1
    return x2
def move_down(x1,x2,y1,y2,z1,z2, obstacles):
    obstacles = list(obstacles)
    while x2>0 and [x1, x2-1] not in obstacles and [x1,x2-1]!=[y1,y2] and [x1,x2-1] != [z1,z2]:
        x2-=1
    return  x2


class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial,goal)
        self.obstacles=obstacles
        self.grid=(7,5)
    def successor(self, state):
        successors=dict()
        h1_x=state[0]
        h1_y=state[1]
        obstacles=self.obstacles
        grid=self.grid
        o_x=state[2]
        o_y=state[3]
        h2_x=state[4]
        h2_y=state[5]
        #H1
        new_h1_x=move_left(h1_x,h1_y,o_x,o_y,h2_x,h2_y, obstacles)
        if (new_h1_x,h1_y)!=(h1_x,h1_y):
            successors['MOVE H1 LEFT']=(new_h1_x,h1_y,o_x,o_y,h2_x,h2_y)
        new_h1_x= move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obstacles)
        if (new_h1_x, h1_y) != (h1_x, h1_y):
            successors['MOVE H1 RIGHT'] = (new_h1_x,h1_y, o_x, o_y, h2_x, h2_y)
        new_h1_y = move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obstacles)
        if (h1_x, new_h1_y) != (h1_x, h1_y):
            successors['MOVE H1 UP'] = (h1_x, new_h1_y, o_x, o_y, h2_x, h2_y)
        new_h1_y = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obstacles)
        if (h1_x, new_h1_y) != (h1_x, h1_y):
            successors['MOVE H1 DOWN'] = (h1_x, new_h1_y, o_x, o_y, h2_x, h2_y)
        #O
        new_o_x = move_left(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obstacles)
        if (new_o_x,o_y) != (o_x, o_y):
            successors['MOVE O LEFT'] = (h1_x, h1_y, new_o_x,o_y, h2_x, h2_y)
        new_o_x = move_right(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obstacles)
        if (new_o_x, o_y) != (o_x, o_y):
            successors['MOVE O RIGHT'] = (h1_x, h1_y, new_o_x, o_y, h2_x, h2_y)
        new_o_y = move_up(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obstacles)
        if (o_x, new_o_y) != (o_x, o_y):
            successors['MOVE O UP'] = (h1_x, h1_y, o_x, new_o_y, h2_x, h2_y)
        new_o_y = move_down(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obstacles)
        if (o_x, new_o_y) != (o_x, o_y):
            successors['MOVE O DOWN'] = (h1_x, h1_y, o_x, new_o_y, h2_x, h2_y)
        #H2
        new_h2_x = move_left(h2_x, h2_y, h1_x, h1_y, o_x, o_y, obstacles)
        if (new_h2_x, h2_y) != (h2_x, h2_y):
            successors['MOVE H2 LEFT'] = (h1_x, h1_y, o_x, o_y, new_h2_x, h2_y)
        new_h2_x = move_right(h2_x, h2_y, h1_x, h1_y, o_x, o_y, obstacles)
        if (new_h2_x, h2_y) != (h2_x, h2_y):
            successors['MOVE H2 RIGHT'] = (h1_x, h1_y, o_x, o_y, new_h2_x, h2_y)
        new_h2_y = move_up(h2_x, h2_y, h1_x, h1_y, o_x, o_y, obstacles)
        if (h2_x, new_h2_y) != (h2_x, h2_y):
            successors['MOVE H2 UP'] = (h1_x, h1_y, o_x, o_y, h2_x, new_h2_y)
        new_h2_y = move_down(h2_x, h2_y, h1_x, h1_y, o_x, o_y, obstacles)
        if (h2_x, new_h2_y) != (h2_x, h2_y):
            successors['MOVE H2 DOWN'] = (h1_x, h1_y, o_x, o_y, h2_x, new_h2_y)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] == state[3] == state[5] and state[0] + 1 == state[2] and state[2] + 1 == state[4]




if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos = [7, 2]

    molecule = Molecule(obstacles_list, (h1_pos[0], h1_pos[1], o_pos[0], o_pos[1], h2_pos[0], h2_pos[1]))
    #state is (h1_pos[0], h1_pos[1], o_pos[0], o_pos[1], h2_pos[0], h2_pos[1])
    result = breadth_first_graph_search(molecule)
    print(result.solution())
    print(result.solve())
