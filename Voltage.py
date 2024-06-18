def Voltage(V, w, I):
    C = 900
    gl = 10
    el = -70
    delT = 2
    Vt = -50  # Initial value in MATLAB function
    Vt = (gl * (el - V) + gl * delT * np.exp((V - Vt) / delT) + I - w) / C
    return Vt
