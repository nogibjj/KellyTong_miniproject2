# IDS 706 Mini Project 2

This repository is for IDS706 mini project week 2. 



## Purpose 
    This repository is created from the template established in week 1. It is set up based on the template's environment. This repository incorporates "pandas" to develop statistical functions. Specifically, the author uses pd.dataframe() to set up a dataset. Then it is tested on the count, mean, max, and min. 

## Things includes are:
    * Makefile
    * Dockerfile
    * Main
    * test_main
    * README
    * requiremets

[![CI](https://github.com/Kelly0604/IDS706/actions/workflows/CI.yml/badge.svg)](https://github.com/Kelly0604/IDS706/actions/workflows/CI.yml)

## The Building Process

`make install`
The building process starts with installing the packages. 
**Make install** calls the command pip install --upgrade pip &&\pip install -r requirements.txt

`make link`
**Make lint** calls the command pylint --disable=R,C --ignore-patterns=test_.*?py *.py
<img width="457" alt="make lint" src="https://github.com/Kelly0604/miniproject2/assets/142815940/39a19764-a6cc-4eaa-977f-7433b8915dad">

`make test`
**Make test** calls the command python -m pytest -vv --cov=main test_*.py
<img width="578" alt="make test" src="https://github.com/Kelly0604/miniproject2/assets/142815940/5b52b741-bea4-4328-8eca-29a43e91d94b">

`make format`
**Make format** calls the command black *.py

<img width="299" alt="make format" src="https://github.com/Kelly0604/miniproject2/assets/142815940/41df08ca-d8f7-4b62-b88b-1f39f1a7d858">

