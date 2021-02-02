# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:16:13 2021

@author: alexs
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing

train = pd.read_csv('train.csv')

#Drop unimportante columns and columns with more than 50% of Na
train.drop(columns = ['Id','PoolQC','MiscFeature','LotFrontage'], inplace = True)


#Create Column for houses with pools. 1 has a pool 0 doesnt has a pool
train['pool'] = train['PoolArea'].apply(lambda x : 1 if x > 0  else 0 )

#Create Column for houses with Alley. 1 has alley access o doesnt has alley access
train['Has_Alley'] = train['Alley'].apply(lambda x : 1 if x == 'Grvl' or x == 'Pave' else 0)

#Dummy code Street column. 1 Pave 0 Grvl
train['Street'] = train['Street'].apply(lambda x : 1 if x == 'Pave' else 0)

#Create Column for houses with Fence
train['has_fence']  = train['Fence'].apply(lambda x : 1 if x in ['MnPrv', 'GdWo', 'GdPrv', 'MnWw'] else 0)

#Create Column for houses with FirePlace
train['Fireplaces'] = train['Fireplaces'].apply(lambda x: 1 if x != 0 else 0) 

#Replace value of OverQual
def map_quality(x):
    if x <= 10 and x >= 7:
        return 'good'
    elif x <= 6 and x >= 4:
        return 'average'
    else :
        return 'bad'

train['OverallQual'] = train['OverallQual'].apply(map_quality) 

#Replace value of Overall conditions of the house
def map_cond(x):
    if x <= 10 and x >= 7:
        return 'good'
    elif x <= 6 and x >= 4:
        return 'average'
    else :
        return 'bad'
train['OverallCond'] = train['OverallCond'].apply(map_cond)
# Drop columns 
train.drop(columns = ['PoolArea','Alley','Fence',], inplace = True)

#Choose max 15 columns of interest
include = ['MSZoning','LotArea','Street',
           'Has_Alley','BldgType','HouseStyle',
           'OverallQual','OverallCond', 
           'YearBuilt','HeatingQC','GrLivArea',
           'BedroomAbvGr','GarageCars','SaleCondition',
           'has_fence','pool','SalePrice']

train= train[include]

#convert type object to category
train = train.apply(lambda x : x.astype('category') if x.dtype == 'object' else x)


