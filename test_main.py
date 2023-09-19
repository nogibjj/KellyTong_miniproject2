#this is for testing functions in main.py
import panda as pd
from main import desrcibe_dataframe, describe, age, generate_general_markdown

data = pd.read_csv("gss.csv")

def test_age():
   age(data)

def test_describe():
   describe(data)

def test_md():
   generate_general_markdown(data)

def test_describe():
   # "testing the desrcibe_dataframe function in main.py"
    describe = desrcibe_dataframe()
    assert describe.loc['count'][0]== 5.0
    assert describe.loc['mean'][0] == 175.0
    assert describe.loc['min'][0] == 160.0
    assert describe.loc['max'][0] == 190.0
