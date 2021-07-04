#!/usr/bin/env python
# coding: utf-8

# In[1]:



# project: p2


# In[22]:


#q1: what is 1+1?



1+1


# In[23]:


#q2: what is 2+2?

2+2


# In[24]:


#q3: what is the type of 220?


type(220)


# In[25]:


#q4: what is the type of 220/4?

type(220/4)


# In[26]:


#q5: what is the type of 220//4?

type(220//4)


# In[27]:


#q6: what is the type of "220"?  Note the quotes!
type("220")


# In[28]:


#q7: what is the type of "False"?  Note the quotes!

type("False")


# In[29]:


#q8: what is the type of True?

type(True)


# In[30]:


#q9: what is the type of 1000<999?

type(1000<999)


# In[31]:


#q10: what is two hundred plus twenty?

# fix the below to make Python do an addition that produces 220

200 + 20


# In[32]:


#q11: please fix the following to display 5 smileys

":)" * 5


# In[33]:


#q12: please fix the following to get 42

6 * 7


# In[34]:


#q13: what is the volume of a cube with side length of 6?


6 ** 3


# In[35]:


#q14: you start with 20 dollars and triple your money every decade.
# how much will you have after 4 decades?

20*3**4


# In[36]:


#q15: fix the Python logic to match the English

# In English: 220 is less than 320 and greater than 400

# In Python:
400 < 220 < 320 


# In[37]:


#q16: change ONLY the value of x to get True for the output

x = -35

x < -30 and x > -40


# In[38]:


#q17: change ONLY the value of x to get True for the output

x = 250

(x > 200 and x < 251) and (x > 249 and x < 300)


# In[39]:


#q18: what???

x = 4

# fix the following logic so we get True, not 4.
# The correct logic should check whether x is either
# -4 or 4.  The problem is with types: to the left
# of the or, we have a boolean, and to the right of
# the or, we have an integer.  This semester, we will
# always try to have a boolean to both the left and
# right of logical operators such as or.

x == -4 or x==4


# In[40]:


#q19: we should win!

number = 36

# There are three winners, with numbers 36, 323, and 325.
# The following should output True if number is changed
# to be any of these (but the logic is currently wrong).
#
# Please update the following expression so we get True
# if the number variable is changed to any of the winning
# options.

# Did we win?
number == 36 or number == 323 or number == 325


# In[41]:


#q20: what is the volume of a cylinder with radius 4 and height 2?
# you may assume PI is 3.14 if you like (a close answer is good enough)

3.14*4**2*2

