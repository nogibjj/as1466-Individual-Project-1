import pandas as pd 
import json
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def unpack_json(json_str, column_name):
    '''
    Function unpacks json 
    '''
    try:
        json_data = json.loads(json_str.replace("'", "\""))
        return json_data[column_name]
    except json.JSONDecodeError:
        return {}



def make_df_json(json): 
  df = pd.DataFrame([json])
  return df

def merge_dfs(df1,df2): 
  '''
  return contecated df with unpacked json 
  '''
  df = pd.concat([df1, df2], axis=1)
  return df


def append_json(basic_df, column): 
  df1 = basic_df
  df2 = make_df_json(unpack_json(basic_df[column]),column)
  return merge_dfs(df1,df2)
  


#function to populate all descriptive statistics
def stats(df): 
  return df.describe()
#function  to return mean of a Series 
def mean(series):
  return series.mean()
#function to return median of Series 
def median(series): 
  return series.median()
#function to return standard deviation of statistics 
def std(series):
  return series.std()


#function to simulate more functions 

def simulate_rows(original_data,num_new_rows): 

  # Determine the number of additional rows you want to generate
  # Adjust this based on your needs

  # Initialize an empty list to store the augmented data
  augmented_data = []

  # Perform bootstrapping to generate new rows
  for _ in range(num_new_rows):
      # Randomly sample a row from the original dataset with replacement
      sampled_row = original_data.sample(n=1, replace=True)
      
      # You can optionally introduce some noise or variations to the sampled data if needed
      
      # Append the sampled row to the augmented data list
      augmented_data.append(sampled_row)

  # Concatenate the augmented data with the original dataset
  augmented_df = pd.concat([original_data] + augmented_data, ignore_index=True)
  return augmented_df

  # Now, 'augmented_df' contains your augmented dataset with more rows based on the original distribution.


## Data Analysis functions


def distribution_analytics(rev1,rev2, types):
  from scipy import stats

  '''

  Requires two distributions to compare

  Requires for data to be continious

  Required the data to be a series (not df)

  produces:

  1) Box plot

  2) CDF

  3) Histogram distribution

  + product two outputs for mann whitney and t test

  '''

  rev1 = rev1.astype(float)

  rev2 = rev2.astype(float)

  #defining the variable type

  if types == 'r':

    freq = 1000

    title = 'Revenue'

  elif types == 'q':

    freq = 1

    title = 'Quantity'

  elif types == 's':

    freq = 20

    title = 'Shipping costs'

  else:

    freq = 500

    title = 'Ref'

 

  #boxplot

  rev1_df = pd.DataFrame()

  rev2_df = pd.DataFrame()

 

  #rev1

  rev1_df['metric'] = rev1

  rev1_df['label'] = 'Group 1'

  rev1_df['id'] = np.arange(0,len(rev1))

 

 

  #rev2

  rev2_df['metric'] = rev2

  rev2_df['label'] = 'Group 2'

  rev2_df['id'] = np.arange(0,len(rev2))

 

  plot_df1 = pd.concat([rev1_df, rev2_df])

 

  fig1 = px.box(plot_df1, x="label", y="metric", points="all", title=title)

  fig1.show()

  plt.figure(figsize=(8, 6))
  sns.boxplot(data=plot_df1, x="label", y="metric")
  plt.title(title)
  plt.show()

 

  #CDF

  plot_df1['N_transactions'] = plot_df1.groupby('label')['id'].transform('nunique')

  cdf = plot_df1.groupby(['metric','N_transactions','label'])['id'].nunique().to_frame().reset_index()

  cdf['percent'] = cdf['id']/cdf['N_transactions']

  cdf['cumsum'] = cdf.groupby('label')['percent'].transform('cumsum')

  cdf = cdf.sort_values(['label','metric'])

  fig  = px.line(cdf, x= 'metric', y = 'cumsum', color = 'label',title=title)

  fig.show()
  plt.figure(figsize=(8, 6))
  sns.lineplot(data=cdf, x='metric', y='cumsum', hue='label')
  plt.title(title)
  plt.show()


  # PDF

 

  hist_data = [rev1, rev2]

 

  group_labels = ['Group1', 'Group2']

  fig = ff.create_distplot(hist_data, group_labels, bin_size=freq)

  fig.update_layout(title=title)

  fig.show()
    # Assuming hist_data is a list of NumPy arrays, group_labels is a list of labels,
  # and freq is the bin size
  fig, ax = plt.subplots(figsize=(8, 6))
  for data, label in zip(hist_data, group_labels):
        sns.histplot(data, label=label, bins=np.arange(0, max(data) + freq, freq), kde=True)

  plt.legend()
  plt.title(title)
  plt.xlabel("Values")
  plt.ylabel("Density")
  plt.show()

 

  #statistical tests

  print('T test results')

  k = rev2.mean() - rev1.mean()

  print(k/rev1.mean()*100,'%uplift of the average from group1')

  j = stats.ttest_ind(rev1, rev2, equal_var =False)

  print(stats.ttest_ind(rev1, rev2, equal_var =False))

  print((1-j.pvalue)*100,'% confidence')

  print('')

  print('Mann whitney results')

  k = (rev2.median() - rev1.median())/rev1.median()*100

  print('Uplift of the median value from group1 to group2:',k,'%')

  test = stats.mannwhitneyu(rev1, rev2)

  print(test)

  print((1-test.pvalue)*100,'% confidence')

 

  print(rev1.mean(),'Group 1 Average')

  print(rev2.mean(), 'Group 2 Average')

 

  print(rev1.median(), 'Group 1 Median')

  print(rev2.median(), 'Group 2 Median')


#weighted T-test
def weighted_tt(group1, group2): 
  from scipy import stats

  # Calculate the sample sizes
  n1 = len(group1)
  n2 = len(group2)

  # Calculate the means and variances for each group
  mean1 = np.mean(group1)
  mean2 = np.mean(group2)
  var1 = np.var(group1, ddof=1)  # Use ddof=1 for sample variance
  var2 = np.var(group2, ddof=1)

  # Calculate the pooled variance with weights
  pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)

  # Calculate the t-statistic with weights
  t_stat = (mean1 - mean2) / np.sqrt(pooled_var * (1 / n1 + 1 / n2))

  # Calculate degrees of freedom (use Welch-Satterthwaite equation)
  df = (pooled_var**2) / ((var1**2 / n1**2) / (n1 - 1) + (var2**2 / n2**2) / (n2 - 1))

  # Calculate the p-value
  p_value = 2 * (1 - stats.t.cdf(np.abs(t_stat), df))

  # Print the results
  print("T-statistic:", t_stat)
  print("Degrees of freedom:", df)
  print("P-value:", p_value)

  # Check if the result is statistically significant (e.g., with alpha=0.05)
  alpha = 0.05
  if p_value < alpha:
      print("The difference between the groups is statistically significant.")
  else:
      print("There is no statistically significant difference between the groups.")




   
