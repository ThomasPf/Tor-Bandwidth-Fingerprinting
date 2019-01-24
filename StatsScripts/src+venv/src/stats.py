import re, getopt, sys
from os import listdir
from os import path as pt
from os.path import isfile, join, isdir

import matplotlib.pyplot as plt
import pandas as pd

mypath: str = "/Users/Pfann/Desktop/Computer_science/Tor-Bandwidth-Fingerprinting/extracted/"
base_path: str = "/Users/Pfann/Desktop/Computer_science/Tor-Bandwidth-Fingerprinting/extracted/"
dataframes = []
onlyfiles_len: int = 0
debug: bool = False
directories = []
multi_run: bool = False


# start with this method if you want to give your own path
def get_files_from_path_multiple_dir(window_size: int):
    global mypath
    multi_run: bool = True
    all_dirs_path = [f for f in listdir(base_path) if isdir(join(base_path, f)) and not f.startswith('.')]
    regex = re.compile(".*(setup).*")
    setups = [m.group(0) for l in all_dirs_path for m in [regex.search(l)] if m]
    for test in setups:
        mypath = base_path+test+'/'
        print('my_path: '+mypath)
        get_files_from_my_path(window_size, optional=test)


# Default start method
def get_files_from_my_path(window_size: int, **args):
    test_name = 'standard_test'
    print(args)
    if len(args) == 1:
        if 'optional' in args:
            print('test name: ', args['optional'])
            test_name = args['optional']
        else:
            print('no test name specified')
    elif len(args) > 1:
        print('incorrect optional arguments')
        exit(1)

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

    correlation_coefficient = df_merged.corr()
    print(correlation_coefficient)

    # below drops all 0 rows
    #df_merged = df_merged.loc[~(df_merged == 0).any(axis=1)]

    df_merged_rolling = df_merged.rolling(window=window_size, center=True, )

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
    fig.savefig("graph_"+test_name+"_windowsize"+str(window_size)+".pdf", bbox_inches='tight')


def get_dfs_from_path(onlyfiles: list):
    # maybe add a special name to the probe file name, but for now this works.
    regex = re.compile(".*(adversary).*")
    probe = [m.group(0) for l in onlyfiles for m in [regex.search(l)] if m]
    global dataframes
    dataframes = []
    if len(probe) == 1:
        dataframes.append(pd.read_csv(mypath + probe[0]))
        onlyfiles.remove(probe[0])
    elif len(probe) > 1:
        print('too many files named adversary, please make sure only one is in ' + mypath)
        exit(1)
    elif len(probe) == 0:
        print('no adversary file in ' + mypath + ' found. Comparing all to the first file in the path')
    print(onlyfiles)
    for file in onlyfiles:
        dataframes.append(pd.read_csv(mypath + file))


def main(argv):
    window_size = 200
    global mypath
    global base_path
    try:
        opts, args = getopt.getopt(argv, "hw:p:", ["path=", "window="])
        print(opts)
        print(args)
    except getopt.GetoptError:
        print('stats.py -p <path> -w <windowsize>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('stats.py -p <path> -w <windowsize>')
            sys.exit()
        elif opt in ("-p", "--path"):
            mypath = arg
            base_path = arg
        elif opt in ("-w", "--window"):
            window_size = int(arg)

        print('using path: '+base_path)
        print('using window_size: '+str(window_size))

        get_files_from_path_multiple_dir(window_size)


if __name__ == "__main__":
    main(sys.argv[1:])

# get_files_from_my_path(200)pi
#get_files_from_path_multiple_dir(500)
