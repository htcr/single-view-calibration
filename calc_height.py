import numpy as np
from math_helper import *

known_b = (97.5483, 206.986)
known_t = (87.0014, 150.416)

known_l = 1.0

measure_b = (134.942, 176.304)
measure_t = (122.477, 29.6065)

v1 = (450.65536571694247, 108.71242830265025)
v2 = (81.6959714367192, 118.67617093689188)
v = (165.7355936870725, 568.6033385424374)

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

print('measured length: %f' % Z)
