import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot(np.random.rand(10))

def on_click(event):
    if event.xdata:
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % 
            ('double' if event.dblclick else 'single', event.button,
            event.x, event.y, event.xdata, event.ydata))
    else:
        print('out of bound')

cid = fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()