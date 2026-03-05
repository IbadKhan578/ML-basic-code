# import seaborn as sns
# import matplotlib.pyplot as plt


# #    scatter and lineplot fell under the category of relational plots

# tips= sns.load_dataset('tips')
# print(tips)
# # sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')   #--> axis level function
# # hue--> it septates data into groups and each group gets a different color (male n female here )

# # sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter', hue='sex') # --> figure level


# # plt.show();



# # line plot --> we prefer it if the one parameter is about time 

# # sns.lineplot(data=tips, x='total_bill',y='tip')
# # plt.show();

# # fecet plot --> by using it we can make multiple plot from  a single column acc to category
# # (facet function works only on figure level function)
# sns.relplot(data=tips,kind='scatter', x='total_bill',y='tip', col='sex') 
# plt.show()