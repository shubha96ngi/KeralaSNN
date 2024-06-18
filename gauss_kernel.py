import numpy as np
from scipy.stats import norm
from scipy.signal import convolve2d

def gauss_kernel(inp_for_sys, cnt_MF):
    x = np.arange(-360, 360.1, 0.1)  # Equivalent to -360:0.1:360 in Matlab
    mf_spiketime = []

    # Normalizing the features using the minmax function
    inp_for_sys_norm = minmax(inp_for_sys, 255, 20)

    for loop_j in range(inp_for_sys_norm.shape[0]):
        stor_sum_val = []
        mf_spike = [[] for _ in range(inp_for_sys_norm.shape[1])]

        for i in range(inp_for_sys_norm.shape[1]):
            norm = norm.pdf(x, loc=inp_for_sys_norm[loop_j, i], scale=10)
            norm1 = convolve2d(norm.reshape(1, -1), inp_for_sys_norm[loop_j, i].reshape(1, 1), mode='same')
            norm1 = (norm1 - np.min(norm1)) / (np.max(norm1) - np.min(norm1))

            datapoints = np.zeros(cnt_MF)
            for j in range(cnt_MF):
                datapoints[j] = createneuron(inp_for_sys_norm[loop_j, i], cnt_MF)

            wt = (inp_for_sys_norm[loop_j, i] / 3) * len(datapoints)

            l_dp = np.isclose(np.round(x, 1), np.round(datapoints, 1).reshape(1, -1))
            find_dp = np.where(l_dp)[1]
            stor_sum = wt * norm1[0, find_dp]

            stor_sum_val.append(stor_sum)
            new_storing_mat = np.array(stor_sum_val)

            # Code to find the spiketime of neurons all features
            for j in range(new_storing_mat.shape[1]):
                mfspike = EulerAdEx(new_storing_mat[i, j])
                mf_spike[i].append(mfspike)

        celength = [len(row) for row in mf_spike]
        m = max(celength)

        spike_positions = [[] for _ in range(inp_for_sys_norm.shape[1])]
        for i in range(inp_for_sys_norm.shape[1]):
            for j in range(len(mf_spike[i])):
                if len(mf_spike[i][j]) < m:
                    temp_zero = np.zeros(m - len(mf_spike[i][j]))
                    mf_spike[i][j] = np.concatenate((mf_spike[i][j], temp_zero))

                spike_positions[i].append(mf_spike[i][j])

        mf_spiketime.append(spiktime2matrix(spike_positions))

    return mf_spiketime
