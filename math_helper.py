import numpy as np

def two_points_to_general(two_points):
    p1, p2 = two_points
    x1, y1 = p1
    x2, y2 = p2
    a = y2 - y1
    b = x1 - x2
    c = x2 * y1 - x1 * y2
    
    return np.array([[a, b, c]]).T

def intersect_line_with_line(l1, l2):
    # l1, l2: lines, general form, vector
    # return: itsc pt (x, y) or None
    itsc = np.cross(l1.reshape(-1), l2.reshape(-1)) # (3,)
    x, y, w = itsc
    if np.abs(w) < 1e-5:
        return None
    else:
        x, y = x/w, y/w
        return (x, y)

def point_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dist

def intersect_line_with_rect(line, rect):
    # line: general form, vector
    # rect: (lb, tb, rb, bb), all general form, vectors
    # return: two intersect points
    rb, bb = rect[2], rect[3]
    h = -bb[2]
    w = -rb[2]


    # get all intersect points
    itsc_pts = list()
    for bound in rect:
        itsc_pt = intersect_line_with_line(line, bound)
        if itsc_pt:
            itsc_pts.append(itsc_pt)
    
    dup_dist_thresh = 0.01

    # nms pts
    i = 0
    while i < len(itsc_pts):
        cur_pt = itsc_pts[i]
        j = i+1
        while j < len(itsc_pts):
            other_pt = itsc_pts[j]
            dist = point_dist(cur_pt, other_pt)
            if dist < dup_dist_thresh:
                itsc_pts.pop(j)
            else:
                j += 1
        i += 1
    
    # pick two legal points
    final_pts = list()
    for pt in itsc_pts:
        x, y = pt
        if 0 <= x <= w and 0 <= y <= h:
            final_pts.append(pt)
    
    assert len(final_pts) == 2
    
    return final_pts[0], final_pts[1]
    