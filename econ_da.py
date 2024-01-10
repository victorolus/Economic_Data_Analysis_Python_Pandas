#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().system('pip install fredapi > /dev/null')


# In[9]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px

plt.style.use('fivethirtyeight')
pd.set_option('display.max_columns',500)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]

from fredapi import Fred

fred_key = '6a2a70d4c3e671dc17bf8e3d461c147a'


# # 1. Create the Fred object

# In[10]:


fred = Fred(api_key='6a2a70d4c3e671dc17bf8e3d461c147a')


# In[11]:


fred


# # 2. Search for economic data

# In[15]:


sp_search = fred.search('S&P',order_by='popularity')


# In[18]:


sp_search.head()


# # 3. Pull Raw Data & Plot

# In[27]:


sp500 = fred.get_series(series_id='SP500')
sp500.plot(figsize=(10,5),title='S&P 500', lw=2)


# # 4. Pull and Join Multiple Data Series

# In[143]:


unemp_df = fred.search('unemployment rate state',filter=('frequency', 'Monthly'))
unemp_df = unemp_df.query('seasonal_adjustment == "Seasonally Adjusted" and units == "Percent"')
unemp_df = unemp_df.loc[unemp_df['title'].str.contains('Unemployment Rate')]

unemp_df = unemp_df[unemp_df['id'].str.len() == 4]

# Now unemp_df contains only rows where the 'id' has a length of 4


# In[264]:


all_results = []

for myid in unemp_df.index:
    results =fred.get_series(myid)
    results = results.to_frame(name=myid)
    all_results.append(results)
uemp_states = pd.concat(all_results, axis=1)    


# In[270]:


uemp_states = uemp_states.dropna()
id_to_state = unemp_df['title'].str.replace( 'Unemployment Rate in ',''). to_dict()
uemp_states.columns = [id_to_state[c] for c in uemp_states.columns]


# In[271]:


# Plot states unemployment rate
px.line(uemp_states)


# ## Pull each states unemployment data from May 2020

# In[194]:


ax = uemp_states.loc[uemp_states.index == '2020-05-01'].T \
.sort_values('2020-05-01') \
.plot(kind='barh', figsize=(8,12), width = 0.7, edgecolor='black',
      title='Unemployment Rate by State, May 2020')

ax.legend().remove()
plt.show()


# ## Pull participation rate

# In[277]:


part_df = fred.search('participation rate state',filter=('frequency', 'Monthly'))
part_df = part_df.query('seasonal_adjustment == "Seasonally Adjusted" and units == "Percent"')
part_df = part_df[part_df['id'].str.len() == 7]


# In[278]:


part_id_to_state = part_df['title'].str.replace('Labor Force Participation Rate for ','').to_dict()

all_results = []

for myid in part_df.index:
    results = fred.get_series (myid)
    results = results. to_frame (name=myid)
    all_results. append (results)
part_states = pd.concat(all_results, axis=1)
part_states.columns = [part_id_to_state[c] for c in part_states.columns]
part_states = part_states.drop(['Labor Force Participation Rate'],axis=1)


# In[279]:


part_states = part_states.dropna()


# # 5. Plot the Unemployment versus the Participation Rate 

# In[280]:


# Fix DC
uemp_states = uemp_states.rename(columns={'the District of Columbia':'District Of Columbia'})


# In[291]:


fig, axs = plt.subplots(10, 5, figsize=(30, 30), sharex=True)
axs = axs.flatten()

i = 0
for state in uemp_states.columns:
    if state in ["District Of Columbia","Puerto Rico"]:
        continue
    ax2 = axs[i].twinx()
    uemp_states.query('index >= 2020 and index < 2024')[state] \
        .plot(ax=axs[i], label='Unemployment')
    part_states.query('index >= 2020 and index < 2024')[state] \
        .plot(ax=ax2, label='Participation', color=color_pal[1])
    ax2.grid(False)
    axs[i].set_title(state)
    i += 1
plt.tight_layout()
plt.show()


# In[293]:


state = 'California'
fig, ax = plt.subplots(figsize=(10, 5), sharex=True)
ax2 = ax.twinx()
uemp_states2 = uemp_states.asfreq('MS')
l1 = uemp_states2.query('index >= 2020 and index < 2024')[state] \
    .plot(ax=ax, label='Unemployment')
l2 = part_states.dropna().query('index >= 2020 and index < 2024')[state] \
    .plot(ax=ax2, label='Participation', color=color_pal[1])
ax2.grid(False)
ax.set_title(state)
fig.legend(labels=['Unemployment','Participation'])
plt.show()


# In[ ]:




