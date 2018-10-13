import numpy as np
import matplotlib.pyplot as plt

class Polygon(object):
    def __init__(self, vset, eset):
        # vset: 3xNv 3d point set
        # eset: edge set, 2xNe int pair set, each col
        # indicates two vertices that are connected
        self.vset = vset
        self.eset = eset
        self.edge_color = None

def get_unit_cube():
    vset = [[0,0,0], [1,0,0], [1,1,0], [0,1,0],
            [0,0,1], [1,0,1], [1,1,1], [0,1,1]]
    vset = np.array(vset, dtype=np.float32).transpose((1,0))
    eset = [[0,1], [1,2], [2,3], [3,0],
            [0,4], [1,5], [2,6], [3,7],
            [4,5], [5,6], [6,7], [7,4]]
    eset = np.array(eset, dtype=np.int32).transpose((1, 0))
    edge_color = np.zeros((3, eset.shape[1]), dtype=np.float32)
    edge_color[:, 0] = [1, 0, 0]
    edge_color[:, 3] = [0, 1, 0]
    edge_color[:, 4] = [0, 0, 1]
    cube = Polygon(vset, eset)
    cube.edge_color = edge_color
    return cube

def draw_segment_2d(ax, p1, p2, color):
    # p1, p2: (x, y)
    # color: (r, g, b)
    xs = [p1[0], p2[0]]
    ys = [p1[1], p2[1]]
    ax.plot(xs, ys, c=color)

 
# test
fig = plt.figure()
ax = fig.add_subplot(111)
ax.invert_yaxis()
ax.axis('equal')
p1 = (1, 0)
p2 = (0, 1)
color = (1, 0, 0)
draw_segment_2d(ax, p1, p2, color)
plt.show()
