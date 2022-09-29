#!/usr/bin/env python
# coding: utf-8

# ### Homework #2

# 1. Round 4.5667 to the nearest hundreth (2 decimals) using a build-in function, round().

# In[1]:


round(4.5667, 2)


# 2. Convert "657" to an integer data type

# In[ ]:


int("657")


# 3. Write a program to get two numbers from a user. Then, create a 6-digit code that is a series of randomly generated numbers between the two numbers given by the user. Print the 6-digit code so all digits are separated by a dash. 

# In[1]:


import random as rand

num1 = int(input("choose a number: "))
num2 = int(input("choose a number:" ))

code1 = rand.randint(num1, num2)
code2 = rand.randint(num1, num2)
code3 = rand.randint(num1, num2)
code4 = rand.randint(num1, num2)
code5 = rand.randint(num1, num2)
code6 = rand.randint(num1, num2)

print(f"The code is {code1}-{code2}-{code3}-{code4}-{code5}-{code6}")


# 4. Write a program to remove ALL the white spaces from the following text:
# 
#         Hickory, dickory, dock,     
#         The mouse ran up the clock.   
#         The clock struck one,   
#         The mouse ran down,                      
#         Hickory, dickory, dock                  

# In[ ]:


line1 =  "Hickory, dickory, dock,    "
line2 =  "The mouse ran up the clock. "
line3 =  "The clock struck one, " 
line4 =  "The mouse ran down, "
line5 =  "Hickory, dickory, dock "


# In[ ]:


line1 = line1.strip(".")
line2 = line2.strip(".")
line3 = line3.strip(".")
line4 = line4.strip(".")
line5 = line5.strip(".")


# In[ ]:





# 5. Write a function to calculate the miles per gallon. Get a miles driven and gallons used from a user and call your function to calculate the miles per gallon.

# In[5]:


def miles_per_gallon(miles, gallons):
    mpg = miles/gallons
    mpg = round(mpg, 2)
    return mpg


# In[6]:


miles_driven = float(input('Enter number of miles driven: '))
gallons_used = float(input("enter gallons used: ")) 

mpg = miles_per_gallon(miles_driven, gallons_used)
print(f"you got {mpg} to the gallon")


# 6. Enhance the <b>compute()</b> function created during Module 2. Enhance the function to compute a circle's area and circumference where:
# 
#  - circle's area = 3.14 X (radius X radius)   
#  - circle's circumference = 3.14 X diameter

# In[ ]:





# In[ ]:





# 7. Write a function called multiply_two() that accepts two parameters. The function should print a message like '15 * 2 = 30'.  Randomly generate two numbers between 1 and 100, then call the function with the two random numbers.

# In[11]:


import random as rand

def multiply_two(param1, param2):
    print(f"{param1} * {param2} = {param1 * param2}")
          
multiply_two(rand.randint(1,100), rand.randint(1,100))


# In[ ]:





# 8. Create a function for a multiplication table.  Get a number from a user and then call you function which produces a multiplication table for that number.
# The output should look something like this:
# 
#         Enter a number: 3
#         3 X 1 = 3
#         3 X 2 = 6
#         3 X 3 = 9
#         3 X 4 = 12
#         3 X 5 = 15
#         3 X 6 = 18
#         3 X 7 = 21
#         3 X 8 = 24
#         3 X 9 = 27

# In[12]:


def multiplication_table(number):
    print(f"{number} * 1 = {number *1}")
    print(f"{number} * 2 = {number *2}")
    print(f"{number} * 3 = {number *3}")
    print(f"{number} * 4 = {number *4}")
    print(f"{number} * 5 = {number *5}")
    print(f"{number} * 6 = {number *6}")
    print(f"{number} * 7 = {number *7}")
    print(f"{number} * 8 = {number *8}")
    print(f"{number} * 9 = {number *9}")
    
number = int(input("When would you like to multiply? "))
multiplication_table(number)


# In[ ]:




