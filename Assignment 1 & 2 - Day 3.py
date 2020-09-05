#!/usr/bin/env python
# coding: utf-8

# In[1]:


altitude = 800

if altitude <= 1000:
    print("Land the plane")
elif 1000 > altitude < 5000:
    print("come down to 1000")
else:
    print("Trun around and try later")
    


# In[2]:


for i in range(1,200): 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 


# In[ ]:




