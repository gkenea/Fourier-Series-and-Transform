#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [8, 8]
plt.rcParams.update({'font.size': 18})

n = 256
w = np.exp(-1j * 2 * np.pi / n)


# In[2]:


DFT = np.zeros((n,n))

# Slow
for i in range(n):
    for k in range(n):
        DFT[i,k] = w**(i*k)
        
DFT = np.real(DFT)
        
plt.imshow(DFT)
plt.show()


# In[10]:


# Fast
J,K = np.meshgrid(np.arange(n),np.arange(n))
DFT = np.power(w,J*K)
DFT = np.real(DFT)
       
plt.imshow(DFT)
plt.show()


# In[ ]:




