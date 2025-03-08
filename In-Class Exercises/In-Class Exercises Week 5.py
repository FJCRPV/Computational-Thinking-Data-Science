"""
@author: Francisco Perestrello, 39001
"""

#Exercise 1

print("\nExercise 1\n")

import numpy as np
import pandas as pd
import random

random.seed(2494)

df = pd.read_excel("In-Class Exercises Week 5 Data - Quality.xlsx", sheet_name = "Sheet1")
N = len(df)

n = 25 #sample size

sample = random.sample(range(N),n) #this function uses Simple Random Sampling without replacement

sample_SRS = []

for k in sample:
    sample_SRS.append(df.Proportion[k])

X_ = np.mean(sample_SRS)
std_ = np.std(sample_SRS)

if n/N > 0.05:
    factor = np.sqrt((N-n)/(N-1))
else:
    factor = 1

alpha = 0.05 # (1-alpha)*100% Confidence Interval
from scipy.stats import norm
quantil = norm.ppf(1-(alpha/2))

left = X_ - quantil*factor*std_/np.sqrt(n)
right = X_ + quantil*factor*std_/np.sqrt(n)

print("\nThe 95% Confidence Interval for the mean proportion of defective items over all monthly shipments is: [",round(left,3), ",",round(right,3), "]")


pop_mean = np.mean(df.Proportion)
if pop_mean >= left and pop_mean <= right:
    print("The 95% CI does contain the actual population mean in this case. The true parameter is", round(pop_mean,3))
else:
    print("The 95% CI does not contain the actual population mean in this case.")
    
print("\nIt is expected that 95% of many similarly constructed confidence intervals include the true population mean.")


#Exercise 2

print("\n\nExercise 2\n")

df2 = pd.read_excel("In-Class Exercises Week 5 Data - SoftDrink.xlsx", sheet_name = "Sheet1")
n = len(df2)

our_brand = df2[df2.Preference == "Our brand"]
p_hat = len(our_brand)/n
se_prop = np.sqrt(p_hat*(1-p_hat)/n)

alpha = 0.1 # (1-alpha)*100% Confidence Interval
from scipy.stats import norm
quantil = norm.ppf(1-(alpha/2))

left = p_hat - quantil*se_prop
right = p_hat + quantil*se_prop

print("\nThe 90% Confidence Interval for the proportion of all consumers who prefer the company's brand is: [",round(left,3), ",",round(right,3), "]")

for gender in df2.Gender.unique():
    df_gender = df2[df2.Gender == gender]
    ng = len(df_gender)
    our_brand_gender = df_gender[df_gender.Preference == "Our brand"]
    p_hat_gender = len(our_brand_gender)/ng
    se_prop_gender = np.sqrt(p_hat_gender*(1-p_hat_gender)/ng)

    left_gender = p_hat_gender - quantil*se_prop_gender
    right_gender = p_hat_gender + quantil*se_prop_gender

    print("\nThe 90% Confidence Interval for the proportion of consumers with gender", gender, "who prefer the company's brand is: [",round(left_gender,3), ",",round(right_gender,3), "]")

for age in df2.Age.unique():
    df_age = df2[df2.Age == age]
    na = len(df_age)
    our_brand_age = df_age[df_age.Preference == "Our brand"]
    p_hat_age = len(our_brand_age)/na
    se_prop_age = np.sqrt(p_hat_age*(1-p_hat_age)/na)

    left_age = p_hat_age - quantil*se_prop_age
    right_age = p_hat_age + quantil*se_prop_age

    print("\nThe 90% Confidence Interval for the proportion of consumers aged", age, "who prefer the company's brand is: [",round(left_age,3), ",",round(right_age,3), "]")
    
print("\nComparing the CIs obtained, we can see that it looks like there is a higher proportion within the male comsumers that prefer the company's brand when compared to the same proportion within the female consumers.\nAdditionaly, we can see that the proportion of consumers aged less than 20 that prefer the Company's brand within this age group is higher than in any other age group. The age group whose proportion seems to prefer mostly the leading low-calorie competitor is consumers aged over 60.")