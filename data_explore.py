import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pandas_profiling import ProfileReport

plt.rcParams.update({'font.size': 14})

# load data with pandas
df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])


def profiling_report():
    """
    run pandas profiling, generate and save the report
    """
    profile = ProfileReport(df, title="Pandas Profiling Report")
    profile.to_file("index.html")


def sns_pairplot():
    """
    seaborn pairplot and save figure
    """
    pair = sns.pairplot(df)

    pair.fig.set_figheight(13)
    pair.fig.set_figwidth(13)

    # plt.show()

    plt.savefig("images/pairplot.png", dpi=100)


# profiling_report()
sns_pairplot()
