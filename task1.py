#!/usr/bin/env python
# coding: utf-8

# In[1]:

# mgasa


import math
import os
import random
import re
import sys


# In[2]:


def virusIndices(p, v):
    len_p = len(p)
    len_v = len(v)
    
    matching_indices = []
    
    for i in range(len_p - len_v + 1):
        substring = p[i:i + len_v]
        # Count mismatches
        mismatches = sum(1 for x, y in zip(substring, v) if x != y)
        if mismatches <= 1:
            matching_indices.append(i)
    
    if matching_indices:
        print(' '.join(map(str, matching_indices)))
    else:
        print("No Match!")


# In[10]:


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = first_multiple_input[0]
        v = first_multiple_input[1]

        virusIndices(p, v)


# In[ ]:


# mgasa


