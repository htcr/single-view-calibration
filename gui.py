import matplotlib.pyplot as plt
import numpy as np
import cv2
from math_helper import two_points_to_general

img = cv2.imread('test.jpg')
fig, ax = plt.subplots()
plt.imshow(img)

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.two_points_form = (p1, p2)
        self.general_form = two_points_to_general(self.two_points_form)

class DrawLineControl(object):
    def __init__(self, ax, img_shape):
        # ax: where to draw line
        # img_shape: (h, w)
        self.lines = list()
        self.first_point = None
        self.ax = ax

        # img bounds, four lines, in vector form
        h, w = img_shape
        lb = np.array([[1, 0, 0]]).T
        tb = np.array([[0, 1, 0]]).T
        rb = np.array([[1, 0, -w]]).T
        bb = np.array([[0, 1, -h]]).T

        self.bounds = (lb, tb, rb, bb)

    def click_callback(self, event):
        if event.xdata:
            x, y = event.xdata, event.ydata
            if not self.first_point:
                self.first_point = (x, y)
            else:
                second_point = (x, y)
                new_line = (self.first_point, second_point)
                new_line_id = len(self.lines)
                self.lines.append(new_line)

                # TODO: draw new line

                self.first_point = None
        else:
            print('click out of bound')

    def draw_new_line(self, new_line, line_id):
        pass




plt.show()

'''
img = cv2.imread('test.jpg')

fig, ax = plt.subplots()
#ax.plot(np.random.rand(10))
plt.imshow(img)

def on_click(event):
    if event.xdata:
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % 
            ('double' if event.dblclick else 'single', event.button,
            event.x, event.y, event.xdata, event.ydata))
    else:
        print('out of bound')

cid = fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()
'''

'''
from matplotlib.widgets import Button

freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = plt.plot(t, s, lw=2)

class Index(object):
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1 
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()
'''


