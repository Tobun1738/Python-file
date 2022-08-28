#!/usr/bin/env python
# coding: utf-8

# In[11]:


def maximum( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return maximum( x, maximum( y, z ) )
print(max_of_three(20, 35, 19 ))


# In[13]:


def calculate(a,b):
    addition= a + b
    subtraction = a - b
    
    return(addition,subtraction)
calculate(40,10)


# In[25]:


def hyph(lists):
    n = lists.split("-")
    n.sort()
    result = "-".join(n)
    return print(result)
hyph("green-red-yellow-black-white")


# In[ ]:




