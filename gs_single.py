import numpy as np
#from pymoo.core.crossover import Crossover
#from pymoo.core.problem import elementwise_eval
#from pymoo.core.sampling import Sampling
#from pymoo.algorithms.so_genetic_algorithms import GA
from pymoo.model.problem import Problem
from pymoo.optimize import minimize
from pymoo.factory import get_algorithm, get_crossover, get_mutation, get_sampling, get_termination
#self es instancia que se esta creando
#Clases 
class MyProblem(Problem):
    def __init__(self): #hace que se ejecute cada que se hace una clase
        super().__init__(n_var= 3, #numero variables 
                        n_obj= 1, #objetivos
                        n_constr= 5, #restricciones
                        xl=np.array([0, 0, 0]), # limites inferior 
                        xu=np.array([100, 1400, 10000]), #limite superior
                        elementwise_evaluation=True

        )
    def _evaluate(self, x,out, *args, **kwargs):
        f1 = -0.6 * x[0] - 0.1 * x[1] - 0.09 * x[2] #funciones objetivo 
        g1 =  1 * x[0] + 0 * x[1] + 0 * x[2] -100 # ecuacion para primera restricción
        g2 = 0 * x[0] + 1 * x[1] + 0 * x[2] -1400
        #g3 = 0 * x[0] + 0 * x[1] + 1 * x[2] -100
        g3 = 0 * x[0] + 0 * x[1] + 1 * x[2] - max(0, (1000 -abs(np.random.normal(0,10))))
        g4 = 0.375 * x[0] + 0.05 * x[1] + 0.0045 * x[2] -180
        #g5 = 1 * x[0] + 0.15 * x[1] + 0.045 * x[2] -175
        g5 = 1 * x[0] + 0.15 * x[1] + 0.045 * x[2] - max(0, (175 -abs(np.random.normal(0,10))))
        out['F'] = f1
        out['G'] = [g1,g2,g3,g4,g5]

problem = MyProblem()
algorithm = get_algorithm('ga',
                         pop_size=50,
                         sampling = get_sampling('int_random'),
                         crossover =get_crossover('int_ux',prob= 0.25),
                         mutation = get_mutation('int_pm', prob= 0.1), eta=5)
termination = get_termination('n_gen',50)
result = minimize(problem,algorithm,termination)
print('Objetivo: {}' .format(result.F))
print('Solución: {}' .format(result.X))