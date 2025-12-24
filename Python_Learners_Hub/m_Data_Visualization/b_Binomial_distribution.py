from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

# sns.displot(random.normal(loc=50, scale = 5, size= 1000), kind='kde')
# sns.displot(random.binomial(n=100, p=0.5, size= 1000), kind='kde')
# plt.show()

# Generate data
normal_data = np.random.normal(loc=50, scale=5, size=1000)
binomial_data = np.random.binomial(n=100, p=0.5, size=1000)

# Plot both distributions on the same graph
sns.kdeplot(normal_data, label='Normal Distribution')
sns.kdeplot(binomial_data, label='Binomial Distribution')

# Add legend
plt.legend()
'''
the legend indicates which line represents the normal distribution and which line represents the binomial distribution. It helps viewers interpret the plot by providing a visual reference for the different distributions being displayed.
In data visualization, a legend is a key or guide that helps identify the elements of a plot. It typically consists of labels or symbols corresponding to different data series or categories present in the plot. Legends are especially useful when multiple datasets or types of data are represented in a single plot, as they provide clarity about what each element represents.
'''
# Show plot
plt.show()
