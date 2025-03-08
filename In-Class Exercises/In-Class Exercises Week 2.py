# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:26:33 2022

@author: Francisco
"""

#Exercise 1

import numpy as np
from itertools import permutations

def BruteForce(ncities):
    best_distance = float("inf")
    cities = ["A", "B", "C", "D", "E"]
    indexlist = list(range(ncities))


    distance = np.array([[0, 120, 220, 150, 210], [120, 0, 80, 110, 130], [220, 80, 0, 160, 185], [150, 110, 160, 0, 190], [210, 130, 185, 190, 0]]) #setting up the distances

    for p in range(1, ncities+1): 
        citieslist = list(permutations(cities, p)) #creating all possible permutations of cities
        citieslist = [list(x) for x in citieslist] #this just serves to change the brackets to straight brackets
        citieslist = [m for m in citieslist if m[0] == "A"] #keep only permutations that begin in city A
        for x in citieslist:
            x.append("A") #adding the final destinantion A in every permutation

    for p in range(1, ncities+1): #Doing the same work but for the indexes
        indexlist_perm = list(permutations(indexlist, p))
        indexlist_perm = [list(x) for x in indexlist_perm]
        indexlist_perm = [m for m in indexlist_perm if m[0] == 0]
        for x in indexlist_perm:
            x.append(0)

    for solution in indexlist_perm:
        dist = distance[solution[0], solution[1]] + distance[solution[-2], solution[-1]] #calculating the distance between the first city and A, and the final city and A

        for i in range(1, len(solution)-2):
            dist += distance[solution[i], solution[i+1]] #calculating and summing the distance between the cities in the middle
        if dist < best_distance:
            best_distance = dist
            best_solution = citieslist[i]
    return best_solution, best_distance

ncities = int(input("Including A, how many cities would you like to visit up to a maximum of 5?: "))

if ncities > 2 and ncities < 6:
    best_solution, best_distance = BruteForce(ncities)
    print("The best route for visiting {} cities is: {}".format(ncities, best_solution))
    print("\nThe total distance traveled is: {} km".format(best_distance))

elif ncities <= 1 or ncities > 5:
    print("That is not a valid number of cities")

else:
    best_solution, best_distance = ["A", "B", "A"], 240 #if the user just wants to go to one other city, he should choose the closest city, wich is 120km apart
    print("The best route for visiting {} cities is: {}".format(ncities, best_solution))
    print("\nThe total distance traveled is: {} km".format(best_distance))
    

#Exercise 2

cities = [0, 1, 2, 3, 4] #cities indexes
cities_names = ["A", "B", "C", "D", "E"]


def Greedy(n):
    
    start = n
    current_city = start
    total_distance = 0
    cities_visited = [current_city]
    distances = []
    cities.remove(current_city)


    distance = np.array([[0, 120, 220, 150, 210], [120, 0, 80, 110, 130], [220, 80, 0, 160, 185], [150, 110, 160, 0, 190], [210, 130, 185, 190, 0]])
    
    while len(cities_visited) != 5:
        if int(distance.argsort()[current_city][0]) not in cities_visited: #if the shortest distance is not in the visited city
            next_city = int(distance.argsort()[current_city][0]) #go there
        else:
            checking = distance.argsort() 
            while checking[current_city][0] in cities_visited:
                checking = np.delete(checking, 0, 1) #else delete it from the array of possibilities
            next_city = checking[current_city][0] #go to the shortest distance left in the array of possibilities

        total_distance += distance[current_city][next_city]
        distances.append(distance[current_city][next_city])
        current_city = next_city
        cities_visited.append(next_city)

    total_distance += distance[cities_visited[-1]][n]
    return total_distance, cities_visited, start


n = int(input("Knowing that city A is 0, city B is 1, city C is 2, city D is 3, and city E is 4, where would you like to start your journey? "))
if n in cities:
    best_distance, best_route, start = Greedy(n)
    best_route.append(start)
    
    print("The optimal route is {} and it is {} km long.".format(best_route, best_distance))
else:
    print("That's not a valid city! Try again.")