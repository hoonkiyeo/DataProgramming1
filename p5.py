#!/usr/bin/env python
# coding: utf-8

# In[1]:


# project: p5


# In[2]:


#project.py

__hurricane__ = []

def __init__():
    import csv
    """This function will read in the csv_file and store it in a list of dictionaries"""
    with open('hurricanes.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            __hurricane__.append(row)

def count():
    """This function will return the number of records in the dataset"""
    return len(__hurricane__)

def get_name(idx):
    """get_name(idx) returns the name of the hurricane in row idx"""
    return __hurricane__[int(idx)]['name']

def get_formed(idx):
    """get_formed(idx) returns the date of formation of the hurricane in row idx"""
    return (__hurricane__[int(idx)]['formed'])

def get_dissipated(idx):
    """get_dissipated(idx) returns the date of dissipation of the hurricane in row idx"""
    return (__hurricane__[int(idx)]['dissipated'])

def get_mph(idx):
    """get_mph(idx) returns the mph of the hurricane in row idx"""
    return int(__hurricane__[int(idx)]['mph'])

def get_damage(idx):
    """get_damage(idx) returns the damage in dollars of the hurricane in row idx"""
    return __hurricane__[int(idx)]['damage']

def get_deaths(idx):
    """get_deaths(idx) returns the deaths of the hurricane in row idx"""
    return int(__hurricane__[int(idx)]['deaths'])

__init__()


# In[3]:


import project
dir(project)


# In[4]:


#Q1: How many records are in the dataset?

project.count()


#output
'''
133
'''


# In[5]:


#Q2: What is the name of the hurricane at last index?

project.get_name(project.count()-1)

#output
'''
'Omar'
'''


# In[6]:


#Q3: How many deaths were caused by the hurricane at index 10?

project.get_deaths(10)

#output
'''
72
'''


# In[7]:


#Q4:Is there a hurricane named Bob?

for i in range(project.count()):
    if project.get_name(i) == "Bob":
        print(True)
        break
        
    else:
        continue

        
#output
'''
True
'''


# In[8]:


#Q5: How many hurricanes named Florence are in the dataset?

count = 0

for i in range(project.count()):
    if project.get_name(i).upper() == "FLORENCE":
        count += 1
    else:
        continue
        
count

#output
'''
3
'''


# In[9]:


#Q6: What is the fastest MPH achieved by a hurricane in the dataset?

mph = 0

for i in range(project.count()):
    if project.get_mph(i) > mph:
        mph = project.get_mph(i)
    else:
        continue
        
mph

#output
'''
190
'''


# In[10]:


#Q7: What is the name of that fastest hurricane?

name = None

for i in range(project.count()):
    if project.get_mph(i) == mph:
        name = project.get_name(i)
name

#output
'''
'Allen'
'''


# In[11]:


#Q8: What is the damage (in dollars) caused by the fastest hurricane?
def format_damage(damage):
    if damage[-1] == "K":
        return float(damage[:-1]) * 1000

    if damage[-1] == "M":
        return float(damage[:-1]) * 1000000
    
    if damage[-1] == "B":
        return float(damage[:-1]) * 1000000000

        
damage = 0
for i in range(project.count()):
    if project.get_name(i) == name:
        damage = project.get_damage(i)
    else:
        continue

int(format_damage(damage))

#output
'''
1570000000
'''


# In[12]:


#Q9: What is the total number of deaths by all the hurricanes in the dataset?

total = 0

for i in range(project.count()):
    total += project.get_deaths(i)
    
total

#output
'''
18960
'''


# In[13]:


def get_month(date):
    '''Returns the month when the date is the in the 'mm/dd/yyyy' format'''
    return (date[:2])

def get_day(date):
    '''Returns the day when the date is the in the 'mm/dd/yyyy' format'''
    return int(date[3:5])

def get_year(date):
    '''Returns the year when the date is the in the 'mm/dd/yyyy' format'''
    return int(date[-4:])


# In[14]:



# return index of deadliest hurricane over the given date range
def deadliest_in_range(year1, year2):
    worst_idx = 0
    for i in range(project.count()):
        if get_year(project.get_formed(i)) >= year1:
            if get_year(project.get_formed(i)) <= year2:
                if project.get_deaths(i) > project.get_deaths(worst_idx):
                    worst_idx = i
    return worst_idx


# In[15]:


#Q10: What was the deadliest hurricane between 2010 and 2020 (inclusive)?

project.get_name(deadliest_in_range(2010, 2020))


#output
'''
Maria
'''


# In[16]:


#Q11: What was the deadliest hurricane of the 20th century (1901 to 2000, inclusive)?

project.get_name(deadliest_in_range(1901, 2000))

#output
'''
'Inez'
'''


# In[17]:


#Q12: In what year did the most deadly hurricane in the dataset form?

get_year(project.get_formed(deadliest_in_range(0,5000)))

#output
'''
1899
'''


# In[18]:


#Q13: How much damage (in dollars) was done by the deadliest hurricane of the 21th century?

#21th century = 2001 ~ 2100

int(format_damage(project.get_damage(deadliest_in_range(2001, 2100))))

#output
'''
91610000000
'''


# In[19]:


#Q14: What were the total damages across all hurricanes in the dataset, in dollars?

total_dmg = 0

for i in range(project.count()):
    total_dmg += int(format_damage(project.get_damage(i)))
    
total_dmg

#output
'''
864830464997
'''


# In[20]:


# return number of huricanes formed in month mm
def hurricanes_in_month(mm):
    num_of_hurricanes = 0
    for i in range(project.count()):
        if get_month(project.get_formed(i)) == mm:
            num_of_hurricanes += 1
        else:
            continue
    return num_of_hurricanes


# In[21]:


#Q15: How many hurricanes were formed in the month of June?

hurricanes_in_month("06")

#output
'''
4
'''


# In[22]:


#Q16: How many hurricanes were formed in the month of January?
hurricanes_in_month("01")


#output
'''
3
'''


# In[23]:


most_num = 0
which_month = 0

for i in range(10):
    if hurricanes_in_month("0"+str(i)) > most_num:
        most_num = hurricanes_in_month("0"+str(i))
        if hurricanes_in_month(str(i)) > most_num:
            most_num = hurricanes_in_month(str(i))
            which_month = i
i

#output
'''
9
'''


# In[24]:


#Q17: Which month experienced the formation of the most number of hurricanes?
most_num = 0
which_month = 0

for i in range(10):
    if hurricanes_in_month("0"+str(i)) > most_num:
        most_num = hurricanes_in_month("0"+str(i))
        if hurricanes_in_month(str(i)) > most_num:
            most_num = hurricanes_in_month(str(i))
            which_month = i
i


#output
'''
9
'''


# In[25]:


#Q18: How many hurricanes were formed in the decade of 1990-1999 (inclusive)?

count = 0

for i in range(project.count()):
    if get_year(project.get_formed(i)) >= 1990 and get_year(project.get_formed(i)) <= 1999:
        count += 1
    else:
        continue
        
count


#output
'''
25
'''


# In[26]:


#Q19: How many years in the history experienced a hurricane that caused more than 200 in deaths?


year_list = []


for i in range(project.count()):
    if project.get_deaths(i) > 200:
        year_list.append(get_year(project.get_formed(i)))
    else:
        continue
        
len(year_list)


#output
'''
16
'''


# In[27]:


#Q20: How many years in the history experienced a hurricane that caused more than 10 Billion in damage?

year_list = []

for i in range(project.count()):
    if int(format_damage(project.get_damage(i))) > 10000000000:
        year_list.append(get_year(project.get_formed(i)))
        
year_list = set(year_list)
len(year_list)


#output
'''
11
'''

