# Google Analytics BQ import and transactions analysis

## Purpose of the analysis

This project looks at export of data from Big Query and Google Analytics for their visitor and transactions data. Many companies are using Google Analytics to analyze their Ecommerce websites as well as UX. This project aim to build two simple scripts that provide a solution to deal with a BQ GA export that uses a complicated data format - the python_script.py using custom developed function in mylib/lib.py proposes a short pipeline to unpack BQ data. Main1.ipynb file then utilizes this pipeline to construct a new dataset. Then we proposa a function to compare two revenue/transactions distribution and compare them with each other using usual GA data.

## Repo files

This repo contains of : 

* Devcontainer with Dockerfile and devcontainer.json
* mylib with _init_.py file and lib.py file where all of the commonly used functions are stored and imported from
* Two datasets BQ_data.csv for the first part of the code, and  Analytics 1 Master View Sales Performance 20230501-20230630.xlsx - Transaction Data from Google Analytics.
* Makefile with make actions to utilize via workflows
* python_script.py -- build an overall function to transform BQ data and utilizes the function.
* test_script.py - test file for the python_script
* test_lib.py - test script for lib functions
* main1.ipynb - notebook utilizing function from both lib and script files. Main report also lives within ipynb file. 
* requirements.txt - has all the needed libraries.
* updated_BQ.csv - automatically generated updated BQ dataframe downloaded into the repo.

## Github actions 
* Overall workflow run (contains main components running in order) - [![Python CI](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/main.yml)
* [![Install](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/install.yml) - package installing
* [![Format](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/Format.yml/badge.svg)](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/Format.yml) - code formatting
* [![Lint](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/Lint.yml/badge.svg)](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/Lint.yml) - Lint
* [![Test](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/Test.yml/badge.svg)](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/Test.yml) - testing code including testing all py scripts and ipynb file via nbval ext.
* [![add_commit_push](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/add_commit_push.yml/badge.svg)](https://github.com/nogibjj/as1466-Individual-Project-1/actions/workflows/add_commit_push.yml) - updating repo with new dataframes. 

