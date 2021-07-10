#!/usr/bin/env python
# coding: utf-8

# In[8]:


#project.py
__pokemon__= {}

def __init__():
    """This function will read the data from 'pokemon_stats.csv' and store it in a dictionary of dictionaries"""
    import csv
    f = open('pokemon_stats.csv', encoding='utf-8')
    data = list(csv.reader(f))
    f.close()
    header = data[0]
    header.pop(0)
    data = data[1:]
    for pkmn_data in data:
        pkmn_data.pop(0)
        pkmn = {}
        for i in range(len(header)):
            pkmn[header[i]] = pkmn_data[i]
        for stat in pkmn:
            if stat in ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']:
                pkmn[stat] = int(pkmn[stat])
        __pokemon__[pkmn["Name"]] = pkmn

def print_stats(pkmn):
    """print_stats(pkmn) prints all the statistics of the Pokémon with the name 'pkmn' """
    try:
        for stat in __pokemon__[pkmn]:
            if not (stat == 'Type 2' and __pokemon__[pkmn][stat] == "None"):
                print(stat, ": ", __pokemon__[pkmn][stat])
    except KeyError:
        print(pkmn, " not found in the file")

def get_region(pkmn):
    """get_region(pkmn) returns the region of the Pokémon with the name 'pkmn' """
    return __pokemon__[pkmn]['Region']

def get_type1(pkmn):
    """get_type1(pkmn) returns Type 1 of the Pokémon with the name 'pkmn' """
    return __pokemon__[pkmn]['Type 1']

def get_type2(pkmn):
    """get_type2(pkmn) returns Type 2 of the Pokémon with the name 'pkmn' """
    return __pokemon__[pkmn]['Type 2']

def get_hp(pkmn):
    """get_hp(pkmn) returns the HP of the Pokémon with the name 'pkmn' """
    return __pokemon__[pkmn]['HP']

def get_attack(pkmn):
    """get_attack(pkmn) returns the Attack of the Pokémon with the name 'pkmn' """
    return __pokemon__[pkmn]['Attack']

def get_defense(pkmn):
    """get_defense(pkmn) returns the Defense of the Pokémon with the name 'pkmn' """
    return __pokemon__[pkmn]['Defense']

def get_sp_atk(pkmn):
    """get_sp_atk(pkmn) returns the Special Attack of the Pokémon with the name 'pkmn' """
    return __pokemon__[pkmn]['Sp. Atk']

def get_sp_def(pkmn):
    """get_sp_def(pkmn) returns the Special Defense of the Pokémon with the name 'pkmn' """
    return __pokemon__[pkmn]['Sp. Def']

def get_speed(pkmn):
    """get_speed(pkmn) returns the Speed of the Pokémon with the name 'pkmn' """
    return __pokemon__[pkmn]['Speed']

__init__()


# In[9]:


import math
import project


# In[10]:


def get_stat_total(pkmn):
    return (project.get_attack(pkmn) +
             project.get_sp_atk(pkmn) +
             project.get_hp(pkmn) +
             project.get_defense(pkmn) +
             project.get_speed(pkmn) +
             project.get_sp_def(pkmn))


# In[11]:


def simple_battle(pkmn1, pkmn2):
    
    if get_stat_total(pkmn1) > get_stat_total(pkmn2):
        return pkmn1
    elif get_stat_total(pkmn1) < get_stat_total(pkmn2):
        return pkmn2
    elif abs(get_stat_total(pkmn1) - get_stat_total(pkmn2) < 20):
        return "Draw"


# In[12]:


#Q1: What is the output of simple_battle('Gligar', 'Pidgeotto')?

simple_battle('Gligar', 'Pidgeotto')


# In[13]:


#Q2: What is the output of simple_battle('Gligar', 'Pidgeot')?

simple_battle('Gligar', 'Pidgeot')


# In[12]:


#Q3: What is the output of simple_battle('Chikorita', 'Turtwig')?

simple_battle('Chikorita', 'Turtwig')


# In[13]:


#Q4: What is the output of simple_battle('Kingler', 'Staraptor')?

simple_battle('Kingler', 'Staraptor')


# In[14]:


#Q5: What is the output of simple_battle('Heracross', 'Krookodile')?

simple_battle('Heracross', 'Krookodile')


# In[16]:


def most_damage(attacker, defender):
    physical_move = 10 * project.get_attack(attacker)/project.get_defense(defender)
    speical_move = 10 * project.get_sp_atk(attacker) / project.get_sp_def(defender)
    
    if physical_move > speical_move:
        return physical_move
    else:
        return speical_move


# In[17]:


#Q6: What is the damage that will be done by Caterpie to Incineroar?

most_damage("Caterpie", "Incineroar")


# In[18]:


#Q7: What is the damage that will be done by Naganadel to Rockruff?

most_damage("Naganadel", "Rockruff")


# In[19]:


#Q8: What is the damage that will be done by Taillow to Swellow?

most_damage("Taillow", "Swellow")


# In[20]:


#Q9: What is the damage that will be done by Swellow to Taillow?

most_damage("Swellow", "Taillow")


# In[22]:


def num_hits(attacker, defender):
    return math.ceil(project.get_hp(defender)/most_damage(attacker,defender))


# In[24]:


#Q10: How many hits can Goomy take from Gible?

num_hits("Gible", "Goomy")


# In[25]:


#Q11: How many hits can Donphan take from Aipom?

num_hits("Aipom", "Donphan")


# In[26]:


#Q12: How many hits can Aipom take from Donphan?

num_hits("Donphan", "Aipom")


# In[32]:


def battle(pkmn1, pkmn2):
    if num_hits(pkmn1, pkmn2) > num_hits(pkmn2, pkmn1):
        return pkmn2
    elif num_hits(pkmn1, pkmn2) < num_hits(pkmn2, pkmn1):
        return pkmn1
    elif num_hits(pkmn1, pkmn2) == num_hits(pkmn2, pkmn1):
        if project.get_speed(pkmn1) > project.get_speed(pkmn2):
            return pkmn1
        elif project.get_speed(pkmn1) < project.get_speed(pkmn2):
            return pkmn2
        else:
            return "Draw"
    #TODO: Return the name of the pkmn that can take more hits from the other
    # pkmn. If both pkmn faint within the same number of moves, return the
    # string 'Draw'


# In[28]:


#Q13: What is the outcome of battle('Infernape', 'Torterra')?

battle('Infernape', 'Torterra')


# In[29]:


#Q14: What is the outcome of battle('Torkoal', 'Sceptile')?

battle('Torkoal', 'Sceptile')


# In[30]:


#Q15: What is the outcome of battle('Tepig', 'Oshawott')?

battle('Tepig', 'Oshawott')


# In[33]:


#Q16: What is the outcome of battle('Bulbasaur', 'Squirtle')?

battle('Bulbasaur', 'Squirtle')


# In[34]:


#Q17: What is the outcome of battle('Greninja', 'Hawlucha')?

battle('Greninja', 'Hawlucha')


# In[35]:


#Q18: What is the outcome of battle('Snorlax', 'Charizard')?

battle('Snorlax', 'Charizard')


# In[36]:


def final_battle(pkmn1, pkmn2):
    if project.get_region(pkmn1) != project.get_region(pkmn2):
        return "Cannot battle"
    else:
        return battle(pkmn1, pkmn2)


# In[37]:


#Q19: What is the outcome of final_battle('Pikachu', 'Snivy')?

final_battle('Pikachu', 'Snivy')


# In[38]:


def final_battle(pkmn1, pkmn2):
    if project.get_region(pkmn1) != project.get_region(pkmn2):
        if project.get_type1(pkmn1) or project.get_type2(pkmn1) == "Flying":
            return battle(pkmn1, pkmn2)
        elif project.get_type1(pkmn2) or project.get_type2(pkmn2) == "Flying":
            return battle(pkmn1, pkmn2)
        else:
            return "Cannot battle"
    else:
        return battle(pkmn1, pkmn2)


# In[39]:


#Q20: What is the outcome of final_battle('Dragonite', 'Goodra')?

final_battle('Dragonite', 'Goodra')

