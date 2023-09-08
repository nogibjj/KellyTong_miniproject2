import pandas as pd

def desrcibe_dataframe():
    data = {'height': [170,175,160,180,190]
    }
    dataframe = pd.DataFrame(data)
    return dataframe.describe()
