from constraint import *
def notAttacking(a,b):
    return a[0]!=b[0] and a[1]!=b[1]
if __name__=='__main__':
    problem=Problem()
    domain=[(i,j) for i in range(0,8) for j in range (0,8)]

    rooks=range(1,9)
    problem.addVariables(rooks, domain)
    for i in rooks:
        for j in rooks:
            if i!=j:
                problem.addConstraint(notAttacking, (i,j))
    print(problem.getSolution())