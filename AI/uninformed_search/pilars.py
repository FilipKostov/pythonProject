from AI.searching_framework.uninformed_search import *
from AI.searching_framework.utils import Problem

class Pilar(Problem):
    def __init__(self, nr_actions,initial, goal=None):
        super().__init__(initial, goal)
        self.nr_actions=nr_actions
    @staticmethod
    def check_valid(a,b):
        if a!=None:
            if b!=None:
                if int(a[0])<int(b[0]):
                    return True
                else:
                    return False
            elif b==None:
                    return True
        else:
            return False


    def successor(self, state):
        succ=dict()
        l=list(state)
        #[['3',2','1'],[],[]]
        for i in range(0,len(l)):
            for j in range(0,len(l)):
                if i!=j and self.check_valid(l[i],l[j]):
                    pom=l
                    pom[i].pop(0)
                    pom[j]=list(l[i][0])
                    pom[j].extend(l[j])


                    succ[f'MOVE TOP BLOCK FROM PILAR {i+1} TO PILAR {j+1}']=tuple(pom)

        return succ
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        if state==self.goal:
            print(f'Number of action {self.nr_actions}')
            return True
        else:
            return False
if __name__=='__main__':
    l=input().split(';')
    nr_actions=0
    m=input().split(';')
    #['3,2,1','','']
    fin=list()
    finG=list()
    for i in range(len(l)):
        final_ini=tuple(l[i].split(','))
        fin.append(final_ini)
        #[('3','2','1'),'','']
    for j in range(len(m)):
        final_gol=tuple(m[j].split(','))
        finG.append(final_gol)
    print(fin,finG)
    pilar=Pilar(nr_actions,tuple(fin),tuple(finG))
    problem=breadth_first_graph_search(pilar)
    print(problem.solution())




