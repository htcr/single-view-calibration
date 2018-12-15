import numpy as np
from math_helper import *

known_b = (1, 2)
known_t = (3, 4)

known_l = 100

measure_b = (5, 6)
measure_t = (7, 8)

v1 = (5, 6)
v2 = (7, 8)
v = (9, 0)

# solve horizon line
horizon = two_points_to_general((v1, v2)) # (3, 1)
l_hat = horizon / np.linalg.norm(horizon)

# solve alpha with known length
known_b_h = np.array([known_b[0], known_b[1], 1.0])
known_t_h = np.array([known_t[0], known_t[1], 1.0])
v_h = np.array([v[0], v[1], 1.0])

l_hat_b = np.sum(l_hat.reshape(-1) * known_b_h)

alpha = 1.0 - np.linalg.norm(np.cross(known_b_h, known_t_h)) / ( l_hat_b * np.linalg.norm(np.cross(v_h, known_t_h)) * known_l)

# solve Z with alpha
measure_b_h = np.array([measure_b[0], measure_b[1], 1.0])
measure_t_h = np.array([measure_t[0], measure_t[1], 1.0])

l_hat_b = np.sum(l_hat.reshape(-1) * measure_b_h)

Z = 1.0 - np.linalg.norm(np.cross(known_b_h, known_t_h)) / ( l_hat_b * np.linalg.norm(np.cross(v_h, known_t_h)) * alpha)

print('measured length: %f' % Z)
