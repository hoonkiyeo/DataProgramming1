#!/usr/bin/env python
# coding: utf-8

# In[9]:


import project
import csv


# In[10]:


project.init("madison.csv")


# In[11]:


#Q1: What is the agency ID of the library agency?

project.get_id("library")


# In[13]:


#Q2: How much did the agency with ID 5 spend in 2018?

project.get_spending(5, 2018)


# In[16]:


#Q3: How much did "streets" spend in 2016?

streets_id = project.get_id("streets")
project.get_spending(streets_id)


# In[17]:


def year_max(year):
    # grab the spending by each agency in the given year
    police_spending = project.get_spending(project.get_id("police"), year)
    fire_spending = project.get_spending(project.get_id("fire"), year)
    library_spending = project.get_spending(project.get_id("library"), year)
    parks_spending = project.get_spending(project.get_id("parks"), year)
    streets_spending = project.get_spending(project.get_id("streets"), year)

    # use builtin max function to get the largest of the five values
    return max(police_spending, fire_spending, library_spending, parks_spending, streets_spending)


# In[19]:


#Q4: What was the most spent by a single agency in 2017?

year_max(2017)


# In[20]:


#Q5: What was the most spent by a single agency in 2018?

year_max(2018)


# In[21]:


def agency_min(agency):
    agency_id = project.get_id(agency)
    y15 = project.get_spending(agency_id, 2015)
    y16 = project.get_spending(agency_id, 2016)
    y17 = project.get_spending(agency_id, 2017)
    y18 = project.get_spending(agency_id, 2018)

    return min(y15, y16, y17, y18)


# In[23]:


#Q6: What was the least the fire agency ever spent in a year?

agency_min("fire")


# In[24]:


#Q7: What was the least that library ever spent in a year?

agency_min("library")


# In[25]:


#Q8: What was the least that parks ever spent in a year?

agency_min("parks")


# In[26]:


def agency_avg(agency):
    y15 = project.get_spending(project.get_id(agency), 2015)
    y16 = project.get_spending(project.get_id(agency), 2016)
    y17 = project.get_spending(project.get_id(agency), 2017)
    y18 = project.get_spending(project.get_id(agency), 2018)
    
    return ((y15+y16+y17+y18)/4)


# In[27]:


#Q9: How much is spent per year on streets, on average?

agency_avg("streets")


# In[29]:


#Q10: How much is spent per year on parks, on average?

agency_avg("parks")


# In[32]:


#Q11: How much did the police spend above their average in 2018?

(project.get_spending(project.get_id("police"), 2018) - agency_avg("police"))/agency_avg("police") * 100


# In[40]:


def change_per_year(agency, start_year=2015, end_year=2018):
    x = project.get_spending(project.get_id(agency), start_year)
    y = project.get_spending(project.get_id(agency), end_year)
    return (y-x)/ (end_year - start_year)


# In[41]:


#Q12: how much has spending increased per year (on average) for parks from 2015 to 2018?

change_per_year("parks")


# In[42]:


#Q13: how much has spending increased per year (on average) for streets from 2017 to 2018?

change_per_year("streets", start_year = 2017, end_year = 2018)


# In[43]:


#Q14: how much has spending increased per year (on average) for streets from 2016 to 2018?

change_per_year("streets", start_year = 2016, end_year = 2018)


# In[50]:


def extrapolate(agency, year1, year2, year3):
    
    x = project.get_spending(project.get_id(agency), year1)
    y = project.get_spending(project.get_id(agency), year2)
    
    return x + change_per_year(agency, year1, year2) * (year3 - year1)


# In[51]:


#Q15: how much will library spend in 2019?

extrapolate("library", year1 = 2015, year2 = 2018, year3 = 2019)


# In[52]:


#Q16: how much will library spend in 2100?

extrapolate("library", year1 = 2015, year2= 2018, year3 = 2100)


# In[53]:


#Q17: how much will library spend in 2100?

extrapolate("library", year1 = 2016, year2 = 2018, year3 = 2100)


# In[56]:


def extrapolate_error(agency, year1, year2, year3):
    
    x = project.get_spending(project.get_id(agency), year1)
    y = project.get_spending(project.get_id(agency), year2)
    extrapolate = x + change_per_year(agency, year1, year2) * (year3 - year1)
    
    return extrapolate - project.get_spending(project.get_id(agency), year3)


# In[57]:


#Q18: what is the error if we extrapolate to 2018 from the 2015-to-2017 data for police?


extrapolate_error("police", 2015, 2017, 2018)


# In[59]:


#Q19: what is the percent error if we extrapolate to 2018 from the 2015-to-2016 data for streets?

(extrapolate_error("streets", 2015, 2016, 2018) / project.get_spending(project.get_id("streets"), 2018)) * 100


# In[61]:


#Q20: what is the standard deviation for library spending over the 4 years?

def sd(agency):
    y15 = project.get_spending(project.get_id(agency), 2015)
    y16 = project.get_spending(project.get_id(agency), 2016)
    y17 = project.get_spending(project.get_id(agency), 2017)
    y18 = project.get_spending(project.get_id(agency), 2018)
    
    avg = (y15+y16+y17+y18)/4
    
    return (((y15-avg)**2+(y16-avg)**2+(y17-avg)**2+(y18-avg)**2)/4)**0.5

sd("library")


# In[62]:


#Q21: what is the standard deviation for police spending over the 4 years?

sd("police")


# In[67]:


#Q22: what is the standard deviation for fire spending over the 4 years?

sd("fire")


# In[69]:


#Q23: what is the standard deviation for parks spending over the 4 years?

sd("parks")


# In[70]:


#Q24: what is the standard deviation for streets spending over the 4 years?

sd("streets")


# In[ ]:




