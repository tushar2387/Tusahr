#!/usr/bin/env python
# coding: utf-8

# In[206]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')
##Standard formate#
get_ipython().run_line_magic('matplotlib', 'inline')


# In[207]:


df = pd.read_csv('DistrictWiseReport20200418.csv', header= 0,encoding= 'unicode_escape')


# In[208]:


#Remove first SR no columns name
df.drop('Sr No', axis=1, inplace=True)


# In[209]:


df.head()


# In[210]:


df.shape


# In[211]:


df.describe()


# In[212]:


df.info()


# In[221]:


print('Gujarat Region Top 5 District Highest Positive Cases')
df.sort_values(by='Confirmed Positive Cases',ascending=False).head()


# In[214]:


df_new = df.dropna()
df.isnull().sum().sort_values(ascending=False)


# In[215]:


fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size


# In[216]:


df.plot()


# In[217]:


df.hist(bins=10, color='steelblue', edgecolor='black', linewidth=1.0,
           xlabelsize=8, ylabelsize=8, grid=False)    
plt.tight_layout(rect=(0, 0, 1.2, 1.2))


# In[218]:


# Correlation Matrix Heatmap
f, ax = plt.subplots(figsize=(10, 6))
corr = df.corr()
hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f',
                 linewidths=.05)
f.subplots_adjust(top=0.93)
t= f.suptitle('Covid-19', fontsize=14)


# In[ ]:




