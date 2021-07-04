# AEMO-data-Analytics
AEMO-data-Analytics

# 1. Fetch the data from PUBLIC_DISPATCHSCADA data.

**For PUBLIC_DISPATCHSCADA data 8,891 files are extracted in a single folder** 

Python-Pandas necessary code for fetching the data from PUBLIC_DISPATCHSCADA data

```python
# import necessary libraries - Monir
import pandas as pd
import os
import glob
import numpy as np

# assign dataset names - Monir
PUBLIC_DISPATCHSCADA_list_of_files = []

# all dataset names with starting PUBLIC_DISPATCHSCADA - Monir
PUBLIC_DISPATCHSCADA_list_of_files = glob.glob('PUBLIC_DISPATCHSCADA*.csv')

# create empty list
dataframes_list = []

list_of_names = PUBLIC_DISPATCHSCADA_list_of_files

# append datasets into teh list - Monir
for i in range(len(list_of_names)):
    temp_df = pd.read_csv(list_of_names[i], skiprows = 1, skipfooter = 1)
    #dataframes_list[i]=temp_df
    dataframes_list.append(temp_df)

# multiple DataFrames are be merged (Concatenate pandas objects) - Monir
PUBLIC_DISPATCHSCADA_df = pd.concat(dataframes_list)

# set a specific column of DataFrame as index - Monir
PUBLIC_DISPATCHSCADA_df.set_index('DUID')

# Export Pandas DataFrame to CSV - Monir
PUBLIC_DISPATCHSCADA_df.to_csv('PUBLIC_DISPATCHSCADA_df.csv', index=False)
```
**PUBLIC_DISPATCHSCADA_df contains 3,326,960 rows × 6 columns**

# 2. Fetch the data from PUBLIC_TRADINGIS data.

**Similarly For PUBLIC_TRADINGIS data 1,674 files are extracted in a single folder** 
