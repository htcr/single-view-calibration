from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
width, height = 500, 400

def draw_rect(x, y, w, h):
    glColor3f(0, 0, 1)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x+w, y)
    glVertex2f(x+w, y+h)
    glVertex2f(x, y+h)
    glEnd()

def refresh2d(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, w, 0, h, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(400, 500)

    draw_rect(10, 20, 200, 300)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
window = glutCreateWindow('test-window')
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()