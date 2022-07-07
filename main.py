#!/usr/bin/env python
# coding: utf-8

# # Functions

# On this lab we will put to practice some of the concepts we have learned on this past few days.
# 
# `NOTE: On this lab you should try to write all the functions yourself using only the most basic of python syntax and without functions such as len, count, sum, max, min, in, etc. Give it a try. 🧑🏻‍💻👩🏻‍💻`
# 
# The cell after each exercise contains a few tests to check if your function works as expected.

# In[2]:


from testing import *
import unittest


# ## 1. Write a function that returns the greater of two numbers

# In[21]:


def greater(a,b):
    if a > b:
        return (a)
    else: 
        return (b)
greater (5,3)


# In[22]:


# This will test your function 
test_greater(greater)


# ## 2. Now write a function that returns the largest element on a list

# In[153]:


def greatest(arr):
    x = 0
    for i in arr:
        if i > x:
            x=i
    return x


# In[154]:


# This will test your function 
test_greatest(greatest)


# ## 3. Write a function that sums all the elements on a list

# In[160]:


list_1 = []
def sum_all(arr):
    x=0
    for i in arr:
        x+=i
    return x


# In[161]:


# This will test your function 
test_sum(sum_all)


# ## 4. Write another function that multiplies all the elements on a list

# In[178]:


def mult_all(arr):
    x=1
    for i in arr:
        x*=i
    return x


# In[179]:


# This will test your function 
test_mult(mult_all)


# ## 5. Now combine those two ideas and write a function that receives a list and either "+" or "*" and outputs acordingly

# In[218]:


def oper_all(arr, oper):
    if oper=='*':
        c=1
        for i in arr:
            c*=i
        return c
    if oper=="+":
        x=0
        for i in arr: 
            x+=i  
        return x


# In[219]:


# This will test your function 
test_operations(oper_all)


# ## 6. Write a function that returns the factorial of a number.

# In[220]:


def factorial(n):
    arr=[]
    i=1
    s=1
    while i<n+1:
        arr.append(i)
        i+=1
    for i in arr:
        s*=i
    return s  


# In[221]:


# This will test your function 
test_factorial(factorial)


# ## 7. Write a function that takes a list and returns a list of the unique values.
# 
# `NOTE: You cannot use set. 🤔`

# In[222]:


def unique(arr):
    ar = []
    for i in arr:
        if i not in ar:
            ar.append(i)
    return ar


# In[223]:


# This will test your function 
test_unique(unique)


# ## 8. Write a function that returns the mode of a list, i.e.: the element that appears the most times.
# `NOTE: You should not use count... 🧐`

# In[224]:


def mode_counter(arr):
    return mode(arr)


# In[225]:


# This will test your function 
test_mode(mode_counter)


# ## 9. Write a function that calculates the standard deviation of a list.
# `NOTE: Do not use any libraries or already built functions. 😉`

# In[226]:


from statistics import stdev
def st_dev(arr):
    return stdev(arr)


# In[227]:


# This will test your function 
test_stdev(st_dev)


# ## 10. Write a function to check if a string is a pangram, i.e.: if it contains all the letters of the alphabet at least once. Mind that the strings may contain characters that are not letters.

# In[228]:


def pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in string.lower():
            return False
    return True


# In[229]:


# This will test your function 
test_pangram(pangram)


# ## 11. Write a function that receives a string of comma separated words and returns a string of comma separated words sorted alphabetically.
# 
# `NOTE: You may use sorted but not split and definitely no join! 🤪`

# In[232]:


def sort_alpha(string):
    character=''
    list_words=[]
    count=0
    for i in string:
        if i!=',' and count!=len(string)-1:
            character+=i
            
        elif i==',':
            list_words.append(character) 
            character=''
            
        else :
            list_words.append(character+i)
            
        count+=1
    list_words=sorted(list_words)
    words=''
    for j in list_words:
        if list_words.index(j)!=len(list_words)-1:
            words+=j+','
        else:
            words+=j
    return words


# In[233]:


# This will test your function 
test_alpha(sort_alpha)


# ## 12. Write a function to check if a given password is strong (at least 8 characters, at least one lower case, at least one upper case, at least one number and at least one special character). It should output True if strong and False if not.
# `Valid special characters: # @ ! $ % & ( ) ^ * [ ] { }`

# In[216]:


#if you use return it will stop the code so make sure it is towards the end
def check_pass(string):
    
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    special = "#@!$%&()^*[]{}"
    upper_letter = False
    lower_letter = False
    count_letters = 0
    special_boolean = False
    numbers_boolean = False
    count = 0
    
    for letter in string:
        count_letters += 1
        if letter in alphabet:
            if letter.isupper():
                 upper_letter = True
            if letter.islower():
                lower_letter = True
        elif letter in numbers:
            numbers_boolean = True
        elif letter in special:
            special_boolean = True
            
    if count_letters >= 8 and upper_letter and lower_letter and special_boolean and numbers_boolean:
        return True
    else:
        return False


# In[217]:


# This will test your function 
test_pass(check_pass)


# In[ ]:




