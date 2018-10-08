from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
width, height = 500, 400

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    #TODO: draw rect

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
window = glutCreateWindow('test-window')
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()