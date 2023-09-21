
from mylib.lib import *

import pandas as pd

df = pd.read_csv("BQ_data.csv")
json_case = df["totals"][0]
answer = {
    "visits": "1",
    "hits": "1",
    "pageviews": "1",
    "timeOnSite": None,
    "bounces": "1",
    "transactions": None,
    "transactionRevenue": None,
    "newVisits": "1",
    "screenviews": None,
    "uniqueScreenviews": None,
    "timeOnScreen": None,
    "totalTransactionRevenue": None,
    "sessionQualityDim": "1",
}
revenue = pd.read_excel(
    "Analytics 1 Master View Sales Performance 20230501-20230630.xlsx",
    sheet_name="Dataset1",
)


def test_main():
    assert unpack_json(json_case, "totals") == answer
    ## asserting stats functions
    assert mean(revenue["Revenue"]) == revenue["Revenue"].mean()
    assert median(revenue["Revenue"]) == revenue["Revenue"].median()


test_main()
