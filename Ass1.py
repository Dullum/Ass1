#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib as plt


# In[51]:


url = 'https://raw.githubusercontent.com/umaimehm/Intro_to_AI_2021/main/assignment1/Ruter_data.csv'


# In[33]:


df = pd.read_csv(url, sep=";")
df.head()


# In[36]:


df.describe()


# In[37]:


df.isna().sum()


# In[53]:


df["Kommune"].value_counts()


# In[68]:


df["Kommune"].value_counts()[:15].plot(kind='barh')
#15 meste brukte


# In[71]:


df["Område"].value_counts().plot(kind='barh')


# In[75]:


df["Kjøretøy_Kapasitet"].value_counts()


# In[76]:


df["Kjøretøy_Kapasitet"].plot.box()


# In[77]:


df["Kjøretøy_Kapasitet"].value_counts().plot(kind='barh')


# In[82]:


df["Passasjerer_Ombord"]


# In[94]:


df["Passasjerer_Ombord"].value_counts()


# In[107]:


#df["Passasjerer_Ombord"] = [(i>0)*i for i in df["Passasjerer_Ombord"]]
df["Passasjerer_Ombord"]=df["Passasjerer_Ombord"].clip(lower=0)
#remove negative numbers 


# In[108]:


df["Passasjerer_Ombord"].value_counts()


# In[112]:



df["Passasjerer_Ombord"].value_counts()[:20].plot(kind='barh')


# In[113]:


df["Linjetype"].value_counts().plot(kind='barh')


# In[ ]:




