import numpy
import GA_Genetic_Algorithme
"y=w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6 "
#data set
#parametres d'un algorithme génétique:(à définir par le data scientis)
#1.nombre des solution par population = taille de la population
#2.taille de la solution 
#3.nombre des parents
#4.intervalle des valeurs à générer
#5.nombre des génération )
#imporation des données
Data_inputs = [4, -2, 7, 5, 11, 1]

#définir le nombre des poids == nombre des variable de décision(xi)==6
num_weights = len(Data_inputs)

#Taille de la population
solution_per_population = 6

#Mating pool size
num_parents_mating = 3

#Définir la taille de la population
Population_size = (solution_per_population , num_weights)

#1.Initialization (la géneration aléatoire de la premier population )
new_population = numpy.random.uniform(low =-12 , high = 12 , size = Population_size)

Number_generation = 100
for generation in range (Number_generation):
    print("c'est le génération:" , generation )
    
    #2.Fitness Assignment(calcule de la fonction fitness)
    fitness = GA_Genetic_Algorithme.cal_pop_fitness(Data_inputs,new_population)
    print("Fitness",fitness)
    
    #3.Selection
    #parent = GeneticAlgorithm.select.mating_pool()

    #4.Crossover
    
    #5.Mutation