from project_pipeline import *

# test
fig = plt.figure()
ax = fig.add_subplot(111)
ax.invert_yaxis()
ax.axis('equal')
# playground

K, Rt = get_simple_camera(eye=(2, 2*3**0.5, 1.5), at=(0, 0, 0))
print(K)
print(Rt)

cube0 = get_unit_cube(offset=(0, 0, 0))
cube1 = get_unit_cube(offset=(1, 0, 0))
cube2 = get_unit_cube(offset=(0, -1, 0))
cube3 = get_unit_cube(offset=(0, -1, 1))
cube4 = get_unit_cube(offset=(0, -1, 2))


objects = [cube0, cube1, cube2, cube3, cube4]

for obj in objects:
    obj_2d = project(obj, K, Rt)
    draw_poly_2d(ax, obj_2d)

draw_img_bound(ax)

# playground
plt.show()
