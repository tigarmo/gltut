from pathlib import Path

from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

angle = 0.0
angle_location = None


def display():
    glClearColor(224 / 255, 255 / 255, 255 / 255, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

    glutSwapBuffers()


def init_gl():
    build_geometry()
    compile_shaders()


def build_geometry():
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    verts = np.array(
        [-1.0, -1.0, 0.0, 1.0, -1.0, 0.0, 1.0, 1.0, 0.0, -1.0, 1.0, 0.0],
        dtype=np.float32,
    )

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, verts, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    elements = np.array([0, 1, 2, 0, 2, 3], dtype=np.int32)

    ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, elements, GL_STATIC_DRAW)


def _compile_shader_source(shader_id, shader_path):
    contents = Path(shader_path).read_text()
    print(contents)
    glShaderSource(shader_id, contents)
    glCompileShader(shader_id)
    compile_ok = glGetShaderiv(shader_id, GL_COMPILE_STATUS)
    if not compile_ok:
        raise RuntimeError(glGetShaderInfoLog(shader_id))


def compile_shaders():
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    _compile_shader_source(vertex_shader, "./shaders/shader.vert")

    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    _compile_shader_source(fragment_shader, "./shaders/shader.frag")

    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        raise RuntimeError(glGetProgramInfoLog(program))

    glUseProgram(program)

    global angle_location
    angle_location = glGetUniformLocation(program, "angle")


def special(key, _x, _y):
    global angle
    if key == GLUT_KEY_DOWN:
        glutLeaveMainLoop()
        return
    if key == GLUT_KEY_LEFT:
        angle -= 5
    elif key == GLUT_KEY_RIGHT:
        angle += 5
    glUniform1f(angle_location, angle)
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"gltut")
init_gl()
glutDisplayFunc(display)
glutSpecialFunc(special)
glutMainLoop()
