# Ben Haws,
# DATA51100 Fall 2021
# Programming Assignment 6 Visualizing PUMS Data
# 10/7/2021

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main():

    # Get data from .csv (assumed to be in working directory)
    pums = pd.read_csv(r'ss13hil.csv', usecols=('HHL', 'HINCP', 'VEH', 'WGTP', 'TAXP', 'VALP'))

    # define figure and subplots
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
    language.set_ylabel('HHL')
    lang_counts = pums['HHL'].value_counts(normalize=True)
    langs = ['English Only', 'Spanish', 'Other Indo-European',
             'Asian and Pacific Island Languages', 'Other']
    lang_counts.index = langs
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
    language.pie(lang_counts, colors=colors, startangle=250)
    coordinates = (-0.5, 0.60, 0.5, 0.5)
    # Note: These coordinates intended to work with fullscreen figure
    language.legend(labels=langs, loc='best', bbox_to_anchor=coordinates)

    # Generate histogram for Household Income
    income.set_xlabel('Household Income($)-Log Scaled')
    income.set_ylabel('Density')
    income_data = pums['HINCP'].dropna()
    bins = np.logspace(1, 7, num=100)
    color = 'mediumseagreen'
    income.hist(income_data, bins=bins, color=color, density=True)
    sns.kdeplot(data=income_data, ax=income, linestyle='--', color='k')
    income.set_xscale('log')

    # Generate bar chart of households by number of vehicles available
    veh_avai = pd.DataFrame(pums['VEH'].dropna())
    veh_avai = veh_avai.join(pums['WGTP'])
    veh_avai = veh_avai.groupby(veh_avai['VEH']).sum().divide(1000)
    veh = veh_avai.index
    count = veh_avai['WGTP']
    vehicles.bar(veh, count, color='r')

    # Generate scatter plot for property tax vs value with colorbar
    # IMPORTANT: Expects an additional .csv file where each tax code
    # number is matched to its tax range (cols named Code and Tax)
    # as this data is not present in our data set
    # the .csv file can be created by copying the numeric info under
    # TAXP in the data dictionary, converting '.' to ',' and stripping $ and +
    conversion = pd.read_csv('conversion.csv')
    conversion[['max', 'min']] = conversion['Tax'].str.split('-', expand=True)

    vis.savefig('pums.png')
    vis.show()
    return


if __name__ == '__main__':
    main()
