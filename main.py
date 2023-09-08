import pandas as pd

def desrcibe_dataframe():
    x = {'height':[170,175,160,180,190,185,180, 155]}
    dataframe = pd.DataFrame(x)
    return dataframe.describe()

#def absolute_dataframe():
   # x = {'money':[100,200,-100,-200,300,-100000]}
   # dataframe = pd.DataFrame()
   # value = dataframe.abs(x)
    #return value