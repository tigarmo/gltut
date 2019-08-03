from OpenGL.GL import *
from OpenGL.GLUT import *


def display():
    glClearColor(224 / 255, 255 / 255, 255 / 255, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(1.0, 0.0, 0.0)
    glRotatef(45, 0, 0, 1)

    glBegin(GL_QUADS)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glEnd()

    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"gltut")
glutDisplayFunc(display)
glutMainLoop()
