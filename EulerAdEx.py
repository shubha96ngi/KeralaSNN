import numpy as np

def EulerAdEx(I):
    dt = 0.025
    x = np.arange(0, 300 + dt, dt)  # Equivalent to MATLAB: 0:dt:300
    
    V = np.zeros(len(x))
    w = np.zeros(len(x))
    VV = np.zeros(len(x))
    spiketime = np.zeros(len(x))
    mfspike = []
    
    Vr = -58
    b = 265
    el = -70
    V[0] = -60
    w[0] = V[0] - el
    sp_cnt = 1
    
    for i in range(len(x) - 1):
        V[i + 1] = V[i] + dt * Voltage(V[i], w[i], I)
        w[i + 1] = w[i] + dt * AdCurrent(V[i], w[i])
        
        if V[i + 1] > 0:
            VV[i + 1] = 0
            V[i + 1] = Vr
            w[i + 1] += b
            spiketime[i + 1] = 1
            mfspike.append(x[i + 1])
            sp_cnt += 1
        else:
            VV[i + 1] = V[i + 1]
    
    return mfspike
