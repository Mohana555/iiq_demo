#!/usr/bin/env python
# coding: utf-8

# In[3]:


num1=int(input('Enter the number'))
num2=int(input('Enter the number'))


# In[7]:


def add(num1,num2):
    if num1==0 or num2==0:
        return 'Input must not be zero'
    else:
        print(num1+num2)
        
add(num1,num2)
        

