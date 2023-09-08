#this is for testing functions in main.py

from main import desrcibe_dataframe


def test_describe():
   # "testing the desrcibe_dataframe function in main.py"
    describe = desrcibe_dataframe()
    assert describe.loc['count'][0]== 6.0
   # assert describe.loc['mean'][0] == 174.375
   # assert describe.loc['min'] == 155.0
   # assert describe.loc['max'] == 190.0

#def test_absolute():
  #  "testing the absolute_dataframe function in main.py"
   # absolute = absolute_dataframe()
   # assert absolute == [100,200,100,200,300,100000]