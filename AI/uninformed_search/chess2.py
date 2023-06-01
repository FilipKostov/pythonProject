from AI.searching_framework.utils import Problem
from AI.searching_framework.uninformed_search import *

def K1(bx,by,kx,ky, board): #up up left
    if 0<=kx-1<8 and 0<=ky+2<8 and [kx-1, ky+2] not in [bx,by]:
        kx-=1
        ky+=2
    return kx, ky

def K2(bx,by,kx,ky, board): #up up right
    if 0<=kx+1<8 and 0<=ky+2<8 and [kx+1, ky+2] not in [bx,by]:
        kx+=1
        ky+=2
    return kx, ky

def K3(bx,by,kx,ky, board): #right right up
    if 0<=kx+2<8 and 0<=ky+1<8 and [kx+2, ky+1] not in [bx,by]:
        kx+=2
        ky+=1
    return kx, ky

def K4(bx,by,kx,ky, board): #right right down
    if 0<=kx+2<8 and 0<=ky-1<8 and [kx+2, ky-1] not in [bx,by]:
        kx+=2
        ky-=1
    return kx, ky

def K5(bx,by,kx,ky, board): #down down right
    if 0<=kx+1<8 and 0<=ky-2<8 and [kx+1, ky-2] not in [bx,by]:
        kx+=1
        ky-=2
    return kx, ky

def K6(bx,by,kx,ky, board): #down down left
    if 0<=kx-1<8 and 0<=ky-2<8 and [kx-1, ky-2] not in [bx,by]:
        kx-=1
        ky-=2
    return kx, ky

def K7(bx,by,kx,ky, board): #left left down
    if 0<=kx-2<8 and 0<=ky-1<8 and [kx-2, ky-1] not in [bx,by]:
        kx-=2
        ky-=1
    return kx, ky

def K8(bx,by,kx,ky, board): #left left up
    if 0<=kx-2<8 and 0<=ky+1<8 and [kx-2, ky+1] not in [bx,by]:
        kx-=2
        ky+=1
    return kx, ky

#HERE IS THE HUNTER MOVEMENT

def B1(bx,by,kx,ky, board): #left up
    if 0<=bx-1<8 and 0<=by+1<8 and [bx-1, by+1] not in [kx,ky]:
        bx-=1
        by+=1
    return bx, by

def B2(bx,by,kx,ky, board): #right up
    if 0<=bx+1<8 and 0<=by+1<8 and [bx+1, by+1] not in [kx,ky]:
        bx+=1
        by+=1
    return bx, by

def B3(bx,by,kx,ky, board): #right down
    if 0<=bx+1<8 and 0<=by-1<8 and [bx+1, by-1] not in [kx,ky]:
        bx+=1
        by-=1
    return bx, by

def B4(bx,by,kx,ky, board): #left down
    if 0<=bx-1<8 and 0<=by-1<8 and [bx-1, by-1] not in [kx,ky]:
        bx-=1
        by-=1
    return bx, by
class Chess(Problem):
    def __init__(self, star_nr, initial, goal=None):
        super().__init__(initial,goal)
        self.board=(7,7)
        self.star_nr=star_nr
    def successor(self, state):
        successors=dict()
        kx=state[0]
        ky=state[1]
        bx=state[2]
        by=state[3]
        stars=list(state[4])#this is a tuple
        board=self.board
        new_k_x,new_k_y=K1(bx,by,kx,ky,board)
        if (new_k_x,new_k_y)!=(kx,ky):
            successors['K1']=(new_k_x,new_k_y,bx,by, tuple([s for s in stars if s[0]!=new_k_x or s[1]!=new_k_y]))
        new_k_x, new_k_y = K2(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K2'] = (
            new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K3(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K3'] = (
            new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K4(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K4'] = (
            new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K5(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K5'] = (
            new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K6(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K6'] = (
            new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K7(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K7'] = (
            new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K8(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K8'] = (
            new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_b_x,new_b_y=B1(bx,by,kx,ky,board)
        if(new_b_x,new_b_y)!=(bx,by):
            successors['B1']=(kx,ky,new_b_x,new_b_y,tuple([s for s in stars if s[0]!=new_b_x or s[1]!=new_b_y]))
        new_b_x, new_b_y = B2(bx, by, kx, ky, board)
        if (new_b_x, new_b_y) != (bx, by):
            successors['B2'] = (
            kx, ky, new_b_x, new_b_y, tuple([s for s in stars if s[0] != new_b_x or s[1] != new_b_y]))
        new_b_x, new_b_y = B3(bx, by, kx, ky, board)
        if (new_b_x, new_b_y) != (bx, by):
            successors['B3'] = (
            kx, ky, new_b_x, new_b_y, tuple([s for s in stars if s[0] != new_b_x or s[1] != new_b_y]))
        new_b_x, new_b_y = B4(bx, by, kx, ky, board)
        if (new_b_x, new_b_y) != (bx, by):
            successors['B4'] = (
            kx, ky, new_b_x, new_b_y, tuple([s for s in stars if s[0] != new_b_x or s[1] != new_b_y]))




        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return len(state[-1])==0

class ChessOptimized(Problem):
    def __init__(self, star_nr, initial, goal=None):
        super().__init__(initial,goal)
        self.board=(7,7)
        self.star_nr=star_nr
    def successor(self, state):
        successors = dict()
        kx = state[0]
        ky = state[1]
        bx = state[2]
        by = state[3]
        stars = list(state[4])  # this is a tuple
        board = self.board
        new_k_x, new_k_y = K1(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K1'] = (
            new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K2(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K2'] = (
                new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K3(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K3'] = (
                new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K4(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K4'] = (
                new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K5(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K5'] = (
                new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K6(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K6'] = (
                new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K7(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K7'] = (
                new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_k_x, new_k_y = K8(bx, by, kx, ky, board)
        if (new_k_x, new_k_y) != (kx, ky):
            successors['K8'] = (
                new_k_x, new_k_y, bx, by, tuple([s for s in stars if s[0] != new_k_x or s[1] != new_k_y]))
        new_bx, new_by =bx,by
        i=0
        nbx, nby = B1(new_bx, new_by, kx, ky, board)
        while (nbx,nby)!=(new_bx,new_by):
            i+=1
            new_bx, new_by=B1(new_bx,new_by,kx,ky,board)
            nbx, nby = B1(new_bx, new_by, kx, ky, board)
            successors[f'B1:{i} moves']=(kx, ky, new_bx, new_by, tuple([s for s in stars if s[0] != new_bx or s[1] != new_by]))
        new_bx, new_by = bx, by
        i = 0
        nbx, nby = B2(new_bx, new_by, kx, ky, board)
        while (nbx,nby) != (new_bx,new_by):
            i += 1
            new_bx, new_by = B2(new_bx, new_by, kx, ky, board)
            nbx, nby = B2(new_bx, new_by, kx, ky, board)
            successors[f'B2:{i} moves'] = (
            kx, ky, new_bx, new_by, tuple([s for s in stars if s[0] != new_bx or s[1] != new_by]))
        new_bx, new_by = bx, by
        i = 0
        nbx, nby = B3(new_bx, new_by, kx, ky, board)
        while (nbx,nby) != (new_bx,new_by):
            i += 1
            new_bx, new_by = B3(new_bx, new_by, kx, ky, board)
            nbx, nby = B3(new_bx, new_by, kx, ky, board)
            successors[f'B3:{i} moves'] = (
            kx, ky, new_bx, new_by, tuple([s for s in stars if s[0] != new_bx or s[1] != new_by]))
        new_bx, new_by = bx, by
        i = 0
        nbx,nby=B4(new_bx,new_by,kx,ky,board)
        while (nbx,nby) != (new_bx,new_by):
            i += 1
            new_bx, new_by = B4(new_bx, new_by, kx, ky, board)
            nbx,nby=B4(new_bx,new_by,kx,ky,board)
            successors[f'B4:{i} moves'] = (
            kx, ky, new_bx, new_by, tuple([s for s in stars if s[0] != new_bx or s[1] != new_by]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return len(state[-1])==0
if __name__=='__main__':


    knight_x=2
    knight_y=5


    bishup_x=5
    bishup_y=1
    star_nr=3


    """for i in range(star_nr):
        print(f'Enter coordinates of {i+1} star: ')
        star_x, star_y = input().split(', ')
        star_x = int(star_x)
        star_y = int(star_y)
        stars.append((star_x,star_y))"""
    stars=[(1,1),(4,3), (6,6)]
    stars=tuple(stars)
    chessboard=Chess(star_nr, (knight_x,knight_y,bishup_x,bishup_y,stars))
    chessboardOptimized=ChessOptimized(star_nr, (knight_x,knight_y,bishup_x,bishup_y,stars))
    #state: (knight_x,knight_y,bishup_x,bishup_y,stars
    result=breadth_first_graph_search(chessboard)
    resultOptimized=breadth_first_graph_search(chessboardOptimized)
    print(result.solution())
    print(result.solve())
    print(resultOptimized.solution())
    print(resultOptimized.solve())