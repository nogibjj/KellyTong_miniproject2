import pandas as pd

def desrcibe_dataframe():
    data = {'height': [170,175,160,180,190,185]
    }
    dataframe = pd.DataFrame(data)
    return dataframe.describe()

#def absolute_dataframe():
   # x = {'money':[100,200,-100,-200,300,-100000]}
   # dataframe = pd.DataFrame()
   # value = dataframe.abs(x)
    #return value