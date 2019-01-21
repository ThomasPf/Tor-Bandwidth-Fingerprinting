import re
from os import listdir
from os import path as pt
from os.path import isfile, join

import matplotlib.pyplot as plt
import pandas as pd

mypath = "/Users/Pfann/Desktop/Computer_science/Tor-Bandwidth-Fingerprinting/extracted/"
dataframes = []
onlyfiles_len = 0


# start with this method if you want to give your own path
def get_files_from_path(path: str, window_size: int):
    mypath = path
    get_files_from_my_path(window_size)


# Default start method
def get_files_from_my_path(window_size: int):
    if not pt.isdir(mypath):
        print('no such directory')
        exit(1)
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and not f.startswith('.')]
    onlyfiles_len = len(onlyfiles)
    if onlyfiles_len == 0:
        print("no files in folder, exiting now")
        exit(1)
    get_dfs_from_path(onlyfiles)
    df_merged = dataframes[0]
    # rename columns and merge. Drop timestamp after
    for i in range(len(dataframes)):
        print(dataframes[i].columns)
        dataframes[i].columns = ['timestamp', 'value_' + str(i)]
    for i in range(1, len(dataframes)):
        df_merged = pd.merge(df_merged, dataframes[i], on='timestamp')

    df_merged = df_merged.drop('timestamp', 1)

    df_merged_rolling = df_merged.rolling(window=window_size)

    correlations = (df_merged_rolling['value_0'].corr(df_merged_rolling['value_1']))
    columns = len(correlations.columns)
    fig = plt.figure()
    axes = [plt.subplot2grid((columns - 1, 1), (0, 0))]

    # 1 is always the probe
    for i in range(0, columns - 1):
        axes.append(plt.subplot2grid((columns - 1, 1), (i, 0), sharex=axes[0]))

    # 1 is always the probe
    for i in range(1, columns):
        correlations['value_' + str(i)].plot(ax=axes[i], label="value_" + str(i))

    plt.show()
    fig.savefig("example1.pdf", bbox_inches='tight')


def get_dfs_from_path(onlyfiles: list):
    # maybe add a special name to the probe file name, but for now this works.
    regex = re.compile(".*(probe).*")
    probe = [m.group(0) for l in onlyfiles for m in [regex.search(l)] if m]

    if len(probe) == 1:
        dataframes.append(pd.read_csv(mypath + probe[0]))
        onlyfiles.remove(probe[0])
    elif len(probe) > 1:
        print('too many files named probe, please make sure only one is in ' + mypath)
        exit(1)
    elif len(probe) == 0:
        print('no probe file in ' + mypath + ' found. Comparing all to the first file in the path')
    print(onlyfiles)
    for file in onlyfiles:
        dataframes.append(pd.read_csv(mypath + file))


get_files_from_my_path(250)
