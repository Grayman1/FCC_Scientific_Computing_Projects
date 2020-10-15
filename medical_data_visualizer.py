# NOTE: You Must Install Matplotlib library version 3.1.3 or
# 3.2.2 to run correctly. Version 3.3.0 will generate an error. 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
overweight = (df['weight']/((df['height']/100)**2)>25).astype(int)
df['overweight'] = overweight

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
#medical_dict = { 1: 0, 2 : 1, 3: 1}
#df['cholesterol'] = df['cholesterol'].map( medical_dict )
#df['gluc'] = df['gluc'].map( medical_dict ) 
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
#print(df['cholesterol'])
df['gluc'] = (df['gluc'] > 1).astype(int)
#print(df['gluc'])

# Draw Cat Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = df.melt(id_vars= 'cardio',value_vars=['cholesterol', 'gluc', 'smoke' , 'alco' , 'active' , 'overweight'])

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
  df_cat = pd.DataFrame(df_cat.groupby(['variable', 'value', 'cardio'])['value'].count()).rename(columns={'value': 'total'}).reset_index()

  # Set up the matplotlib figure and draw the catplot
  g = sns.catplot(x='variable', y='total',
              hue='value', 
              col='cardio', data=df_cat, kind='bar')
  fig = g.fig
  fig.savefig('catplot.png')
  return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df ['ap_hi']) &
            (df['height'] >= df['height'].quantile(0.025)) & 
            (df['height'] <= df['height'].quantile(0.975)) &
            (df['weight'] >= df['weight'].quantile(0.025)) &
            (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    # Alternate mask generator
    #mask = np.triu(np.ones_like(corr, dtype=bool))
    # Alternate mask generator
    #mask = np.zeros_like(corr, dtype=np.bool)
    #mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    #sns.axes_style("white")
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    """sns.heatmap(corr, mask=mask, annot=True, fmt='.1f',  vmax=.3, center=0,
              square=True, linewidths=.5, cbar_kws={"shrink": .5})"""

    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f',  vmax=0.3, vmin=-0.15, center=0, linewidths=0.5,axes=ax, square=True, cbar_kws={"shrink": .5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig