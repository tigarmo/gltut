from pathlib import Path

# Tell Mesa to use this version of OpenGL
import os; os.environ['MESA_GL_VERSION_OVERRIDE'] = '3.0'

from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

angle = 0.0


def display():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glColor3f(1.0, 0.0, 0.0)
    glScalef(0.5, 0.5, 0.5)
    glRotatef(angle, 0, 0, 1)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glEnd()

    glutSwapBuffers()


def special(key, _x, _y):
    global angle
    if key == GLUT_KEY_END:
        glutLeaveMainLoop()
        return
    if key == GLUT_KEY_LEFT:
        angle += 5
    elif key == GLUT_KEY_RIGHT:
        angle -= 5
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"gltut")
glutDisplayFunc(display)
glutSpecialFunc(special)
glutMainLoop()
