
# Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for 
# drawing attractive and informative statistical graphics. Seaborn is built on top of matplotlib and integrates closely 
# with pandas data structures, making it easy to create complex visualizations with just a few lines of code.
# Seaborn provides a variety of functions for creating different types of plots, including:
# 1. **Relational Plots**: These include scatter plots, line plots, and more, which are used to visualize relationships between variables.
# 2. **Categorical Plots**: These include bar plots, box plots, violin plots, and more, which are used to visualize the distribution of data across different categories.
# 3. **Distribution Plots**: These include histograms, KDE plots, and more, which are used to visualize the distribution of a single variable.
# 4. **Matrix Plots**: These include heatmaps and cluster maps, which are used to visualize data in a matrix format.
# 5. **Regression Plots**: These include linear regression plots and more, which are used to visualize the relationship between two variables along with a regression line.
# Seaborn also provides functions for customizing the appearance of plots, such as setting color palettes, 
# adjusting plot aesthetics, and adding annotations. It is widely used in data analysis and machine learning for exploratory data analysis and visualization.

# To use Seaborn, you can install it using pip:
# ```
# pip install seaborn
# ```

# Here is a simple example of how to use Seaborn to create a scatter plot:
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
import numpy as np

# Load an example dataset
tips = sns.load_dataset("tips")
# Create a scatter plot of total bill vs. tip
sns.scatterplot(x="total_bill", y="tip", data=tips)
#plt.show()
#===========================================================
# In this example, we load the "tips" dataset, which contains information about restaurant tips. We then create a scatter plot to visualize the relationship between the total bill and the tip amount. 
# Seaborn makes it easy to create such plots with just a few lines of code.

# Seaborn also provides a high-level interface for creating more complex visualizations, such as pair plots, which show relationships between multiple variables in a dataset:
# Create a pair plot of the tips dataset
sns.pairplot(tips)
#plt.show()
#===========================================================
# Load in data
iris_ = pd.read_csv("data/iris.csv")
print(iris_.head())

# Load the data
iris = sns.load_dataset("iris")
print(iris.head())
#===========================================================
sns.pairplot(iris, hue="species")
#plt.show()
#===========================================================
# Create violinplot
sns.violinplot(x = "sepal_length", data=iris)
#plt.show()

#===========================================================
## How To Use Seaborn’s Colors As A colormap in Matplotlib?
# Number of samples
N = 100

# Construct the colormap
plt.figure("Colormap Plot")
palette = sns.color_palette("muted", n_colors=5)
cmap = ListedColormap(sns.color_palette(palette).as_hex())# hexadecimal casting

# Initialize the data
x1 = np.random.randn(N)
x2 = np.random.randn(N)
# Assume that there are 5 possible labels
colors = np.random.randint(0,5,N)

# Create a scatter plot
plt.scatter(x1, x2, c=colors, cmap=cmap)

# Add a color bar
plt.colorbar()

# Show the plot
#plt.show()
#===========================================================
# example for categorical plot
plt.figure("Categorical Plot")
g = sns.catplot(x="species", y="petal_length", data=iris, kind="bar", height=4, aspect=2, hue="species", palette="muted", legend=False)

#plt.show()
#===========================================================
# example for matrix plot
plt.figure("Matrix Plot")
data = np.random.rand(10,4)
rows = list('0123456789')
cols = list('WXYZ')
plt.pcolor(data,cmap=plt.cm.Oranges_r,edgecolors='k')
plt.xticks(np.arange(0,4)+0.5,cols)
plt.yticks(np.arange(0,10)+0.5,rows)
#plt.show()
#===========================================================
# example for distribution plot
plt.figure("Distribution Plot")
x = np.random.sample(100)
n, bins, patches = plt.hist(x, bins=20, facecolor='blue', alpha=0.80, density=True)
plt.setp(patches[1], 'facecolor', 'b')
plt.xlabel('bins')
plt.ylabel('Values')
#plt.show()
#===========================================================
# example for Regression plot
plt.figure("Regression Plot")
sns.lmplot(x="total_bill", y="tip", data=tips)  
plt.show()
#===========================================================
