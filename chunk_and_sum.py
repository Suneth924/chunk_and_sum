#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Specify the full path to your CSV file on local disk D


# In[3]:


file_path = r"D:\AGCT.csv"


# In[4]:


# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)


# In[5]:


df.head(5)


# In[6]:


# Define the starting value for chunking
start_value = 114497906


# In[7]:


# Define the chunk size
chunk_size = 60


# In[8]:


# Initialize an empty list to store the summation of 1s for each chunk
summations = []


# In[9]:


# Iterate over chunks
while start_value <= df['AGCT'].max():
    end_value = start_value + chunk_size - 1
    chunk = df[(df['AGCT'] >= start_value) & (df['AGCT'] <= end_value)]
    if len(chunk) > 0:
        summation = chunk['N'].sum()
        summations.append((start_value, end_value, summation))
    else:
        summations.append((start_value, end_value, 0))  # Append 0 if no rows meet the condition
    start_value += chunk_size

# Print the starting and ending numbers of WRCY and the summation of 1s for each chunk
for i, (start_value, end_value, summation) in enumerate(summations):
    print(f"Chunk {i+1}: Start value = {start_value}, End value = {end_value}, Sum of 1s = {summation}")


# In[10]:


# Create a separate DataFrame with 'Start_WRC', 'End_WRC', and 'Sum_of_1s' columns
result_df = pd.DataFrame(summations, columns=['start_value_AGCT', 'end_value_AGCT', 'Sum_of_1s'])


# In[11]:


# Print the separate DataFrame
print(result_df)


# In[12]:


# Write the separate DataFrame to a new CSV file on the D drive
file_path_new = r"D:\separate_result_AGCT.csv"
result_df.to_csv(file_path_new, index=False)


# In[ ]:




