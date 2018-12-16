import numpy as np
from math_helper import *

v1 = (-806.65, 454.72)
v2 = (1534.04, 179.37)
v  = (1250.14, 5156.87)

ts = [(191.85, 16.48), (571.74, 553.24), (564.05, 497.88), (693.24, 760.87)]
bs = [(390.25, 982.35), (600.96, 762.41), (600.96, 762.41), (736.30, 1073.09)]
lens = [243.0, 85.2, 105.2, 77.0]

def measure(known_b, known_t, known_l, measure_b, measure_t):
    # solve horizon line
    horizon = two_points_to_general((v1, v2)) # (3, 1)
    l_hat = horizon / np.linalg.norm(horizon)

    # solve alpha with known length
    known_b_h = np.array([known_b[0], known_b[1], 1.0])
    known_t_h = np.array([known_t[0], known_t[1], 1.0])
    v_h = np.array([v[0], v[1], 1.0])

    l_hat_b = np.sum(l_hat.reshape(-1) * known_b_h)

    alpha = -(np.linalg.norm(np.cross(known_b_h, known_t_h)) / ( l_hat_b * np.linalg.norm(np.cross(v_h, known_t_h)) * known_l))

    # solve Z with alpha
    measure_b_h = np.array([measure_b[0], measure_b[1], 1.0])
    measure_t_h = np.array([measure_t[0], measure_t[1], 1.0])

    l_hat_b = np.sum(l_hat.reshape(-1) * measure_b_h)

    Z = -(np.linalg.norm(np.cross(measure_b_h, measure_t_h)) / ( l_hat_b * np.linalg.norm(np.cross(v_h, measure_t_h)) * alpha))

    return Z

N = len(ts)
ans = list()
for i in range(N):
    known_b, known_t = bs[i], ts[i]
    known_l = lens[i]
    row = list()
    for j in range(N):
        if j == i:
            row.append('%.1f*' % known_l)
        else:
            measure_b, measure_t = bs[j], ts[j]
            Z = measure(known_b, known_t, known_l, measure_b, measure_t)
            row.append('%.1f' % Z)
    ans.append(row)

for row in ans:
    print(row)