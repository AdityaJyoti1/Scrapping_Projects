#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from shutil import which
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# In[2]:


chrome_path=which("chromedriver")


# In[3]:


driver = webdriver.Chrome()
driver.get('http://carreteras.chihuahua.gob.mx/tarifas.html')

#Table1
tr_1=[item.text for item in driver.find_elements_by_xpath('//table[1]/tbody/tr')]
header_1=[item.text for item in driver.find_elements_by_xpath('//table[1]/thead/tr/th')]  

#Table2
tr_2=[item.text for item in driver.find_elements_by_xpath('//table[2]/tbody/tr')]
header_2=[item.text for item in driver.find_elements_by_xpath('//table[2]/thead/tr/th')] 


# In[6]:


data1=[]
Container_1=[]
import re
for items in tr_1:
    x=items.split('$')
    Container_1.append(x)
for entries in Container_1:
    data1.append(dict(zip(header_1, entries)))


# In[8]:


data2=[]
Container_2=[]
import re
for item in tr_2:
    y=item.split('$')
    Container_2.append(y)
for j in Container_2:
    data2.append(dict(zip(header_2, j)))


# In[14]:


table1=pd.DataFrame(data1)
table2=pd.DataFrame(data2)


# In[18]:


table1.to_csv(r'C:\Users\aditya\Documents\Docs\Teaching\ash\table1.csv')
table2.to_csv(r'C:\Users\aditya\Documents\Docs\Teaching\ash\table2.csv')


# In[ ]:




