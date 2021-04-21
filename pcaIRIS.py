# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:04:57 2019

@author: Dr Vinod
"""
# Jesus is my saviour!!

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns


import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
%matplotlib inline


iris = pd.read_csv("C:/Users/Dr Vinod/Desktop/DataSets1/iris.csv")
iris = pd.DataFrame(iris)
iris.shape

ir = iris.drop(['Species'],1)

#convert it to numpy arrays
X=ir.values
#Scaling the values
X = scale(X)
pca = PCA(n_components=4)
pca.fit(X)
#The amount of variance that each PC explains
var= pca.explained_variance_ratio_
var
#Cumulative Variance explains
var1=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
var1

plt.plot(var1)

#Looking at above plot I'm taking 4 variables
pca = PCA(n_components=2)
pca.fit(X)
X1=pca.fit_transform(X)
print(X1) # 50by2 data
































