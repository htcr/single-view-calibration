import numpy as np
from math_helper import *

v1 = (-11274.44, 1955.96)
v2 = (527.27, 494.05)
v = (4249.46, 33328.73)

ts = [(297.02, 145.47)]
bs = [(362.77, 711.82)]
lens = [243.4]

# solve horizon line
horizon = two_points_to_general((v1, v2)) # (3, 1)
l_hat = horizon / np.linalg.norm(horizon)
v_h = np.array([v[0], v[1], 1.0])

def get_alpha(known_b, known_t, known_l):
    # solve alpha with known length
    known_b_h = np.array([known_b[0], known_b[1], 1.0])
    known_t_h = np.array([known_t[0], known_t[1], 1.0])

    l_hat_b = np.sum(l_hat.reshape(-1) * known_b_h)

    alpha = -(np.linalg.norm(np.cross(known_b_h, known_t_h)) / ( l_hat_b * np.linalg.norm(np.cross(v_h, known_t_h)) * known_l))

    return alpha

N = len(ts)
alphas = list()
for i in range(N):
    known_b, known_t = bs[i], ts[i]
    known_l = lens[i]
    alpha = get_alpha(known_b, known_t, known_l)
    alphas.append(alpha)
alpha = np.mean(alpha)
print('alpha: %.10f' % alpha)

alpha_Z_mat = np.array([[v1[0], v2[0], l_hat[0, 0]], [v1[1], v2[1], l_hat[1, 0]], [1.0, 1.0, l_hat[2, 0]]])
alpha_Z = - (np.linalg.det(alpha_Z_mat))

W_mat = np.array([[v1[0], v2[0], v[0]], [v1[1], v2[1], v[1]], [1.0, 1.0, 1.0]])
W = (np.linalg.det(W_mat))

Z = alpha_Z / alpha / W

print('Z: %.2f' % Z)
