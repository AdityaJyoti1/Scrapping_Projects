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


# In[20]:


Tram1=['Ajuste Lerma','Origen Sitel - Destino Sitel','Complemento Cruce I+D','Origen I+D-Destino I+D','Complemento Tedisa','Origen I+D-Destino I+D',
 'Complemento Tedisa',
 'Origen TEDISA-Destino TEDISA',
 'Complemento Televia',
 'Origen Televia-Destino Televia',
 'Origen Televia-Destino Televia',
 'Complemento Osipass',
 'Origen OSIPASS - Destino OSIPASS',
 'Tramo nuevo carril',
 'Complemento de Cruce I+D',
 'Complemento de Cruce Osipass',
 'Complemento de Cruce Tedisa',
 'Complemento de Cruce Televia',
 'Complemento de Cruce Viapass']
driver = webdriver.Chrome()
driver.get('https://www.viapass.com.mx/viapass/web_tarifas.aspx')
Tramo=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id,'span_TRAMODSC')]") if item.text not in Tram1 ]
labels=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id,'span_vCLASEVEHICULOCVE')]")]
label = list( dict.fromkeys(labels) )
label.append('Tramos')
AUTOMOVILES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0001')]")]
AUTOMOVIL_CON_REMORQUE_1_EJE=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0002')]")]
AUTOMOVIL_CON_REMOLQUE_2_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0003')]")]
AUTOBUS_2_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0004')]")]
AUTOBUS_3_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0005')]")]
AUTOBUS_4_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0006')]")]
CAMION_2_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0007')]")]
CAMION_3_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0008')]")]
CAMION_4_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0009')]")]
CAMION_5_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0010')]")]
CAMION_6_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0011')]")]
CAMION_7_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0012')]")]
CAMION_8_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0013')]")]
CAMION_DE_9_O_MAS_EJES=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0014')]")]
# MOTOCICLETAS=[item.text for item in driver.find_elements_by_xpath("//*[contains(@id, 'span_TRAMOCUOTA_0015')]")]


# In[21]:


df = pd.DataFrame(columns=label)
df['Tramos']=pd.Series(Tramo)
df['A - AUTOMOVILES']=pd.Series(AUTOMOVILES)
df['AR1 - AUTOMOVIL CON REMORQUE 1 EJE']=pd.Series(AUTOMOVIL_CON_REMORQUE_1_EJE)
df['AR2 - AUTOMOVIL CON REMOLQUE 2 EJES']=pd.Series(AUTOMOVIL_CON_REMOLQUE_2_EJES)
df['B2 - AUTOBUS 2 EJES']=pd.Series(AUTOBUS_2_EJES)
df['B3 - AUTOBUS 3 EJES']=pd.Series(AUTOBUS_3_EJES)
df['B4 - AUTOBUS 4 EJES']=pd.Series(AUTOBUS_4_EJES)
df['C2 - CAMION 2 EJES']=pd.Series(CAMION_2_EJES)
df['C3 - CAMION 3 EJES']=pd.Series(CAMION_3_EJES)
df['C4 - CAMION 4 EJES']=pd.Series(CAMION_4_EJES)
df['C5 - CAMION 5 EJES']=pd.Series(CAMION_5_EJES)
df['C6 - CAMION 6 EJES']=pd.Series(CAMION_6_EJES)
df['C7 - CAMION 7 EJES']=pd.Series(CAMION_7_EJES)
df['C8 - CAMION 8 EJES']=pd.Series(CAMION_8_EJES)
df['C9+ - CAMION DE 9 O MAS EJES']=pd.Series(CAMION_DE_9_O_MAS_EJES)
# df['M - MOTOCICLETAS']=pd.Series(MOTOCICLETAS)


# In[22]:


df = df[['Tramos','A - AUTOMOVILES', 'AR1 - AUTOMOVIL CON REMORQUE 1 EJE',
       'AR2 - AUTOMOVIL CON REMOLQUE 2 EJES', 'B2 - AUTOBUS 2 EJES',
       'B3 - AUTOBUS 3 EJES', 'B4 - AUTOBUS 4 EJES', 'C2 - CAMION 2 EJES',
       'C3 - CAMION 3 EJES', 'C4 - CAMION 4 EJES', 'C5 - CAMION 5 EJES',
       'C6 - CAMION 6 EJES', 'C7 - CAMION 7 EJES', 'C8 - CAMION 8 EJES',
       'C9+ - CAMION DE 9 O MAS EJES', 'M - MOTOCICLETAS', 'P', 'VNC']]
df.set_index('Tramos',inplace=True)


# In[23]:


df.fillna(-1,inplace=True)


# In[24]:


df.to_csv(r'C:\Users\aditya_jyoti\Documents\Docs\Teaching\ash\scrapped.csv')

