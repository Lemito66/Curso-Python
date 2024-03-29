def ILP(coeficientes, LHS, RHS, type, opt):
    import pulp
    import numpy as np
    import pandas as pd
    # Inicializar el modelo
    ILP_model = pulp.LpProblem('ILP Problem', pulp.LpMinimize)
    
    # Crear una lista con las variables de decisión
    variables = list(range(len(coeficientes)))

    # Asignar a cada variable su respectivo limite inferior y superior así como el tipo de
    # cada variable, i.e. cat que puede ser igual a Integer, Binary o Continuous(default)
    x = []
    for i in range(len(coeficientes)):
        x.append(pulp.LpVariable('x_{}'.format(i), lowBound = 0, upBound = None, cat = type))
    
    # Especificar los coeficientes de la función objetivo
    objective_coefficients = dict(zip(variables, coeficientes))
    
    # Especificar si queremos maximizar ('max') o minimizar ('min') 
    if opt == 'min':
        ILP_model += sum([objective_coefficients[i] * x[i] for i in variables])
    elif opt == 'max':
        ILP_model += -sum([objective_coefficients[i] * x[i] for i in variables])
    
    # Especificar las restricciones
    for constraint in range(len(RHS)):
        ILP_model += np.dot(LHS[constraint], x) <= RHS[constraint]  
    
    # Solucionar el problema
    ILP_model.solve()
    
    # Obtener la solución y el valor de la función objetivo 
    solution = []
    for variable in variables:
        solution.append(x[variable].value())
    ILP_solution = solution
    
    if opt == 'max':
        objective_value = -pulp.value(ILP_model.objective)
    else:   
        objective_value = pulp.value(ILP_model.objective)

    print('Objective value = {}\n'.format(objective_value))

    if type == 'Integer':
        o = [{'Variable': variable.name, 'Result': variable.varValue} for variable in ILP_model.variables()]
        print(pd.DataFrame(o), '\n')

    else:
        o = [{'Variable': variable.name, 'Result': variable.varValue, 'Reduced cost': variable.dj} for variable in ILP_model.variables()]
        print(pd.DataFrame(o), '\n')

        #o = [{'Name': name, 'Shadow price': c.pi, 'Slack': c.slack} for name, c in ILP_model.constraints.items()]
        o = [{'Name': name, 'Shadow price': c.pi} for name, c in ILP_model.constraints.items()]
        print(pd.DataFrame(o))

    return ILP_solution, objective_value	