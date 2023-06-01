from AI.searching_framework.informed_search import astar_search
from AI.searching_framework.utils import Problem

class House(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
    def successor(self, state):
        successors=dict()
        x = state[0]
        y = state[1]
        obstacle_1 = [state[2], state[3], state[4]]
        obstacle_2 = [state[5], state[6], state[7]]
        if obstacle_1[2] == 1:#up
            if obstacle_1[1]==5:
                obstacle_1[2]=-1
                obstacle_1[1]-=1
            else:
                obstacle_1[1]+=1
        else:
            if obstacle_1[1]==0:
                obstacle_1[2]=1
                obstacle_1[1]+=1
            else:
                obstacle_1[1]-=1

        if obstacle_2[2] == 1:#up
            if obstacle_2[1]==5:
                obstacle_2[2]=-1
                obstacle_2[1]-=1
            else:
                obstacle_2[1]+=1
        else:
            if obstacle_2[1]==0:
                obstacle_2[2]=1
                obstacle_2[1]+=1
            else:
                obstacle_2[1]-=1

        obstacles=[[obstacle_1[0], obstacle_1[1]], [obstacle_2[0], obstacle_2[1]]]
        checker=[obstacle_1[2], obstacle_2[2]]
        if x<7 and [x,y] not in obstacles:
            successors["RIGHT"] = (x+1, y, obstacles[0][0], obstacles[0][1],checker[0], obstacles[1][0], obstacles[1][1], checker[1])
        if x > 0 and [x, y] not in obstacles:
            successors["LEFT"] = (x - 1, y, obstacles[0][0], obstacles[0][1],checker[0], obstacles[1][0], obstacles[1][1], checker[1])
        if y < 5  and [x, y] not in obstacles:
            successors["UP"] = (x, y+1, obstacles[0][0], obstacles[0][1],checker[0], obstacles[1][0], obstacles[1][1],checker[1])
        if y>0 and [x, y] not in obstacles:
            successors["DOWN"] = (x , y-1, obstacles[0][0], obstacles[0][1],checker[0], obstacles[1][0], obstacles[1][1],checker[1])
        return successors

    def result(self, state, action):
        return self.successor(state)[action]
    def actions(self, state):
        return self.successor(state).keys()
    def goal_test(self, state):
        return state[0]==self.goal[0] and state[1]==self.goal[1]
    def h(self, node):
        x = node.state[0]
        y = node.state[1]
        x1 = self.goal[0]
        y1 = self.goal[1]
        return abs(x - x1) + abs(y - y1)
if __name__=="__main__":
    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())

    house = [house_x, house_y]
    explorer = House((man_x, man_y, 2, 5, -1, 5, 0, 1), house)

    answer = astar_search(explorer)
    print(answer.solution())
