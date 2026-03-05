import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# price=[49000,54000,55000,52000,50000,46000];
# year=[2015,2016,2017,2018,2019,2020];

# # single plot 
# batsman = pd.read_csv('metplot\sharma-kohli.csv').squeeze('columns')
# # print(batsman)
# plt.plot(batsman['index'],batsman['V Kohli'])
# # plt.show()


# # plotting multiple plots 
# plt.plot(batsman['index'],batsman['V Kohli'],color='green')
# plt.plot(batsman['index'],batsman['RG Sharma'],color='yellow') # green n yellow are the line colors

# # label title 
# plt.title("Rohit Sharma vs virat kohli career comparison")
# # plt.show()
# # label x and y axies 
# plt.xlabel('Year')
# plt.ylabel('Score')
# # plt.show();

# # add marker in the plot 
# plt.plot(batsman['index'],batsman['V Kohli'],label='Virat',color='green',marker='o')
# plt.plot(batsman['index'],batsman['RG Sharma'],label='Rohit Sharma',color='yellow',marker='o') # green n yellow are the line colors

# # label title 
# plt.title("Rohit Sharma vs virat kohli career comparison")
# # plt.show()
# # label x and y axies 
# plt.xlabel('Year')
# plt.ylabel('Score')
# plt.legend() # to show the labels like v kohli and rohit 
# plt.grid()
# # plt.show() # to show the graph 




# Scatter plot
# x = np.linspace(-10,10,50)
# y= 10*x + 3 + np.random.randint(0,300,50)

# plt.scatter(x,y)   # scatter plot 
# # plt.show();



# plot scatter on panda data 
# batter = pd.read_csv('metplot/batter.csv').squeeze('columns');
# batter = batter.head(50);
# print(batter)
# plt.scatter(batter['avg'],batter['strike_rate'])
# plt.title("Avg and strike rate analysis  of top 50  batter ")
# plt.xlabel("avg")
# plt.ylabel("Strike rate")
# plt.show()


# bar chart 

# children = [10,20,15,17,25]
# color = ['red','green','yellow','blue','pink']

# plt.bar(color,children, width=0.7)   # x axies category , y axis number 
# # plt.barh(color,children)   to draw a horizontal bar 
# plt.show()

#Multiple bar charts

rec= pd.read_csv('metplot/batsman_season_record.csv');
# print(rec)
# x = np.arange(len(rec['batsman']))

# plt.bar(x- 0.2, rec['2015'], width=0.2);
# plt.bar(x,rec['2016'], width=0.2);
# plt.bar(x+ 0.2,rec['2017'], width=0.2);
# plt.xticks(x,rec['batsman']);     #What is xticks?
# # xticks controls what appears on the x-axis and where it appears.
# # tells matplotlib: Where to place labels on the x-axis What text to show at those places Syntax plt.xticks(positions, labels)
# plt.show()


# stacked bar chart

plt.bar(rec['batsman'], rec['2015'],label='2015')
plt.bar(rec['batsman'], rec['2016'], bottom=rec['2015'], label='2016')
plt.bar(rec['batsman'], rec['2017'], bottom=(rec['2015']+ rec['2016']), label='2017')
plt.legend();    # function to make the label visible 
plt.show()