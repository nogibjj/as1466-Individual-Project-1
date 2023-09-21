import pandas as pd
from mylib.lib import unpack_json, merge_dfs
'''
Python script ties json functions 
from the lib library and creates new df that will be 
better used in jupyter notebook that will 
perform vizualization analytics
'''
def make_whole_df(df):
  '''
  This function wraps up json unpacking, creates updated df and writes new csv file
  '''
  df = df[['visitId','visitStartTime','date','totals','device',
           'channelGrouping','fullVisitorId']]
    #adding totals data
  # Create an empty list to store column names and data
  columns = []
  data_list = []
  json_column = 'totals'
  column_name = 'totals'

  # Iterate over each row and unpack the JSON data
  for index, row in df.iterrows():
      unpacked_data = unpack_json(row[json_column], column_name)
      data_list.append(unpacked_data)

      # Collect unique keys from the first row's JSON
      if index == 0:
          columns.extend(unpacked_data.keys())

  # Create a DataFrame from the data list
  unpacked_df = pd.DataFrame(data_list)

  # Reorder columns to match the order in which they were encountered
  unpacked_df = unpacked_df[columns]
  df = merge_dfs(df, unpacked_df)
    #adding totals data
  # Create an empty list to store column names and data
  columns = []
  data_list = []
  json_column = 'device'
  column_name = 'device'

  # Iterate over each row and unpack the JSON data
  for index, row in df.iterrows():
      unpacked_data = unpack_json(row[json_column], column_name)
      data_list.append(unpacked_data)

      # Collect unique keys from the first row's JSON
      if index == 0:
          columns.extend(unpacked_data.keys())

  # Create a DataFrame from the data list
  unpacked_df = pd.DataFrame(data_list)

  # Reorder columns to match the order in which they were encountered
  unpacked_df = unpacked_df[columns]
  df = merge_dfs(df, unpacked_df)
  return df

"""# Summary and basic statisticts"""

df = pd.read_csv('BQ_data.csv')
df.head(3)
df = df.iloc[:,:]

df  = make_whole_df(df)
df.to_csv('updated_BQ.csv')

