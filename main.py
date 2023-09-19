import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def describe(data):
    df = pd.read_csv(csv)
    return df.describe()
    
def age(data):
    #df=pd.read_csv("gss.csv")
    #print(df.shape)
    #print(df.describe())
    plot = sns.histplot(df["age"], kde=True, color="blue")
    plt.title("Age Density Graph")
    plt.xlabel("Age")
    plt.ylabel("Count")
    #plot.legend()
    #plt.show()
    plt.savefig("age.png")

def generate_general_markdown(data):
    """generate an md file with outputs"""
    markdown_table = describe(data)
    markdown_table = str(markdown_table1)

    # Write the markdown table to a file
    with open("output.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table)
        file.write("\n\n")  # Add a new line
        file.write("![age](age.png)\n")
    
def desrcibe_dataframe():
    data = {'height': [170,175,160,180,190]
    }
    dataframe = pd.DataFrame(data)
    return dataframe.describe()
