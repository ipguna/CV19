#!/usr/bin/env python

##################################################################
#
# Simple simulation on of COVID-19 cases in Indonesia
#
# Written by: Irwan Prasetya Gunawan
# Data source: http://kcov.id/daftarpositif
#
# Original data from the website was downloaded in csv format 
# CSV filename: daily.csv
# Data was read in from the csv file
#
# Mathematical model was taken from http://eprints.itb.ac.id/119/
# [1] Nuraini, Nuning and Khairudin, Kamal and Apri, Mochamad 
#     Data dan Simulasi COVID-19 dipandang dari Pendekatan Model Matematika. 
#     Preprint. (Submitted)
#

import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

##################################################################
#
# Read data from file, convert the name columns
#

df = pd.read_csv('daily.csv',
		header=0, 
		names=['Date','New','Imported','Local','Accumulated','Treatment','Recovered','Rec (Acc)', 'Death', 'Death (Acc)', 'Death (rate)', 'Checked', 'Positif', 'Negatif', 'Process', 'Test (+)', 'Test (percent)', 'Test (daily)', 'Notes' ],
		parse_dates=['Date'])

# print(df)	# check the parsed data by printing it out

# Copied the original data from file into dataframe matrix with several columns
mtx = df[['Date', 'New', 'Accumulated', 'Recovered', 'Rec (Acc)', 'Death (Acc)']]

# Drop NaN from data
mtx = mtx.dropna()

# date
dateid = mtx['Date']

# variable - new case
newcase = mtx['New']

# variable - accumulated number 
accumulated = mtx['Accumulated']

# variable - accumulated number of death cases
death_acc = mtx['Death (Acc)']

# variable - accumulated number of recovered cases
recovered_acc = mtx['Rec (Acc)']

##################################################################
#
# Mathematical model
#

# Parameters for the model based on the paper
# KOREAN
K = 8495
r = 0.2
alpha = 0.410
t_m = 40.12
modelname = 'Korean'

# Parameters for the model, based on modified
#K = 12950
alpha = 1.076541410
#alpha = 0.91410
#alpha = 1
modelname = 'Modified'

# Total number of extra days for prediction
extra_days = 3

# Create an empty array to store the calculation results 
y = []
y_acc = []

# Loop for calculation
for t in range(len(dateid)+extra_days) : 
	exponent = -r * (t - t_m)
	output = K / pow(( 1 + alpha * m.exp(exponent)),1/alpha)
	y.append(output)

# Calculate the accumulated value
for t in range(1,len(dateid)+extra_days) :
	cumsum = y[t] + y[t-1]
	y_acc.append(cumsum)


##################################################################
#
# Analysis: RMSE between actual data and mathematical model
#

error_acc = y_acc[:len(dateid)] - accumulated		# error calculation
ssq = np.sum(error_acc ** 2)						# sum of square error
mean = np.mean(ssq)									# mean of sum square error (MSE)
RMSE = np.sqrt(mean)								# square root of MSE

# Display/output the results of the analysis
print("K = %2d\t r = %2.4f \t alpha = %2.5f \t t_m = %2.4f \t RMSE = %3.6f " % (K, r, alpha, t_m, RMSE))

# Save output to csv file


##################################################################
#
# Plotting data
#

# Plot the data

# Bar chart for plotting daily new case.
# First, create index replaces date index from the original data for plotting purposes
idx = list(range(len(dateid))) 
bar_width = 0.35
opacity = 0.8
plt.bar(idx, #dateid, 
	newcase, bar_width,
	alpha=opacity,
	color='b',
	label='Daily new case')
# plt.plot(newcase, color='g', label='Daily new case') # New case plot as line

# Other data plot as line graph
plt.plot(accumulated, color='blue', label='Acc. case')
plt.plot(death_acc, color='red', label='Acc. death')
plt.plot(recovered_acc, color='g', label='Acc. recovery')
plt.plot(y, color='orange', label='Model')
plt.plot(y_acc, color='black', label='Model (Acc)')
plt.xlabel('Days')
plt.ylabel('Population')
plt.tick_params(axis='x', rotation=70)
plt.title('nCOVID-19 cases in Indonesia')
plt.legend()

# Save figure to file
basename = 'cv19caseID_'
filetype = '.png'
filename = basename + modelname + filetype
# plt.savefig('cv19caseID.png', bbox_inches='tight')
plt.savefig(filename, bbox_inches='tight')

# Show figure on the terminal
plt.show()


