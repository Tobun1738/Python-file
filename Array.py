#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np 
def np_list(array_num):
    num_list = np.tolist()
    print(num_list)
  

array_num = array('i', [1,3,6]) 
array_list(array_num)



#question1


# In[16]:


import numpy as np
array = np.array([[55, 25, 15],
                  [30, 44, 2],
                  [11, 45, 77]])
  

print("Numpy Matrix is:")
print(array)
  
trace = np.trace(array)
  
  
print("\nTrace of given 3X3 matrix:")
print(trace)



#question2


# In[32]:


import numpy as np
x = np.array([[1,2],[3,5]])
print(x)
print("Values bigger than 2 =", x[x>2])



#question3


# In[34]:


import numpy as np
a = [[1,2],[3,5]]
b = [[1,2],[3,5]]
c=np.add(a, b)
print(c)




#question4


# In[35]:


import numpy as np
a = np.random.rand(6, 10)
print(a)
b = a - a.mean(axis=1, keepdims=True)
print(b)





#question5


# In[ ]:




