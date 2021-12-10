#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("Enter the number of element"))


# In[2]:


lst=[]
print("Enter the Element one by one")
for i in range(0,n):
    elt=int(input())
    lst.append(elt)


# In[3]:


count=0


# In[4]:


search=int(input("Enter the Search Element"))


# In[6]:


for num in lst:
    if num==search:
        count=1
        
        
if count==1:
    print("Element Found")
else:
    print("Element Not Found")


# In[ ]:




