from python_script import make_whole_df
import pandas as pd
df = pd.read_csv('BQ_data.csv')
def test_main():
   assert make_whole_df(df).iloc[0,1] == 1501591568


test_main()
