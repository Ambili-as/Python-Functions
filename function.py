#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment - Python


# In[ ]:


#What does the len() function do in Python? 
#Write a code example using len() to find the length of a list.


# In[ ]:


# len() Function : The len() function in Python is used to get the number of items
# in a sequence or collection, like a string, list, tuple, or dictionary. 


# In[1]:


my_list = [12,15,54,87,69,86]
length = len(my_list)
print(length)


# In[ ]:


#. Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!".


# In[3]:


def greet(name):
    print("Hello", name,"!")


# In[5]:


greet("Ambili")


# In[ ]:


#Write a Python function find_maximum(numbers) that takes a list of integers 
#and returns the maximum value without using the built-in max() function. 
#Use a loop to iterate through the list and compare values. 


# In[6]:


def find_maximum(numbers):
    maximum = numbers[0]
    for n in numbers[1:]:
        if n> maximum:
            maximum = n
    return maximum


# In[7]:


numbers = [15,16,89,75,23,45,985]
print(find_maximum(numbers))


# In[ ]:


#Explain the difference between local and global variables in a Python function.
#Write a program where a global variable and a local variable have the same name 
#and show how Python differentiates between them. 


# In[8]:


x = 10  # Global variable 
 
def my_function(): 
    x = 5  # Local variable 
    print("Local :", x) 
 
my_function() 
print("Global:", x) 


# In[ ]:


#Create a function calculate_area(length, width=5) that calculates the area of a rectangle.
#If only the length is provided, the function should assume the width is 5. 
#Show how the function behaves when called with and without the width argument.


# In[17]:


def calculate_area(length,width=5):
    """Calculates the area of a rectangle.
        length:The length of the rectangle.
        width:The width of the rectangle."""
    return length * width
#with and without arguments
Area1 = calculate_area(8,6) #Calling with both length and width
print("Area with length=8 and width=6:", Area1)
Area2 = calculate_area(8) #Calling with only length 
print("Area with length=8 and width=default value(5):", Area2)


# In[11]:




