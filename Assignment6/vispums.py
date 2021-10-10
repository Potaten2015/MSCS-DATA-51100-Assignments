"""
Ben Haws, Ashwini Anand Rao, Taten Knight
2021.10.10
DATA 51100 - Statistical Programming
Fall 2021
Programming Assignment 6 Visualizing PUMS Data
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pprint import pprint


# Ben - This code is really clean. Always impressed by the how clear things are. -Taten
def main():
    # Get data from .csv (assumed to be in working directory)
    # Ashwini - usecols is really cool. Never seen it used before -Taten
    pums = pd.read_csv(r'ss13hil.csv', usecols=('HHL', 'HINCP', 'VEH', 'WGTP', 'TAXP', 'VALP', 'MRGP'))

    # Define figure and subplots
    vis = plt.figure(tight_layout=True, figsize=(11.7, 8), dpi=200)
    language = vis.add_subplot(2, 2, 1)
    income = vis.add_subplot(2, 2, 2)
    vehicles = vis.add_subplot(2, 2, 3)
    tax = vis.add_subplot(2, 2, 4)

    # Set titles for each subplot
    language.set_title('Household Languages')
    income.set_title('Distribution of Household Income')
    vehicles.set_title('Vehicles Available in Households')
    tax.set_title('Property Taxes vs Property Values')

    # Generate pie chart for Household Languages
    language.set_ylabel('HHL', labelpad=90)
    lang_counts = pums['HHL'].value_counts(normalize=True)
    langs = {1: 'English only',
             2: 'Spanish',
             3: 'Other Indo-European languages',
             4: 'Asian and Pacific Island languages',
             5: 'Other'}
    lang_counts.index = langs
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
    language.pie(lang_counts, colors=colors, startangle=242)
    coordinates = (-0.5, .5, 0.5, 0.5)
    # Note: These coordinates intended to work with fullscreen figure
    language.legend(labels=langs.values(), loc='upper left', bbox_to_anchor=coordinates)

    # Generate histogram for Household Income
    income.set_xlabel('Household Income($)-Log Scaled')
    income.set_ylabel('Density')
    income.ticklabel_format(useOffset=False, style='plain')
    income_data = pums['HINCP'].dropna()
    bins = np.logspace(1, 7, num=100)
    color = 'mediumseagreen'
    income.hist(income_data, bins=bins, color=color, density=True)
    income_data.plot.kde(ax=income, linestyle='--', color='k')
    income.set_xscale('log')
    income.grid(linestyle=':')


    # Generate bar chart of households by number of vehicles available
    veh_avai = pd.DataFrame(pums['VEH'].dropna())
    veh_avai = veh_avai.join(pums['WGTP'])
    veh_avai = veh_avai.groupby(veh_avai['VEH']).sum().divide(1000)
    veh = veh_avai.index
    count = veh_avai['WGTP']
    vehicles.bar(veh, count, color='r')
    vehicles.set_ylabel('Thousands of Households')

    # Generate scatter plot for property tax vs value with colorbar
    # IMPORTANT: Expects an additional .csv file where each tax code
    # number is matched to its tax range (cols named Code and Tax)
    # as this data is not present in our data set
    # the .csv file can be created by copying the numeric info under
    # TAXP in the data dictionary, converting '.' to ',' and stripping $ and +
    conversion = pd.read_csv('conversion.csv')
    conversion[['max', 'min']] = conversion['Tax'].str.split('-', expand=True).astype(float)
    mins = conversion['min'].to_dict()
    taxp = pums['TAXP'].map(mins)
    wgtp = pums['WGTP']
    valp = pums['VALP']
    mrgp = pums['MRGP']

    taxp_not_na = taxp.notna()
    valp_not_na = valp.notna()
    not_na = taxp_not_na.multiply(valp_not_na)
    taxp = taxp[not_na]
    wgtp = wgtp[not_na] / 5
    valp = valp[not_na]
    mrgp = mrgp[not_na]

    tax.set_xlabel('Property Value($)')
    tax.set_ylabel('Taxes($)')
    tax.set_xlim([0, 1200000])
    tax.set_ylim([0, 11000])
    tax.scatter(valp, taxp, c=mrgp, cmap='coolwarm', s=wgtp, marker='o', alpha=.4)
    tax.ticklabel_format(useOffset=False, style='plain')
    tax_cbar = vis.colorbar(mappable=plt.cm.ScalarMappable(cmap='coolwarm'), ax=tax,
                            label='First Mortgage Payment (Monthly $)')
    tax_cbar.ax.set_yticklabels(np.linspace(0, 5000, 6).astype(int))

    # Save the final figure
    vis.savefig('pums.png')
    return


if __name__ == '__main__':
    main()
