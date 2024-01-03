#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("C:\\Users\\LENOVO\\Downloads\\INFY.csv")


# In[4]:


data


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.head()


# In[8]:


data.tail()


# In[9]:


data.dropna()


# In[10]:


data.dropna(inplace = True)


# In[11]:


data.fillna(1, inplace = True)


# In[12]:


print(data.duplicated())


# In[13]:


data.drop_duplicates(inplace = True)


# In[14]:


data.plot()
plt.show()


# In[15]:


data.plot(kind = "scatter", x = "Open", y = "High")


# In[16]:


data["Low"].plot(kind = "hist")


# In[17]:


# Convert 'Date' column to datetime type
data['Date'] = pd.to_datetime(data['Date'])


# In[18]:


# Set 'Date' as the index
data.set_index('Date', inplace=True)


# In[19]:


# Line plot of Revenue and Expenses over time
data.plot(kind='line', marker='o')
plt.title('Stock Price')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.grid(True)
plt.show()


# In[20]:


plt.figure(figsize=(12, 6))
data['Close'].plot(marker='o')
plt.title('Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.show()



# In[30]:


# Pie chart of Volume distribution by date
sample_data = data.sample(10)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
plt.pie(sample_data["High"],  colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Distribution of High Value")
plt.show()


# In[ ]:





# In[ ]:




