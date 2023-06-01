from AI.searching_framework.utils import Problem
from AI.searching_framework.uninformed_search import *

#HERE IS THE HORSE MOVEMENT

def k1(k_x, k_y, h_x,h_y): #up up left
    if 0<=k_x-1<8 and 0<=k_y+2<8 and [k_x-1, k_y+2] not in [h_x,h_y]:
        k_x-=1
        k_y+=2
    return k_x, k_y

def k2(k_x, k_y, h_x,h_y): #up up right
    if 0<=k_x+1<8 and 0<=k_y+2<8 and [k_x+1, k_y+2] not in [h_x,h_y]:
        k_x+=1
        k_y+=2
    return k_x, k_y

def k3(k_x, k_y, h_x,h_y): #right right up
    if 0<=k_x+2<8 and 0<=k_y+1<8 and [k_x+2, k_y+1] not in [h_x,h_y]:
        k_x+=2
        k_y+=1
    return k_x, k_y

def k4(k_x, k_y, h_x,h_y): #right right down
    if 0<=k_x+2<8 and 0<=k_y-1<8 and [k_x+2, k_y-1] not in [h_x,h_y]:
        k_x+=2
        k_y-=1
    return k_x, k_y

def k5(k_x, k_y, h_x,h_y): #down down right
    if 0<=k_x+1<8 and 0<=k_y-2<8 and [k_x+1, k_y-2] not in [h_x,h_y]:
        k_x+=1
        k_y-=2
    return k_x, k_y

def k6(k_x, k_y, h_x,h_y): #down down left
    if 0<=k_x-1<8 and 0<=k_y-2<8 and [k_x-1, k_y-2] not in [h_x,h_y]:
        k_x-=1
        k_y-=2
    return k_x, k_y

def k7(k_x, k_y, h_x,h_y): #left left down
    if 0<=k_x-2<8 and 0<=k_y-1<8 and [k_x-2, k_y-1] not in [h_x,h_y]:
        k_x-=2
        k_y-=1
    return k_x, k_y

def k8(k_x, k_y, h_x,h_y): #left left up
    if 0<=k_x-2<8 and 0<=k_y+1<8 and [k_x-2, k_y+1] not in [h_x,h_y]:
        k_x-=2
        k_y+=1
    return k_x, k_y

#HERE IS THE HUNTER MOVEMENT

def b1(k_x, k_y, h_x,h_y): #left up
    if 0<=h_x-1<8 and 0<=h_y+1<8 and [h_x-1, h_y+1] not in [k_x,k_y]:
        h_x-=1
        h_y+=1
    return h_x, h_y

def b2(k_x, k_y, h_x,h_y): #right up
    if 0<=h_x+1<8 and 0<=h_y+1<8 and [h_x+1, h_y+1] not in [k_x,k_y]:
        h_x+=1
        h_y+=1
    return h_x, h_y

def b3(k_x, k_y, h_x,h_y): #right down
    if 0<=h_x+1<8 and 0<=h_y-1<8 and [h_x+1, h_y-1] not in [k_x,k_y]:
        h_x+=1
        h_y-=1
    return h_x, h_y

def b4(k_x, k_y, h_x,h_y): #left down
    if 0<=h_x-1<8 and 0<=h_y-1<8 and [h_x-1, h_y-1] not in [k_x,k_y]:
        h_x-=1
        h_y-=1
    return h_x, h_y

class Chess(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)


    def successor(self, state):
        successors = dict()

        knight_x = state[0][0]
        knight_y = state[0][1]

        bishop_x = state[1][0]
        bishop_y = state[1][1]
        stars_positions = state[2]

        #EXAMPLE OF WHAT YOU CAN DO
        if (knight_x, knight_y) != (k1(knight_x, knight_y, bishop_x, bishop_y)):
            successors['K1'] = ((k1(knight_x, knight_y, bishop_x, bishop_y)), (bishop_x, bishop_y),
                                tuple([s for s in stars_positions if s[0] != [k1(knight_x, knight_y, bishop_x, bishop_y)][0] or s[1] != [k1(knight_x, knight_y, bishop_x, bishop_y)][1]]))

        new_x, new_y = k2(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors['K2'] = ((new_x, new_y), (bishop_x, bishop_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = k3(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors['K3'] = ((new_x, new_y), (bishop_x, bishop_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = k4(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors['K4'] = ((new_x, new_y), (bishop_x, bishop_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = k5(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors['K5'] = ((new_x, new_y), (bishop_x, bishop_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = k6(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors['K6'] = ((new_x, new_y), (bishop_x, bishop_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = k7(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors['K7'] = ((new_x, new_y), (bishop_x, bishop_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = k8(knight_x, knight_y, bishop_x, bishop_y)
        if [knight_x, knight_y] != [new_x, new_y]:
            successors['K8'] = ((new_x, new_y), (bishop_x, bishop_y), tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        #BISHOP

        new_x, new_y = b1(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [new_x, new_y]:
            successors['B1'] = ((knight_x, knight_y), (new_x, new_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = b2(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [new_x, new_y]:
            successors['B2'] = ((knight_x, knight_y), (new_x, new_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = b3(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [new_x, new_y]:
            successors['B3'] = ((knight_x, knight_y), (new_x, new_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))

        new_x, new_y = b4(bishop_x, bishop_y, knight_x, knight_y)
        if [bishop_x, bishop_y] != [new_x, new_y]:
            successors['B4'] = ((knight_x, knight_y), (new_x, new_y),
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y]))


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


    def goal_test(self, state):
        return len(state[-1]) == 0


if __name__=="__main__":
    print("Enter coordinates for Horse:")
    k_x=int(input())
    k_y=int(input())
    print("Enter coordinates for Hunter:")
    h_x = int(input())
    h_y = int(input())
    print("Enter star number:")
    n = int(input())
    print("Enter coordinates for Stars:")
    stars=list()
    for i in range(0,n):
        print(f"Enter coordinates for {i+1} Star:")
        s_x = int(input())
        s_y = int(input())
        stars.append((s_x, s_y))
    stars = tuple(stars)
    chess=Chess(((k_x, k_y), (h_x,h_y), stars))
    result = breadth_first_graph_search(chess)
    print(result.solution())
