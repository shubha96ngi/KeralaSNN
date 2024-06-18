def createneuron(inp_for_sys, cnt_MF):
    datapoints = []
    
    if cnt_MF % 2:  # If cnt_MF is odd
        sd_cnt = int(cnt_MF / 2)
        sd_cnt = 3 / sd_cnt
        datapoints.append(inp_for_sys)
    else:
        sd_cnt = cnt_MF / 2
        sd_cnt = 3 / sd_cnt
        
    for i in range(1, cnt_MF):
        minsigma = inp_for_sys - (i * sd_cnt)
        plussigma = inp_for_sys + (i * sd_cnt)
        datapoints.extend([minsigma, plussigma])
        
    datapoints = sorted(datapoints)
    
    return datapoints
