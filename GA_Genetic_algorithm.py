import numpy
#Implementation d'un Algorithme génétique 

y=44.1
#2.Fitness Assignment(calcule de la fonction fitness)

def cal_pop_fitness(dataset,population):
    y_pred = numpy.sum(population*dataset, axis=1)
    fitness=1/numpy.abs(y_pred - y)
    return fitness
def select_mating_pool()