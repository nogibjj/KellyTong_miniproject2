import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def age():
    df=pd.read_csv("gss.csv")
    print(df.shape)
    print(df.describe())
    plot = sns.histplot(df["age"], kde=True, color="blue", label="Age")
    plot.legend()
    plt.show()
    plt.savefig("congress.png")
    
def desrcibe_dataframe():
    data = {'height': [170,175,160,180,190]
    }
    dataframe = pd.DataFrame(data)
    return dataframe.describe()
