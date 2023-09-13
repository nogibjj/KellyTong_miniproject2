import pandas as pd
import matplotlib.pyplot as plt

def marital():
    df=pd.read_csv("gss.csv")
    print(df.shape)
    print(df.describe())
    df.plot(x='Age', y='Marital', kind = 'Scatter', title="Correlation between Age and Marital Stage")
    plt.savefig('Age_Marital.png')
    
def desrcibe_dataframe():
    data = {'height': [170,175,160,180,190]
    }
    dataframe = pd.DataFrame(data)
    return dataframe.describe()
