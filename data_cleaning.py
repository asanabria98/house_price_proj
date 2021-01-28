# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:16:13 2021

@author: alexs
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing

train = pd.read_csv('train.csv')

# Check for Na
train.isnull().sum().sort_values(ascending = False)/len(train) *100

#Check for columns with pool
len(train['PoolArea'][train['PoolArea'] != 0]) 

#Drop unimportante columns and columns with more than 50% of Na
train.drop(columns = ['Id','PoolQC','MiscFeature','LotFrontage'], inplace = True)


#Change column type

train['MSSubClass'] = train['MSSubClass'].astype('category')

train['MoSold'] = train['MoSold'].astype('category')

#Create Column for houses with pools. 1 has a pool 0 doesnt has a pool
train['pool'] = train['PoolArea'].apply(lambda x : 1 if x > 0  else 0 )

#Create Column for houses with Alley. 1 has alley access o doesnt has alley access
train['has_alley'] = train['Alley'].apply(lambda x : 1 if x == 'Grvl' or x == 'Pave' else 0)

#Create Column for houses with Fence


#Create Column for houses with FirePlace

#Solve for Na values