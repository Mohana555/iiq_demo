#!/usr/bin/env python
# coding: utf-8

# # Binary Search

# In[1]:


n=int(input("Enter the number of element"))


# In[2]:


lst=[]
print("Enter the Element one by one")
for i in range(0,n):
    elt=int(input())
    lst.append(elt)


# In[7]:


low=0
high=n
search=int(input("Enter the Search Element"))


# In[8]:


def BinSearch(low,high):
    if(low<=high):
        middle=(low+high)//2
        if search==lst[middle]:
            print("Element Found")
            return middle
        elif search<lst[middle]:
            high=middle-1
            BinSearch(low,high) 
        elif search>lst[middle]:
            low=middle+1
            BinSearch(low,high)
    else:
        print("Element Not Found")
        

BinSearch(0,n)


# In[ ]:





# In[ ]:




