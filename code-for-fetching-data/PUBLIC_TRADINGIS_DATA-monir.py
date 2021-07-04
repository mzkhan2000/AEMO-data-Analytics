#!/usr/bin/env python
# coding: utf-8

# In[36]:


# import necessary libraries - Monir
import pandas as pd
import os
import glob
import numpy as np
from csv import reader


# In[37]:


# assign dataset names - Monir
PUBLIC_TRADINGIS_list_of_files = []

#read all dataset names with starting PUBLIC_DISPATCHSCADA - Monir
PUBLIC_TRADINGIS_list_of_files = glob.glob('PUBLIC_TRADINGIS*.csv')


# In[38]:


len(PUBLIC_TRADINGIS_list_of_files)


# In[39]:


# create empty list
dataframes_list = []

list_of_names = PUBLIC_TRADINGIS_list_of_files


# In[40]:


# append datasets into teh list
for i in range(len(list_of_names)):
    # read csv file as a list of lists
    with open(list_of_names[i], 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        #print(list_of_rows)
        #temp_df = pd.DataFrame(list_of_rows)
        temp_df = pd.DataFrame(list_of_rows[9:14])
    dataframes_list.append(temp_df)
    list_of_column = list_of_rows[8]
    
    
    #temp_df = pd.read_csv(list_of_names[i], skiprows = 1, skipfooter = 1)
    #dataframes_list[i]=temp_df
    #dataframes_list.append(temp_df)
    


# In[42]:


len(dataframes_list)


# In[41]:


list_of_column


# In[43]:


dataframes_list[0].shape


# In[44]:


dataframes_list[1673].tail()


# In[45]:


# multiple DataFrames are be merged (Concatenate pandas objects) - Monir
PUBLIC_TRADINGIS_df = pd.concat(dataframes_list)


# In[46]:


PUBLIC_TRADINGIS_df.shape


# In[47]:


PUBLIC_TRADINGIS_df


# In[48]:


PUBLIC_TRADINGIS_df.columns = list_of_column


# In[49]:


PUBLIC_TRADINGIS_df.head()


# In[21]:


with open('PUBLIC_TRADINGIS_202104180030_0000000340056853.csv', 'r') as read_obj:
      # pass the file object to reader() to get the reader object
      csv_reader = reader(read_obj)
      # Pass reader object to list() to get a list of lists
      list_of_rows = list(csv_reader)
      #print(list_of_rows)
      #temp_df = pd.DataFrame(list_of_rows)
      test_df = pd.DataFrame(list_of_rows[8:14])
      #temp_df = pd.DataFrame(list_of_rows[8:14])
      


# In[22]:


test_df.head()


# In[30]:


PUBLIC_TRADINGIS_df.dtypes


# In[31]:


PUBLIC_TRADINGIS_df.info()


# In[50]:


PUBLIC_TRADINGIS_df


# In[51]:


# Export Pandas DataFrame to CSV - Monir
PUBLIC_TRADINGIS_df.to_csv('PUBLIC_TRADINGIS_df.csv', index=False)


# In[ ]:




