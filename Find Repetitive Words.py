#!/usr/bin/env python
# coding: utf-8

# In[6]:


mysentence = input("Please enter a sentence to find out how many words are repeated: ")
msl = mysentence.lower()
msl2 = msl.split()

count = {}
for i in msl2:
    if i not in count:
        count[i] = 0
    count[i]+=1

for a in count:
    print(a + " is repeated " + str(count[a]) + " times.")


# In[ ]:




