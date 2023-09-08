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
**Make install** calls the command **pip install --upgrade pip &&\pip install -r requirements.txt**

`make link`
**Make lint** calls the command **pylint --disable=R,C --ignore-patterns=test_.*?py *.py**
[!Make Lint](./make lint.png)

`make test`
**Make test** calls the command **python -m pytest -vv --cov=main test_*.py**
[!Make Test](./make test.png)

`make format`
**Make format** calls the command **black *.py **
[!Make Format](./make format.png)
