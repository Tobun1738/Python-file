#!/usr/bin/env python
# coding: utf-8

# In[ ]:


question 1


# In[10]:


def test(first,last):
    full_name = first+" "+last
    reversed_full_name = full_name[::-1]
    return(reversed_full_name)
test("Tobun","quadri")


# In[ ]:


question 2


# In[12]:


def add(n):
    #n= input("input a number")
    result= int(n) + int(n+n) + int(n+n+n)
    return(result)
add('5')


# In[ ]:


question 3


# In[20]:


def evenOrOdd():
    num=int(input("Enter a number: "))
    if num % 2 == 0:
        print("the number () is even", format(num))
    else:
        print("the number () is odd", format(num))
evenOrOdd()        


# In[ ]:


Question 4


# In[16]:


num = []
for i in range(2000,3201):
    if i % 7 == 0:
        if i % 5 != 0:
            num.append(i)
print(num)


# In[ ]:


question 5


# In[23]:


def factoral(n):
    n= input("enter a number")
    result= 8*7*6*5*4*3*2*1
    return(result)
factoral(8)


# In[ ]:


question 6


# In[ ]:


str1= input("enter a string")

