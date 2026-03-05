import seaborn as sns
import matplotlib.pyplot as plt

# plots under distribution plots
# histplot
#kdplot
# rugplot

tips= sns.load_dataset('tips')
print(tips)
sns.histplot(x='total_bill',data=tips)   # we can also specify bins 
plt.show()


