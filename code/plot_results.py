# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:58:15 2016

@author: adityanagarajan
Note: This code plots the results of training and validation error from the 
output csv files
"""

from matplotlib import pyplot as plt
import numpy as np

file_list = ['exp_1000_10_gpu2.csv','exp_1000_20_gpu2.csv','exp_1000_30_gpu2.csv','exp_1000_40_gpu2.csv']
line_color = ['r','g','b','k']
model = ['10 points','20 points','30 points','40 points']

for f,c,m in zip(file_list,line_color,model):
    results_array = np.loadtxt('output/' + f,dtype = 'S',delimiter = ',',skiprows = 1)
    results_array = results_array[:-1].astype('float')
    
    plt.plot(results_array[:,0],results_array[:,1],c + '--',label = m + ' training mean squared error')
    
    plt.plot(results_array[:,0],results_array[:,2],c, label = m + ' validation mean squared error')
    

plt.xlabel('epochs')
plt.ylabel('Mean Squared Error')
plt.title('2 convolution layers and 1 fully connected layer')
plt.legend()

plt.grid()
plt.show()


