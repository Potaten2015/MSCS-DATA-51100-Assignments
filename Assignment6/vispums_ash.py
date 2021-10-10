print("Group 3: Ben Haws, Taten Knight, Ashwini Rao")
print("Data Preperations and Statistics")
print("Progrramming Assignment 5")
print("DATA51100 Fall 2021")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#To read the required data from CSV file
data = pd.read_csv(r'ss13hil.csv', usecols=('HHL', 'HINCP', 'VEH', 'WGTP', 'TAXP', 'VALP'))

df_hhl = data.HHL.value_counts().reset_index()

#To Set titles and index for Languages
names_dict =

df_hhl['names'] = df_hhl['index'].map(names_dict)

#To Set titles and index for Vehicles
df_veh = data.groupby(['VEH']).agg({'WGTP':'sum'}).reset_index()#.hist()

df_veh['WGTP'] = round(df_veh['WGTP']/1000, 0)

#To get pie chart for Household Languauges
fig, axs = plt.subplots(2, 2, figsize=(20, 14))
axs[0,0].pie(df_hhl['HHL'], labels=df_hhl['names'], #autopct='%1.1f%%',
       labeldistance=None, startangle=240)
axs[0,0].legend(loc='upper left')
axs[0,0].set_title(label='Household Languages')
axs[0,0].set_ylabel(ylabel='HHL')

#To get bar chart for Household Vehicles
axs[1,0].bar(df_veh['VEH'],df_veh['WGTP'], color='red')
axs[1,0].set_title(label='Vehicles Available in Households')
axs[1,0].set_ylabel(ylabel='Thousands of Households')
axs[1,0].set_xlabel(xlabel='# of Vehicles')
plt.plot()