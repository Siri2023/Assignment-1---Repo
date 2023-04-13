#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns

def create_scatterplot(data, x_col, y_col, title):
    """
    Creates a scatter plot for the given dataset using Matplotlib and Seaborn.
    
    Parameters:
        - data (pandas.DataFrame): The dataset to use for creating the scatter plot.
        - x_col (str): The name of the column to use for the x-axis.
        - y_col (str): The name of the column to use for the y-axis.
        - title (str): The title to use for the scatter plot.
    """
    # Set the style of the plot
    sns.set(style="ticks")

    # Create the scatter plot using Matplotlib and Seaborn
    sns.scatterplot(x=x_col, y=y_col, data=data)

    # Set the title of the plot
    plt.title(title)

    # Show the plot
    plt.show()


# In[ ]:






# In[ ]:




