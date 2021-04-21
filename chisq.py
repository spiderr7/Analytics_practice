# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 16:08:19 2020

@author: Dr Vinod
"""
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns

df = pd.DataFrame({'Gender' : ['M', 'M', 'M', 'F', 'F'] * 10,
                   'isSmoker' : ['Smoker', 'Smoker', 'Non-Smpoker', 'Non-Smpoker', 'Smoker'] * 10
                  })
df.head()

contigency= pd.crosstab(df['Gender'], df['isSmoker']) 
contigency

# F, Non-Smoker, 20*20/50
400/50 # 8
# F, Smoker, 20*30/50
600/50 # 12
# M, Non-Smoker, 30*20/50
30*20/50 #12
# M, Smoker, 30*30/50
30*30/50 #18

contigency_pct = pd.crosstab(df['Gender'], df['isSmoker'], normalize='index')
contigency_pct # obsrvd cells in percentages 
contigency_all = pd.crosstab(df['Gender'], df['isSmoker'], normalize='all')
contigency_all # percent from Grand Total

plt.figure(figsize=(12,8)) 
sns.heatmap(contigency, annot=True, cmap="YlGnBu")

#_______________WITHOUT continuity correction
chi2, p, dof, ex = chi2_contingency(obs, correction=False)

chi2, p, dof, ex = chi2_contingency(contigency, correction=False)

print(chi2)
print(p)
print(ex)