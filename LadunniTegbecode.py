#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
food_data = pd.read_csv(r"C:\Users\HP\Desktop\FoodBalanceSheets_E_Africa_NOFLAG.csv")
food_data


# In[26]:


item = food_data.groupby('Item')
item.sum()


# In[16]:


food_data.describe()


# In[12]:


food_data.isnull()


# In[13]:


food_data.isnull().count()


# In[14]:


food_data.isnull().sum()


# In[50]:


food_data['percent'] = (food_data['Y2016'].isnull().sum()/food_data['Y2016'].count())*100
food_data['percent']


# In[51]:


food_data.corr()


# In[34]:


imprt = food_data.groupby('Element')
imprt.sum()


# In[80]:


food_data.groupby('Element')['Y2018','Element'].sum()


# In[94]:


country = food_data.groupby('Area')

country.sum('Element',"Import Quantity")


# In[77]:


country = food_data.groupby('Area')

country.describe()


# In[ ]:




