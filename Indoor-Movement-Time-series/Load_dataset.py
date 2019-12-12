# load user movement dataset into memory
import pandas as pd
from pandas import read_csv
from os import listdir
 
# return list of traces, and arrays for targets, groups and paths
def load_dataset(prefix=''):
    grps_dir, data_dir = prefix+'groups/', prefix+'dataset/'
    # load mapping files
    targets = read_csv(data_dir + 'MovementAAL_target.csv', header=0)
    groups = read_csv(grps_dir + 'MovementAAL_DatasetGroup.csv', header=0)
    paths = read_csv(grps_dir + 'MovementAAL_Paths.csv', header=0)
    # load traces
    sequences = list()
    target_mapping = None
    directory = '/home/supradha/Downloads/MovementAAL/dataset/'
    for name in listdir(directory):
        filename = directory +'/'+ name
        if filename.endswith('_target.csv'):
            continue
        df = read_csv(filename, header=0)
        values = df.values
        sequences.append(values)
    return sequences, targets.values[:,1], groups.values[:,1], paths.values[:,1]

#loading the data
sequence, target, group, path = load_dataset('MovementAAL/')
# summarize shape of the loaded data
print(len(sequence), target.shape, group.shape, path.shape)