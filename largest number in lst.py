#!/usr/bin/env python
# coding: utf-8

# In[21]:


lst=[]


# In[22]:


n=int(input('Enter the number of elements'))


# In[23]:


print(n)


# In[24]:


for i in range(0,n):
    element=int(input())
                
    lst.append(element)
    


# In[25]:


print(lst)


# In[31]:


max_num=0
for num in lst:
    if num > max:
        max = num
        
print('Largest number is:' ,max)


# In[ ]:




