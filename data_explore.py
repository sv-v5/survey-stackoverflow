import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pandas_profiling import ProfileReport

plt.rcParams.update({'font.size': 16})

# load data with pandas
df = pd.read_csv('data/survey_results_public.csv')    # [4999 rows x 61 columns]
# exclude variable 'Respondent'
df = df.drop(['Respondent'], axis=1)


def profiling_report():
    """
    run pandas profiling, generate and save the report
    """
    # Maximum allowed size exceeded for default dataset. set minimal=True
    profile = ProfileReport(df, title="Pandas Profiling Report", minimal=True)
    profile.to_file("index.html")


def sns_pairplot():
    """
    seaborn pairplot and save figure
    """
    # keep a selection of the columns/variables
    keep = ["Hobbyist", "Age", "Age1stCode", "WorkWeekHrs", "YearsCode"]  # "YearsCodePro"
    dfkeep = df[keep]
    # drop rows that have NaN.  4999 rows --> 3k rows
    dfkeep = dfkeep.dropna(axis=0)

    # convert data types to numerical, remove rows with difficult categorical values
    dfkeep["Hobbyist"] = dfkeep["Hobbyist"].map({"Yes": 1, "No": 0})

    # keep rows that are within +/-3 standard deviations
    dfkeep = dfkeep[np.abs(dfkeep.WorkWeekHrs - dfkeep.WorkWeekHrs.mean()) <= (3*dfkeep.WorkWeekHrs.std())]

    dfkeep = dfkeep[~dfkeep.Age1stCode.str.contains("than ") ]    # than  * years
    dfkeep = dfkeep[~dfkeep.YearsCode.str.contains("than ") ]    # than  * years
    # dfkeep = dfkeep[~dfkeep.YearsCodePro.str.contains("than ") ]    # than  * years
    
    # TODO: can use pd.apply() here.  df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric)
    dfkeep["Age1stCode"] = pd.to_numeric(dfkeep["YearsCode"])
    dfkeep["YearsCode"] = pd.to_numeric(dfkeep["YearsCode"])
    # dfkeep["YearsCodePro"] = pd.to_numeric(dfkeep["YearsCodePro"])
    
    # view variable pairs and color code by "Hobbyist" var
    pair = sns.pairplot(dfkeep, hue="Hobbyist")

    pair.fig.set_figheight(12)
    pair.fig.set_figwidth(17)
    # plt.show()

    plt.savefig("images/pairplot.jpg", dpi=150)


profiling_report()
sns_pairplot()
