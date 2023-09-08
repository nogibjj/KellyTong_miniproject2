import pandas as pd

def create_dataframe():
    data = {'Name': ['Tom', 'Jack', 'nick', 'juli'],
        'marks': [99, 98, 95, 90]}
    dataframe = pd.DataFrame(data)
    dataframe


#def desrcibe_dataframe():
    #data = {'height': [170,175,160,180,190,185,180,155]
   # }
   # dataframe = pd.DataFrame(data)
   # return dataframe.describe()

#def absolute_dataframe():
   # x = {'money':[100,200,-100,-200,300,-100000]}
   # dataframe = pd.DataFrame()
   # value = dataframe.abs(x)
    #return value