"""
In-Class Exercises Week 6

@author: Francisco Perestrello, 39001
"""

# Exercise 1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('peakpower.xlsx')

# a)
print('\na)')
corr = df['Daily High Temperature'].corr(df['Peak Load'])

plt.figure(1)
plt.plot(df['Daily High Temperature'],df['Peak Load'],'ro')
plt.title('Scatterplot')
plt.xlabel('Daily High Temperature')
plt.ylabel('Peak Load')

print(f'\nLooking at the scatterplot, we can see that our data seems to show an exponential relationship. Additionaly, the correlation between the Daily High Temperature and Peak Power Load is {corr:.4f}.')


# b)
print('\nb)')
print('\nThe relationship between Daily High Temperature and Peak Power Load seems to follow an exponential model. However, to better understand which model fits our data the best, we will compute all three models and compare the R-squared of the three.')

def rsquared(observed, error):
    errorSQ = error**2
    average = observed.sum()/len(observed)
    return 1 - errorSQ.sum()/((observed - average)**2).sum()

# Linear Model: Y = aX + b
LM = np.polyfit(df['Daily High Temperature'],df['Peak Load'],1)
a_LM = LM[0]
b_LM = LM[1]

EstimatedLM = np.multiply(df['Daily High Temperature'],a_LM) + b_LM
ErrorLM = df['Peak Load'] - EstimatedLM

RsquaredLM = rsquared(np.array(df['Peak Load']), ErrorLM)

plt.figure(2)
plt.plot(df['Daily High Temperature'],df['Peak Load'],'ro')
plt.plot(df['Daily High Temperature'],EstimatedLM,'b-')
plt.title('Linear Model')
plt.xlabel('Daily High Temperature')
plt.ylabel('Peak Power Load')
plt.text(20, 180, f'Y = aX + b with a = {a_LM:.2f} and b = {b_LM:.2f}\nR2 = {RsquaredLM:.4f}')


# Exponential Model: Y = a*b^X <=> ln(Y) = ln(a) + ln(b) X <=> ln(Y) = ln(b) X + ln(a)
# A = ln(a) <=> a = e^A   and B = ln(b) <=> b = e^B
EM = np.polyfit(df['Daily High Temperature'], np.log(df['Peak Load']), 1)
a_EM = np.exp(EM[1])
b_EM = np.exp(EM[0])

EstimatedEM = np.multiply(a_EM, np.power(b_EM,df['Daily High Temperature']))
ErrorEM = df['Peak Load'] - EstimatedEM

RsquaredEM = rsquared(np.array(df['Peak Load']), ErrorEM)

plt.figure(3)
plt.plot(df['Daily High Temperature'],df['Peak Load'],'ro')
plt.plot(df['Daily High Temperature'],EstimatedEM,'g-')
plt.title('Exponential Model')
plt.xlabel('Daily High Temperature')
plt.ylabel('Peak Power Load')
plt.text(20, 180, f'Y = a*b^X with a = {a_EM:.2f} and b = {b_EM:.2f}\nR2 = {RsquaredEM:.4f}')


# Multiplicative Model: Y = a*X^b <=> ln(Y) = ln(a) + b ln(X) <=> ln(Y) = b ln(X) + ln(a)
# A = ln(a) <=> a = e^A   and B = b
MM = np.polyfit(np.log(df['Daily High Temperature']), np.log(df['Peak Load']), 1)
a_MM = np.exp(MM[1])
b_MM = MM[0]

EstimatedMM = np.multiply(a_MM, np.power(df['Daily High Temperature'],b_MM))
ErrorMM = df['Peak Load'] - EstimatedMM

RsquaredMM = rsquared(np.array(df['Peak Load']), ErrorMM)

plt.figure(4)
plt.plot(df['Daily High Temperature'],df['Peak Load'],'ro')
plt.plot(df['Daily High Temperature'],EstimatedMM,'k-')
plt.title('Multiplicative Model')
plt.xlabel('Daily High Temperature')
plt.ylabel('Peak Power Load')
plt.text(20, 180, f'Y = a*X^b with a = {a_MM:.2f} and b = {b_MM:.2f}\nR2 = {RsquaredMM:.4f}')


# Quadratic Model: Y = a*X^2 + bX + c
QM = np.polyfit(df['Daily High Temperature'],df['Peak Load'], 2)
a_QM = QM[0]
b_QM = QM[1]
c_QM = QM[2]

EstimatedQM = np.multiply(df['Daily High Temperature']**2,a_QM) + np.multiply(df['Daily High Temperature'],b_QM) + c_QM
ErrorQM = df['Peak Load'] - EstimatedQM

RsquaredQM = rsquared(np.array(df['Peak Load']), ErrorQM)

plt.figure(5)
plt.plot(df['Daily High Temperature'],df['Peak Load'],'ro')
plt.plot(df['Daily High Temperature'],EstimatedQM,'c-')
plt.title('Quadratic Model')
plt.xlabel('Daily High Temperature')
plt.ylabel('Peak Power Load')
plt.text(20, 178, f'Y = a*X^2 + bX + c with a = {a_QM:.2f}, b = {b_QM:.2f},\nc = {c_QM:.2f} and R2 = {RsquaredQM:.4f}')

print(f'\nLinear Model R2: {RsquaredLM:.4f}\nExponential Model R2: {RsquaredEM:.4f}\nMultiplicative Model R2: {RsquaredMM:.4f}\nQuadratic Model R2: {RsquaredQM:.4f}')

print(f'\nBy comparing the four R-squared, we can see that the quadratic model seems to fit best, showing the highest R-squared, with a value of R2 = {RsquaredQM:.4f}.')
print(f'\nThus, the appropriate regression equation to predict the peak power load for EDP is Y = a*b^X with a = {a_EM:.2f} and b = {b_EM:.2f}')

# c)
print('\nc)\n')
def prediction(x):
    prediction = np.multiply(a_EM, np.power(b_EM,x))
    print(f'On a summer day with high temperature of {x:.0f} degrees, our model predicts that the peak power load will be {prediction:.2f}.')
    
prediction(38)