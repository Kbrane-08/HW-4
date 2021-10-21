#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib.inline', '')
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


def bisection_method(f,a,b,tol,show iteration=False)
if f(a)*f(b)>=0
print("invalid interval")
else:
    est root=[a,b]
    count=0
    while ture
    c=(a+b)/2
    est_roots.append(c)
    if abs(f(c))<=tol:
        break
     if f(a)*f(b)<0  
     b=c
    else 
    a=c
    count+=1
    print(f"Number of Iterations Perform: {count}")
    print(f"the root ｛c｝")
    return est_roots
    else
    print(f"the root ｛c｝")
 #part 1
 f=lambda x=1.01*x*x-3.04*x+2.07


# In[4]:


print("Root 1")
bisection_method(f,0.5,1.5,10**-6,ture)
print("Root 2")
bisection_method(f,0.5,1.5,10**-6,ture)


# In[5]:


print("Root 1")
roots1=bisection_method(f,0.5,1.5,10**-6,ture)
print("Root 2")
roots2=bisection_method(f,0.5,1.5,10**-6,ture)


# In[16]:


x=np.linspace(0.3,1000)
plt.plot[[0.3],[0,0],'k'] #plot the horizontal line y=0
ply.plot(x.f(x))   #plot the function
plt.plot(roots1,np.zeros(len(roots1)),"or")  #plot root
plt.plot(roots2,np.zeros(len(roots2)),"og")  #plot root
plt.xlim(0,3)
plt.ylim(-0.5,2.1)
plt.show()


# In[ ]:




