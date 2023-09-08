import pandas as pd

def desrcibe_dataframe():
    x = {heihgt:[170,175,160,180,190,185,180, 155]}
    dataframe = pd.dataframe(x)
    result = dataframe.describe()
    return result

def absolute_dataframe():
    x = {money:[100,200,-100,-200,300,-100000]}
    dataframe = pd.dataframe()
    value = dataframe.abs(x)
    return value