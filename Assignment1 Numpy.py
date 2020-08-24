#!/usr/bin/env python
# coding: utf-8

# # Assignment

# Import numpy as np

# In[3]:


import numpy as np
a=[1,2,3,4,5]
a_np=np.array(a)
a_np


# Make a python list => \[1,2,3,4,5\]
# 
# Convert it into numpy array and print it

# In[4]:


a_np


# Make a python matrix (3 x 3) => \[[1,2,3],[4,5,6],[7,8,9]\]
# 
# Convert it into numpy array and print it

# In[5]:


matrix1=[[1,2,3],[4,5,6],[7,8,9]]
np.array(matrix1)


# Make a matrix (3 x 3) using built-in methods (like arange(), reshape() etc.):
# 
# \[ [1,3,5],
# 
#  [7,9,11],
#  
#  [13,15,17] \]

# In[31]:


arr=np.arange(1,18,2)
arr.reshape(3,3)


# Create a numpy array with 10 random numbers from 0 to 10 (there should be few numbers greater than 1)

# In[34]:


ranarr=np.random.randint(0,10,10)
ranarr


# Create numpy array => \[1,2,3,4,5\] and convert it to 2D array with 5 rows

# In[41]:


b=[1,2,3,4,5]
b1=np.array(b)
b1.reshape(1,5)


# Print the shape of the above created array

# In[43]:


b1.reshape(5)


# Create a numpy array with 10 elements in it. Access and print its 3rd, 4th and 9th element.

# In[51]:


arr1=np.array([1,2,3,4,5,6,7,8,9,10])
arr1[2]


# In[53]:


arr1[3]


# In[54]:


arr1[8]


# Print alternate elements of that array

# In[55]:


arr1[0:9:2]


# Change last 3 elements into 100 using broadcasting and print

# In[67]:


arr1[7:]=[100,100,100]
arr1


# Create a 5 x 5 matrix (fill it with any element you like), print it.
# 
# Then print the middle (3 x 3) matrix.

# In[71]:


arr5=np.arange(1,26).reshape(5,5)
arr5


# In[72]:


arr5[0:3,1:4]

