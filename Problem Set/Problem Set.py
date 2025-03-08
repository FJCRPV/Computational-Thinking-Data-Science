"""
Computational Thinking and Data Science

Problem Set

@author: Francisco Perestrello, 39001
"""

import numpy as np
import pandas as pd
import random
import math
from itertools import combinations

# Exercise 1 

print('\nExercise 1')

def check_sum(nums, k):   
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False

# Exercise 2

# a)

inv1 = [-14200,0,0,0,0,0,11450,10530,9690]
inv2 = [-42700,0,13440,16130,15320,0,13820,0,12470,0,11260]
inv3 = [-14100,0,13890,0,0,0,0,0,9700,0,0]
inv4 = [-15900,0,13330,0,0,0,0,0,0,14630,0]
inv5 = [-24200,0,9320,10720,10080,0,8910,0,0,0,0]
inv6 = [-44700,0,13430,0,16550,14900,13410,12070,10860,0,0]
inv7 = [-3200,0,0,0,0,0,0,0,0,9230,0]
inv8 = [-11000,0,0,0,0,0,0,0,16000,0,14440]
inv9 = [-26700,0,0,14540,13230,0,0,9970,9070,8250,0]
inv10 = [-15400,0,12610,0,0,0,0,13910,0,0,0]
investments = [inv1,inv2,inv3,inv4,inv5,inv6,inv7,inv8,inv9,inv10]


def npv(cash_flows, rate):
    discounted_cashflows = []
    year = 0
    
    for i in cash_flows:
        discounted_cashflows.append(i * (1/(1+rate)**year))
        year+=1   
        
    NPV = sum(discounted_cashflows)
    return NPV    

NPV_list = []
for inv in investments:
    NPV_list.append((npv(inv, 0.1)))    

cost = []
for inv in investments:
    cost.append((inv[0]))

sorted_NPV = np.flip(np.argsort(NPV_list))
cash = 100000
n_investments = len(investments)
total_npv = 0
total_cost = 0
chosen_investments = []

for i in range(n_investments):
    new_investment = sorted_NPV[i]
    new_investment_npv = NPV_list[new_investment]
    new_investment_cost = cost[new_investment]
    
    if cash + new_investment_cost > 0:
        chosen_investments.append(new_investment+1)
        total_npv += new_investment_npv
        total_cost += new_investment_cost
        cash += new_investment_cost
    if 1 in chosen_investments:
        chosen_investments = np.append(chosen_investments, 3)
        total_cost += cost[2]
        total_npv += NPV_list[2]

print("\na)\nThe company should make the following investments: {}. The total NPV is ${} and its total cost is ${}.".format(chosen_investments, round(total_npv, 2), -total_cost))

# b)
# i)

cash = 100000
n_investments = len(investments)
total_npv = 0
total_cost = 0
chosen_investments = []

for i in range(n_investments):
    new_investment = sorted_NPV[i]
    new_investment_npv = NPV_list[new_investment]
    new_investment_cost = cost[new_investment]
    
    if cash + new_investment_cost > 0:
        chosen_investments.append(new_investment+1)
        total_npv += new_investment_npv
        total_cost += new_investment_cost
        cash += new_investment_cost
        
    if 1 in chosen_investments:
        chosen_investments = np.append(chosen_investments, 3)
        total_cost += cost[2]
        total_npv += NPV_list[2]

print("\nb)\ni)\nWith the imposed condition, the investments the company should make are {}. The total NPV is ${} and its total cost is ${}.".format(chosen_investments, round(total_npv, 2), -total_cost))


# ii)

cash = 100000
best_total_npv = -math.inf
best_total_cost = 0
best_chosen_investments = []
investments = list(range(1, 11))
n_investments = len(NPV_list)
indexlist = list(range(n_investments))
flag = True

for i in range(1, n_investments+1):
    comblist = list(combinations(indexlist,i))
    for j in range(len(comblist)):
        total_npv = 0
        total_cost = 0
        chosen_investments = []
        
        for k in range(i):
            if (4 in comblist[j]) or (5 in comblist[j]):
                total_cost += cost[comblist[j][k]]
                total_npv += NPV_list[comblist[j][k]]
                chosen_investments = np.append(chosen_investments, investments[comblist[j][k]])
                if cash >= -total_cost:
                    if total_npv > best_total_npv:
                        best_total_npv = round(total_npv, 2)
                        best_total_cost = round(total_cost, 2)
                        best_chosen_investments = chosen_investments   

print("\nb)\nii)\nWith the imposed condition, the investments the company should make are {}. The total NPV is ${} and its total cost is ${}.".format(best_chosen_investments, best_total_npv, -best_total_cost))


# Exercise 3 

graph = {
    1 : [2, 3, 4],
    2 : [],
    3 : [1, 5, 7],
    4 : [1, 5],
    5 : [3, 4, 6, 9],
    6 : [5, 7, 8, 10],
    7 : [2, 3, 6, 10],
    8 : [],
    9 : [],
    10: [6, 7, 8],
    11: [8, 9]}

visited = []
stack = []

def dfs(graph, start):
    visited.append(start)
    stack.append(start)
    
    while stack:
        s = stack.pop(0)
        
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor) 
    return visited

start = int(input("In which city would you like to start your watering supply? "))
visited = dfs(graph, start)

print("\nStarting at city {}, the maximum number of cities you can supply water to is {}. The cities are {}".format(start, len(visited), visited))


# Exercise 4 
print('\nExercise 4')

random.seed(2494)

n_employees = 300
years = 2
trials = 1000
p_total = 0.9
p_ind = 0.9

year_1 = np.zeros((trials, 1))
year_2 = np.zeros((trials, 1))

for trial in range(trials):
    employees = np.zeros((n_employees, years))
    for i in range(years):
        for j in range(len(employees)):
            employees[j][i] += np.random.choice([0, 100, 10000], p=[1-p_total, p_total*p_ind, p_total*(1-p_ind)])
                
        total_year_1 = np.sum(employees[:,0])
        total_year_2 = np.sum(employees[:,1])
    
    if total_year_1 - 300000 > 0:
        total_year_1 = total_year_1 - 300000
    else:
        total_year_1 = 0
        
    if total_year_2 - 300000 > 0:
        total_year_2 = total_year_2 - 300000
    else:
        sum_year_2 = 0
    year_1[trial] = total_year_1
    year_2[trial] = total_year_2
    
mean = np.mean(year_1+year_2)
st_dev = np.std(year_1+year_2)

print("After {} trials, the estimated mean of the amount that the insurance company will have to after 2 years is ${}, and the estimated standard deviation is ${}".format(trials, round(mean,2), round(st_dev, 2)))


# Exercise 5 
print('\nExercise 5')

random.seed(2494)

df = pd.read_excel("Auditing.xlsx", sheet_name = "Data")
N = len(df)

n = 100 #sample size

sample = random.sample(range(N),n) #this function uses Simple Random Sampling without replacement

sample_SRS = []

for k in sample:
    sample_SRS.append(df['Account Balance'][k])

X_ = np.mean(sample_SRS)
mean_est_pop_total = N*X_
std_ = np.std(sample_SRS)

se_est_pop_total = N*std_/(np.sqrt(n))

alpha = 0.05 # (1-alpha)*100% Confidence Interval
from scipy.stats import norm
quantil = norm.ppf(1-(alpha/2))

left = mean_est_pop_total - quantil*se_est_pop_total
right = mean_est_pop_total + quantil*se_est_pop_total

print("\nThe 95% Confidence Interval for the total value of 2265 savings account balances within this bank is: [$",round(left,2), ", $",round(right,2), "]")


pop_total = np.sum(df['Account Balance'])
if pop_total >= left and pop_total <= right:
    print("\nThe 95% CI does contain the actual population total in this case. The true parameter is $", round(pop_total,2))
else:
    print("\nThe 95% CI does not contain the actual population total in this case.")