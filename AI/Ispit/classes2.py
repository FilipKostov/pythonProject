from constraint import *

if __name__=='__main__':
    problem=Problem(BacktrackingSolver)
    variables_all=list()
    variables_ml=list()
    casovi_AI=input()
    casovi_ML=input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12", "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]
    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]
    for i in range(int(casovi_R)):
        problem.addVariable(f'R_cas{i+1}', R_predavanja_domain)
        variables_all.append(f'R_cas{i+1}')
    for i in range(int(casovi_BI)):
        problem.addVariable(f'BI_cas{i+1}', BI_predavanja_domain)
        variables_ml.append(f'BI_cas{i + 1}')
    for i in range(int(casovi_ML)):
        problem.addVariable(f'ML_cas{i+1}', ML_predavanja_domain)
        variables_ml.append(f'ML_cas{i+1}')
        variables_all.append(f'ML_cas{i+1}')
    for i in range(int(casovi_AI)):
        problem.addVariable(f'AI_cas{i+1}', AI_predavanja_domain)
        variables_all.append(f'AI_cas{i+1}')



