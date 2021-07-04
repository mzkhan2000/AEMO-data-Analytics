#!/usr/bin/env python
# coding: utf-8

# In[16]:


# import necessary libraries - Monir
import pandas as pd
import os
import glob
import numpy as np


# In[18]:


# assign dataset names - Monir
PUBLIC_DISPATCHSCADA_list_of_files = []

#read all dataset names with starting PUBLIC_DISPATCHSCADA - Monir
PUBLIC_DISPATCHSCADA_list_of_files = glob.glob('PUBLIC_DISPATCHSCADA*.csv')


# In[19]:


# create empty list
dataframes_list = []

list_of_names = PUBLIC_DISPATCHSCADA_list_of_files


# In[20]:


# append datasets into teh list
for i in range(len(list_of_names)):
    temp_df = pd.read_csv(list_of_names[i], skiprows = 1, skipfooter = 1)
    #dataframes_list[i]=temp_df
    dataframes_list.append(temp_df)


# In[23]:


dataframes_list[0].head()


# In[24]:


dataframes_list[0].tail()


# In[25]:


dataframes_list[0].shape


# In[27]:


len(dataframes_list)


# In[28]:


dataframes_list[8890].tail()


# In[29]:


# multiple DataFrames are be merged (Concatenate pandas objects) - Monir
PUBLIC_DISPATCHSCADA_df = pd.concat(dataframes_list)


# In[30]:


PUBLIC_DISPATCHSCADA_df.shape


# In[31]:


# set a specific column of DataFrame as index - Monir
PUBLIC_DISPATCHSCADA_df.set_index('DUID')


# In[32]:


PUBLIC_DISPATCHSCADA_df.dtypes


# In[33]:


PUBLIC_DISPATCHSCADA_df.info()


# In[34]:


# Export Pandas DataFrame to CSV - Monir
PUBLIC_DISPATCHSCADA_df.to_csv('PUBLIC_DISPATCHSCADA_df.csv', index=False)


# In[ ]:




