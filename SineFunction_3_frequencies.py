#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16, 4]
plt.rcParams.update({'font.size': 18})

# Create a simple signal with two frequencies
dt = 0.001
t = np.arange(0,0.3,dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t) + np.sin(2*np.pi*200*t)# Sum of 2 frequencies
f_clean = f
f = f + 2.5*np.random.randn(len(t))


# In[14]:


plt.plot(t, f_clean)


# In[ ]:




