"""
Francisco Perestrello, 39001
"""

# Exercise 1

import numpy as np
import random
random.seed(2949)
import matplotlib.pyplot as plt

possible_mov_1 = [[1,0], [0,1], [-1,0], [0,-1]] # the set of possible movements for Drunken man 1: right/up/left/down
possible_mov_2 = [[1,0], [-1,0], [0,1], [0,-2]] # the set of possible movements for Drunken man 2: right/left/up/down-down
possible_mov_3 = [[1,0], [-1,0]] # the set of possible movements for Drunken man 3: right/left

initial_pos = [0,0]
ntrials = 100 # the number of paths that we are going to simulate

def distance(p1,p2):
    # calculates the distance between two points in R2
    distance = np.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
    return distance

def path(ip, mov, nsteps):
    # generates a random path with length = nsteps
    current_pos = ip
    for k in range(nsteps):
        i = random.randint(1,len(mov))
        current_pos = np.sum([current_pos, mov[i-1]], axis = 0)
    distance_path = distance(ip, current_pos) # calculates the distance from the 
                                                # initial position to the last one
    return distance_path

def trial(ip, mov, nsteps, ntrials):
    # calculates the average, maximum, and minimum distance from a sequence of ntrials
    # paths with length equal to nsteps
    distvector = np.zeros(ntrials)
    for k in range(ntrials):
        distvector[k] = path(ip, mov, nsteps)
    return round(np.mean(distvector),4)

print("\n\nExercise 1\n")
nsteps = int(input("Enter the length of the path (positive integer): "))
ntrials = int(input("Enter the number of paths that should be generated (positive integer): "))

Mean_1 = trial(initial_pos, possible_mov_1, nsteps, ntrials)
Mean_2 = trial(initial_pos, possible_mov_2, nsteps, ntrials)
Mean_3 = trial(initial_pos, possible_mov_3, nsteps, ntrials)
print("\n\nRandom Walk of ", nsteps, " steps:")
print("\nDrunken Man Number 1 \nMean distance: ", Mean_1)
print("\nDrunken Man Number 2 \nMean distance: ", Mean_2)
print("\nDrunken Man Number 3 \nMean distance: ", Mean_3)
      
# Exercise 2

Walk_1_x = np.zeros(nsteps)
Walk_1_y = np.zeros(nsteps)
Walk_2_x = np.zeros(nsteps)
Walk_2_y = np.zeros(nsteps)
Walk_3_x = np.zeros(nsteps)
Walk_3_y = np.zeros(nsteps)

def path_taken(ip, mov, nsteps):
    # defines the path taken by the three drunkards
    for k in range(1,nsteps):
        i = random.randint(1,len(mov))
        if i == 1:
            Walk_1_x[k] = Walk_1_x[k-1] + 1 #move right
            Walk_1_y[k] = Walk_1_y[k-1]
            Walk_2_x[k] = Walk_2_x[k-1] + 1 #move right
            Walk_2_y[k] = Walk_2_y[k-1]
            Walk_3_x[k] = Walk_3_x[k-1] + 1 #move right
            Walk_3_y[k] = Walk_3_y[k-1]
        elif i == 2:
            Walk_1_x[k] = Walk_1_x[k-1]
            Walk_1_y[k] = Walk_1_y[k-1] + 1 #move up
            Walk_2_x[k] = Walk_2_x[k-1] - 1 #move left
            Walk_2_y[k] = Walk_2_y[k-1]
            Walk_3_x[k] = Walk_3_x[k-1] - 1 #move left
            Walk_3_y[k] = Walk_3_y[k-1]
        elif i == 3:
            Walk_1_x[k] = Walk_1_x[k-1] - 1 #move left
            Walk_1_y[k] = Walk_1_y[k-1]
            Walk_2_x[k] = Walk_2_x[k-1]
            Walk_2_y[k] = Walk_2_y[k-1] + 1 #move up
        else:
            Walk_1_x[k] = Walk_1_x[k-1]
            Walk_1_y[k] = Walk_1_y[k-1] - 1 #move down
            Walk_2_x[k] = Walk_2_x[k-1]
            Walk_2_y[k] = Walk_2_y[k-1] - 2 #move down-down

path_taken(initial_pos, possible_mov_1, nsteps)
plt.plot(Walk_1_x, Walk_1_y, label = "Drunkard 1")
plt.plot(Walk_2_x, Walk_2_y, label = "Drunkard 2")
plt.plot(Walk_3_x, Walk_3_y, label = "Drunkard 3")
plt.legend(loc="lower right")
plt.annotate("Starting Point", (0,0))
plt.plot(0,0, marker= "o", markersize = 5)
plt.title("Random walks of the three drunkards")


# Exercise 3

door_numbers = [1, 2, 3]
wanted_award = "car"
unwanted_award = "goat"
awards = [wanted_award, unwanted_award, unwanted_award]

def monte_carlo_trial(initial_door_number, should_switch): #one single game
    random.shuffle(awards)
    doors = dict(zip(door_numbers, awards))
    remaining_door_numbers = [x for x in door_numbers if x != initial_door_number]
    for door_number in remaining_door_numbers:
        if doors[door_number] == unwanted_award:
            remaining_door_numbers.remove(door_number)
            break

    switched_door_number = remaining_door_numbers[0]
    if should_switch:
        final_door_number = switched_door_number
    else:
        final_door_number = initial_door_number
    if doors[final_door_number] == wanted_award:
        won_car = True
    else:
        won_car = False
    return won_car

def monte_carlo_simulation(trial_number, should_switch): #performs a given number of simulations and calculates the probabilities of winning the car
    winning_counts = 0
    for trial_i in range(trial_number):
        initial_pick = random.choice(door_numbers)
        won_car = monte_carlo_trial(initial_pick, should_switch)
        winning_counts += int(won_car)
    winning_prob = winning_counts/trial_number
    print(f"\nNumber of times the game is simulated: {trial_number} times\n"
          f"Switching status: {should_switch}\n"
          f"Probability of winning the car: {winning_prob:.2%}")
    
print("\n\nExercise 3\n")
trial_number = int(input("Mary, how many times would you like to simulate the game? "))
monte_carlo_simulation(trial_number, True)
monte_carlo_simulation(trial_number, False)