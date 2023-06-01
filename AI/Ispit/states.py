from constraint import *
def diff(a,b):
    return a!=b
if __name__=='__main__':
    problem=Problem()
    variables=['WA','NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domain=['red', 'green', 'blue']
    problem.addVariables(variables,domain)
    problem.addConstraint(diff, ('WA', 'NT'))
    problem.addConstraint(diff, ('WA','SA'))
    problem.addConstraint(diff, ('SA','NT'))
    problem.addConstraint(diff, ('SA','NSW'))
    problem.addConstraint(diff, ('WA','NT'))
    problem.addConstraint(diff, ('SA','Q'))
    problem.addConstraint(diff, ('V','SA'))
    problem.addConstraint(diff, ('NT','Q'))
    problem.addConstraint(diff, ('Q','NSW'))
    problem.addConstraint(diff, ('NSW','V'))
    print(problem.getSolution())