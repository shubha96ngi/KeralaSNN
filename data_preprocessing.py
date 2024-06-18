import pandas as pd
import numpy as np

def data_preprocessing(filename):
    # Load data from Excel file
    whole_data = pd.read_excel(filename).values
    
    # Extract features (endeffector_coor) and labels (motor)
    endeffector_coor = whole_data[:, :-1]
    motor = whole_data[:, -1]
    
    # Perform 66% train-test split
    P = np.random.permutation(len(motor))
    train_size = round(0.66 * len(motor))
    
    traindata = endeffector_coor[P[:train_size], :]
    trainout = motor[P[:train_size]]
    testdata = endeffector_coor[P[train_size:], :]
    testout = motor[P[train_size:]]
    
    return traindata, trainout, testdata, testout
