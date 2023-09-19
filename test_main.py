#this is for testing functions in main.py
import pandas as pd
from main import describe, age, generate_general_markdown



def test_age():
   data = pd.read_csv("gss.csv")
   age(data)

def test_describe():
   data = pd.read_csv("gss.csv")
   describe(data)

def test_md():
   data = pd.read_csv("gss.csv")
   generate_general_markdown(data)

#def test_describe():
   # "testing the desrcibe_dataframe function in main.py"
    #describe = desrcibe_dataframe()
    #assert describe.loc['count'][0]== 5.0
    #assert describe.loc['mean'][0] == 175.0
    #assert describe.loc['min'][0] == 160.0
    #assert describe.loc['max'][0] == 190.0
