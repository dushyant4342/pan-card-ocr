#!/usr/bin/env python
# coding: utf-8

# In[1]:


import io
import json
import cv2
import matplotlib.pyplot as plt
import os
import os.path
import json
import sys
import pytesseract
import re
import difflib
import csv
import dateutil.parser as dparser
from PIL import Image
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
import ftfy


# In[2]:


img=cv2.imread("pan_card.jpg")


# In[3]:


plt.imshow(img)


# In[4]:


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap='gray')


# In[5]:


text = pytesseract.image_to_string(gray_img)


# In[6]:


print(text)


# In[7]:


name = None
fname = None
dob = None
pan = None
nameline = []
dobline = []
panline = []
text0 = []
text1 = []
text2 = []
govRE_str = '(GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT             |PARTMENT|ARTMENT|INDIA|NDIA)$'
numRE_str = '(Number|umber|Account|ccount|count|Permanent|             renmanent|manent)$'
incOM_str = '(INCOMETAXDEPARWENT|INCOME|TAX|GOW|GOVT|             GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA)$'


# In[8]:


lines = text.split('\n')
for lin in lines:
    s = lin.strip()
    s = lin.replace('\n','')
    s = s.rstrip()
    s = s.lstrip()
    text1.append(s)

text1 = list(filter(None, text1))
print(text1)


lineno = 0  # to start from the first line of the text file.

for wordline in text1:
    xx = wordline.split('\n')
    if ([w for w in xx if re.search(incOM_str, w)]):
        text1 = list(text1)
        lineno = text1.index(wordline)
        break

# text1 = list(text1)
text0 = text1[lineno+1:]
print(text0) 


# In[9]:


def findword(textlist, wordstring):
    lineno = -1
    for wordline in textlist:
        xx = wordline.split( )
        if ([w for w in xx if re.search(wordstring, w)]):
            lineno = textlist.index(wordline)
            textlist = textlist[lineno+1:]
            return textlist
    return textlist


# In[10]:


name=text0[0]
fname=text0[1]
dob=text0[2]


# In[11]:


text2 = findword(text1, '(Pormanam|Number|umber|Account|ccount|count|Permanent|ermanent|manent|wumm)$')
pan = text2[0]


# In[12]:


data={}
data['Name'] = name
data['Father Name'] = fname
data['Date of Birth'] = dob
data['PAN'] = pan


# In[13]:


data


# In[37]:


# Writing data into JSON
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Write JSON file
with io.open('data.json', 'w', encoding='utf-8') as outfile:
    str_ = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json', encoding = 'utf-8') as data_file:
    data_loaded = json.load(data_file)

#print(data == data_loaded)

# Reading data back JSON(give correct path where JSON is stored)
with open('data.json', 'r', encoding= 'utf-8') as f:
    ndata = json.load(f)

# print('\t', "|+++++++++++++++++++++++++++++++|")
print('\t', 'Name:', '\t', ndata['Name'])
# print('\t', "|-------------------------------|")
print('\t', 'Father Name:', '\t', ndata['Father Name'])
# print('\t', "|-------------------------------|")
print('\t', 'Date of Birth:', '\t', ndata['Date of Birth'])
# print('\t', "|-------------------------------|")
print('\t', 'Pan Id:', '\t', ndata['PAN'])
# print('\t', "|+++++++++++++++++++++++++++++++|")



# In[38]:


import pickle


# In[8]:


# Saving model to disk
pickle.dump( , open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))


# In[ ]:





# In[ ]:





# In[ ]:




