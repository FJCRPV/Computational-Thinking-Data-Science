# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:56:11 2022

@author: franc
"""
#Francisco Perestrello, 39001

#In-Class Exercises

#Exercise 1 

import numpy as np
import networkx as nx

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11])  #setting up the nodes, where A->1, B->2, etc
G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(2,7),(3,7),(3,5),(4,5),(5,6),(5,9),(5,10),(6,7),(6,8),(6,9),(7,8),(8,9),(8,11),(9,10),(9,11),(10,11)]) #setting up the edges

def BFS(G,s): #G is the graph, s is the initial node
    visited = np.zeros(G.number_of_nodes()) #array of zeros representing the nodes we HAVEN'T visited. Once visited, it is going to turn each entry from a 0 into a 1
    prev_node = np.zeros(G.number_of_nodes()) #array of zeros representing the last we were in. Once a node is visited, the next entry will turn into the last node visited
    queue = []
    queue.append((s,0)) #(s,0) is the starting point
    
    while not len(queue) == 0:
        u, prev_u = queue.pop(0) #(u,prev_u) is the representation of the possibilities of nodes. If A can go to B or C only, the two possibilities are (B,A) and (C,A)
        if visited[u-1] == 0: #if we haven't visited the node yet
            visited[u-1] = 1 #we go there, so we must change it from a 0 to a 1 in the array. (u-1 because the first entry of arrays in python is v[0])
            prev_node[u-1] = prev_u #changing the next entry of the array to the previous node we were in
            neighbors = list(G.neighbors(u)) #find the possibilities of paths from where we are
            neighbors.reverse() #this way we get from Z to A, just like in the slides
            for w in neighbors:
                if visited[w-1] == 0: #if we haven't visited the node yet
                    queue.append((w,u)) #we go there
    return prev_node


"""SHORTEST PATCH ALGORITHM"""

#all three functions follow the same logic. The comments made on the first function also apply to the other two.

def shortestpath_total(G,s,t):
    nodes = BFS(G,s) #prev_node array from BFS
    stop = False 
    n = t
    total_path = int(t)
    total_distance = 0
    while not stop: 
        if int(nodes[n-1]) != 0: #because when it is 0, we are in our initial point. this connection is built backwards
            total_path = np.append(total_path,int(nodes[n-1])) #appending the previous node we were in to our total path
            total_distance += 1 #it increases the distance by one
            n = int(nodes[n-1]) #again, this connection is built backwards
        else:
            stop = True #when we are in our initial point, the search is over
    return total_path, total_distance

def shortestpath_to_k(G,s,k):
    nodes = BFS(G,s) #prev_node array from BFS
    stop = False
    n = k
    path_to_k = int(k)
    distance_to_k = 0
    while not stop:
        if int(nodes[n-1]) != 0: #because when it is 0, we are in our initial point. this connection is built backwards
            path_to_k = np.append(path_to_k,int(nodes[n-1]))
            distance_to_k += 1
            n = int(nodes[n-1])
        else:
            stop = True
    return path_to_k, distance_to_k

def shortestpath_from_k(G,k,t):
    nodes = BFS(G,k) #prev_node array from BFS
    stop = False
    n = t
    path_from_k = int(t)
    distance_from_k = 0
    while not stop:
        if int(nodes[n-1]) != 0: #because when it is 0, we are in our initial point. this connection is built backwards
            path_from_k = np.append(path_from_k,int(nodes[n-1]))
            distance_from_k += 1
            n = int(nodes[n-1])
        else:
            stop = True
    return path_from_k, distance_from_k

s = int(input("What is the starting node? "))
t = int(input("What is the final node? "))
k = int(input("Where do you want to stop? "))
delta = int(input("What percentage of the total distance are you okay with sacrificing? "))/100

shortest_total_path, min_total_distance = shortestpath_total(G,s,t)
shortest_path_to_k, min_distance_to_k = shortestpath_to_k(G,s,k)
shortest_path_from_k, min_distance_from_k = shortestpath_from_k(G,k,t)

STP = list(shortest_total_path)
STP.reverse() #this helps us get the path in the correct order, from the starting point to the final point
SP_to_k = list(shortest_path_to_k)
SP_to_k.reverse()
SP_from_k = list(shortest_path_from_k)
SP_from_k.reverse()

min_distance_with_k = min_distance_to_k + min_distance_from_k
shortest_path_with_k = np.append(SP_to_k, SP_from_k)
ratio = min_distance_with_k/min_total_distance

if ratio > min_total_distance*(1+delta): #if the path increases by more than delta%, we won't stop at k
    print("\nIt is not possible to stop at node", k, "without increasing the length of your path by more than", delta*100, "percent.\nThe shortest path from node", s, "to node", t, "is", STP, "and it is a distance of", min_total_distance)
else: #if it increases by less or equal than delta%, we will stop at k
    print("\nThe shortest path from node", s, "to node", t, "while stopping at node", k, "is", shortest_path_with_k, "and it is a distance of", min_distance_with_k)
