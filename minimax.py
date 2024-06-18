import numpy as np

def minmax(data, newmax, newmin):
    arr = np.zeros_like(data)
    data_min = np.min(data, axis=0)
    data_max = np.max(data, axis=0)
    data_range = data_max - data_min
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            arr[i, j] = (data[i, j] - data_min[j]) / data_range[j]
            range2 = newmax - newmin
            arr[i, j] = arr[i, j] * range2 + newmin
    
    return arr
