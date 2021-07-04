# AEMO-data-Analytics
AEMO-data-Analytics

1. Fetch the data from data sources.

Python-Pandas necessary-code-for-me

```python
# 1 import necessary libraries - Monir
import pandas as pd
import os
import glob
import numpy as np

# 2 assign dataset names - Monir
PUBLIC_DISPATCHSCADA_list_of_files = []

# all dataset names with starting PUBLIC_DISPATCHSCADA - Monir
PUBLIC_DISPATCHSCADA_list_of_files = glob.glob('PUBLIC_DISPATCHSCADA*.csv')

# create empty list
dataframes_list = []

list_of_names = PUBLIC_DISPATCHSCADA_list_of_files

# 3 append datasets into teh list - Monir
for i in range(len(list_of_names)):
    temp_df = pd.read_csv(list_of_names[i], skiprows = 1, skipfooter = 1)
    #dataframes_list[i]=temp_df
    dataframes_list.append(temp_df)
# 4
dataframes_list[2].tail()

# 5
PUBLIC_DISPATCHSCADA_df = pd.concat(dataframes_list)

#6
PUBLIC_DISPATCHSCADA_df.tail()

#7
PUBLIC_DISPATCHSCADA_df.shape

# 8
PUBLIC_DISPATCHSCADA_df.to_csv("PUBLIC_DISPATCHSCADA_all.csv") # Saving as csv file/ Monir 
```
