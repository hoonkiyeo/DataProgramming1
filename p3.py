#!/usr/bin/env python
# coding: utf-8

# In[9]:


#project.py

from csv import DictReader as __DictReader

# key: (agency_id, year), val: spending in millions
__data = None

# key: agency name, val: agency ID
__agency_to_id = None


def init(path):
    """init(path) must be called to load data before other calls will work.  You should call it like this: init("madison.csv")"""

    global __data
    global __agency_to_id

    if path != 'madison.csv':
        print("WARNING!  Opening a path other than madison.csv.  " +
              "That's fine for testing your code yourself, but madison.csv " +
              "will be the only file around when we test your code " +
              "for grading.")

    __data = {}
    __agency_to_id = {}

    with open(path) as f:
        reader = __DictReader(f)
        for row in reader:
            agency_id = int(row['agency_id'])
            __agency_to_id[row['agency']] = agency_id
            for year in range(2015, 2018+1):
                __data[(agency_id, year)] = float(row[str(year)])

def dump():
    """prints all the data to the screen"""
    if __agency_to_id == None:
        raise Exception("you did not call init first")
    
    for agency in sorted(__agency_to_id.keys()):
        agency_id = __agency_to_id[agency]
        print("%-7s [ID %d]" % (agency, agency_id))
        for year in range(2015, 2018+1):
            print("  %d: $%f MILLION" % (year, __data[(agency_id, year)]))
        print()


def get_id(agency):
    """get_id(agency) returns the ID of the specified agency."""
    if __agency_to_id == None:
        raise Exception("you did not call init first")
    if not agency in __agency_to_id:
        raise Exception("No agency '%s', only these: %s" %
                        (str(agency), ','.join(list(__agency_to_id.keys()))))
    return __agency_to_id[agency]


def get_spending(agency_id, year=2018):
    """get_spending(agency_id, year) returns the dollars spent (in millions) by the specified agency in specified year."""
    if __data == None:
        raise Exception("you did not call init first")
    if not (agency_id, year) in __data:
        raise Exception("No data for agency %s, in year %s" %
                        (str(agency_id), str(year)))
    return __data[(agency_id, year)]


# In[ ]:


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

