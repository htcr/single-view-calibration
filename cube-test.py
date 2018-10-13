import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

class Polygon(object):
    def __init__(self, vset, eset, edge_color=None):
        # vset: 3xNv 3d point set
        # eset: edge set, Nex2 int pair set, each col
        # indicates two vertices that are connected
        self.vset = vset
        self.eset = eset
        if edge_color is None:
            self.edge_color = np.zeros((eset.shape[0], 3), dtype=np.float32)
        else:
            self.edge_color = edge_color
    
    def get_dimension(self):
        return vset.shape[0]

def to_homogeneous(points):
    # points: nd array of shape (d, N)
    # return: nd array of shape (d+1, N),
    # with last row are all 1
    h = np.ones((1, points.shape[1]), dtype=np.float32)
    return np.concatenate((points, h), axis=0)

def to_cartesian(points):
    # points: nd array of shape (d+1, N)
    # return: nd array of shape (d, N)
    assert points.shape[0] > 1
    ans = points[:-1, :].copy()
    ans = ans / points[-1, :][np.newaxis, :]
    return ans

def get_unit_cube():
    vset = [[0,0,0], [1,0,0], [1,1,0], [0,1,0],
            [0,0,1], [1,0,1], [1,1,1], [0,1,1]]
    vset = np.array(vset, dtype=np.float32).transpose((1,0))
    eset = [[0,1], [1,2], [2,3], [3,0],
            [0,4], [1,5], [2,6], [3,7],
            [4,5], [5,6], [6,7], [7,4]]
    eset = np.array(eset, dtype=np.int32)
    edge_color = np.zeros((eset.shape[0], 3), dtype=np.float32)
    edge_color[0, :] = [1, 0, 0]
    edge_color[3, :] = [0, 1, 0]
    edge_color[4, :] = [0, 0, 1]
    cube = Polygon(vset, eset, edge_color)
    return cube

def draw_segment_2d(ax, p1, p2, color):
    # p1, p2: (x, y)
    # color: (r, g, b)
    xs = [p1[0], p2[0]]
    ys = [p1[1], p2[1]]
    ax.plot(xs, ys, c=color)

def get_look_at_matrix(eye, at):
    # eye, at: 3d point coordinate, cartesian, np array of shape (3,)
    # return : np array of shape (3, 4)
    
    # camera system axes in world coordinate
    cz = at - eye
    cz = cz / la.norm(cz)
    up = np.array([0, 0, 1], dtype=np.float32)
    cx = np.cross(cz, up)
    cx = cx / la.norm(cx)
    cy = np.cross(cz, cx)
    cy = cy / la.norm(cy)

    # last column of projection matrix
    t = -eye

    # put together
    R = np.stack((cx, cy, cz), axis=0)
    Rt = np.concatenate((R, t[:, np.newaxis]), axis=1)
    return Rt
    
def get_camera_matrix(f=3.5):
    # f: focal length, in cm
    # return: transformation from camera coordinate 
    # to image plane coordinate (not pixel coordinate!),
    # np array of shape (3, 3)
    camera_matrix = np.array([[f, 0, 0], [0, f, 0], [0, 0, 1]], dtype=np.float32)
    return camera_matrix

def get_image_matrix(f=3.5, aov_w=60, aov_h=60, img_w=600, img_h=600):
    # f: focal length, in cm
    # aov_w, aov_h: angle of view, in degrees
    # img_w, img_h: image size in pixel
    # return: transformation from image plane coordinate
    # to image pixel coordinate, 
    # np array of shape (3, 3)
    ax = img_w / (2.0*f) * np.cos(np.deg2rad(aov_w) / 2.0)
    ay = img_h / (2.0*f) * np.cos(np.deg2rad(aov_h) / 2.0)
    bx = img_w / 2.0
    by = img_h / 2.0
    image_matrix = np.array([[ax, 0, bx], [0, ay, by], [0, 0, 1]], dtype=np.float32)
    return image_matrix

def get_simple_camera():
    # get the intrinsic and extrinsic matrices
    # of a default camera positioned at
    # (10, 10, 8) cm and looking at (0, 0, 0) cm
    eye = np.array([10, 10, 8], dtype=np.float32)
    at = np.array([0, 0, 0], dtype=np.float32)
    
    # extrinsic
    Rt = get_look_at_matrix(eye, at)
    
    # intrinsic
    M_cam = get_camera_matrix()
    M_img = get_image_matrix()
    K = M_img @ M_cam

    return K, Rt

def project(poly_3d, K, Rt):
    # project a 3d polygon to 2d with 
    # intrinsic and extrinsic matrices
    # poly_3d: 3d input Polygon
    # K, Rt: intrinsic and extrinsic
    # return: a 2d polygon with image pixel coordinate
    assert poly_3d.vset.shape[0] == 3
    vset_3d_homo = to_homogeneous(poly_3d.vset)
    vset_2d_homo = K @ Rt @ vset_3d_homo
    vset_2d_cart = to_cartesian(vset_2d_homo)
    return Polygon(vset_2d_cart, poly_3d.eset, poly_3d.edge_color)

    

# test

K, Rt = get_simple_camera()
print(K)
print(Rt)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.invert_yaxis()
ax.axis('equal')
p1 = (1, 0)
p2 = (0, 1)
color = (0, 0, 0)
draw_segment_2d(ax, p1, p2, color)
plt.show()
