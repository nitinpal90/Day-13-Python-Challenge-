#!/usr/bin/env python
# coding: utf-8

# # Day-13 Python Challenge

# # NumPy Part - 2

# # Slicing in NumPy Array

# In[4]:


import numpy as np


# In[6]:


a = np.array([1,2,3,4,5,6,7])

print(a[1:6])


# In[7]:


a = np.array([1,2,3,4,5,6,7])

print(a[::2])


# # Slicing in 2d Array

# In[8]:


import numpy as np

a = np.array([[10,20,30,40,50],[60,70,80,90,100]])

print(a[1,0:3])


# # Check the data types of an array

# In[10]:


a = np.array([1,2,3,4,5])
print(a.dtype)


# In[11]:


a = np.array(["Day"])
print(a.dtype)


# # Creating array with a define data type

# In[12]:


a = np.array([1,2,3,4,5],  dtype = 'S')
print(a)
print(a.dtype)


# # Creating an array with data types 4 bytes integer

# In[13]:


a = np.array([1,2,3,4,5],  dtype = 'i4')
print(a)
print(a.dtype)


# # NumPy Array Shape

# The shape of an array is the number of element in each dimension.

# # Print the shape of 2d array

# In[15]:


a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a.shape)


# # Print the shape of 3d array

# In[16]:


a = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(a.shape)


# # Joining Array NumPy Arrays

# In[18]:


a = ([1,2,3])

b = ([4,5,6])

arr = np.concatenate((a,b))

print(arr)


# # Joining 2d Arrays in NumPy

# In[21]:


a = ([[1,2,3], [4,5,6]])

b = ([[7,8,9], [10,11,12]])

arr = np.concatenate((a,b), axis = 1)

print(arr)


# In[22]:


a = ([[1,2,3], [4,5,6]])

b = ([[7,8,9], [10,11,12]])

arr = np.concatenate((a,b), axis = 0)

print(arr)


# # Splitting NumPy Array

# # Splitting the arrays in 3 parts

# In[28]:


a = np.array([1,2,3,4,5,6])
b = np.array_split(a,2)
print(b)


# # Splitting the arrays in 2 parts

# In[29]:


a = np.array([1,2,3,4,5,6])
b = np.array_split(a,3)
print(b)


# # Ravel and Flatten Function 

# # Convert Multi-Dimension Array in 1d Arrays

# In[34]:


a = np.array([[[1,2,],[3,4],[5,6]]])

print(a)

print("Dimension Is:", a.ndim)

b = a.ravel() ## Ravel function is use to change 3d array to 1d array

print(b)

print("Now the new dimension is:",b.ndim)


# In[35]:


a = np.array([[[1,2,],[3,4],[5,6]]])

print(a)

print("Dimension Is:", a.ndim)

b = a.flatten() ## Flatten function is use to change 3d array to 1d array

print(b)

print("Now the new dimension is:",b.ndim)


# # Unique Function

# In[38]:


a = np.array([1,1,2,3,3,4,4,5,6,6,66,7,7,10])

print(a)

b = np.unique(a)

print(b)


# # Delete Function

# In[40]:


a = np.array([1,2,3,4,5])

b = np.delete(a,[0])

print(b)

