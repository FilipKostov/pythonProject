from AI.searching_framework.utils import Problem
from AI.searching_framework.uninformed_search import *
class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid=(8,6)
    def successor(self, state):
        successors=dict()
        man=list(state[0])
        obstacle1=list(state[1])
        obstacle2=list(state[2])
        grid=list(self.grid)
        if obstacle1[2]==0:#up
            if obstacle1[1]==grid[1]-1:
                obstacle1[2]=1
                obstacle1[1]-=1
            elif obstacle1[1]==0:
                obstacle1[2]=1
                obstacle1[1]+=1
            else:
                obstacle1[1]+=1
        else:
            if obstacle1[1] == grid[1]-1:
                obstacle1[2] = 1
                obstacle1[1] -= 1
            elif obstacle1[1] == 0:
                obstacle1[2] = 1
                obstacle1[1] += 1
            else:
                obstacle1[1] += 1
        if obstacle2[2]==0:#up
            if obstacle2[1]==grid[1]-1:
                obstacle2[2]=1
                obstacle2[1]-=1
            elif obstacle2[1]==0:
                obstacle2[2]=1
                obstacle2[1]+=1
            else:
                obstacle2[1]+=1
        else:
            if obstacle2[1] == grid[1]-1:
                obstacle2[2] = 1
                obstacle2[1] -= 1
            elif obstacle2[1] == 0:
                obstacle2[2] = 1
                obstacle2[1] += 1
            else:
                obstacle2[1] += 1
        obstacles=[obstacle1, obstacle2]
        if man[0] < grid[0]-1 and [man[0]+1,man[1]] not in obstacles:
            successors['RIGHT']=((man[0]+1, man[1]), tuple(obstacles[0]), tuple(obstacles[1]))
        if man[0] > 0 and [man[0]-1,man[1]] not in obstacles:
            successors['DOWN']=((man[0]-1, man[1]), tuple(obstacles[0]), tuple(obstacles[1]))
        if man[1] < grid[1]-1 and [man[0],man[1]+1] not in obstacles:
            successors['UP']=((man[0], man[1]+1), tuple(obstacles[0]), tuple(obstacles[1]))
        if man[0] > 0 and [man[0],man[1]-1] not in obstacles:
            successors['DOWN']=((man[0], man[1]-1), tuple(obstacles[0]), tuple(obstacles[1]))

        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        position=tuple(state[0])
        return position==self.goal

if __name__=='__main__':
    print("Vnesi koordinati za kuca")
    house_x, house_y=input().split(", ")
    house_x=int(house_x)
    house_y=int(house_y)
    print("Vnesi koordinati za coek")
    man_x,man_y=input().split(", ")
    man_x=int(man_x)
    man_y=int(man_y)
    man=(man_x,man_y)
    house=(house_x,house_y)
    obstacle1 = (2,5,1)
    obstacle2 =(5,0,0)
    explorer=Explorer((man, obstacle1, obstacle2), house)
    result=breadth_first_graph_search(explorer)
    print(result.solution())
    print(result.solve())

