import pygame
from OpenGL.GL import *
import numpy
import ctypes
from OpenGL.GL.shaders import compileProgram, compileShader
import os

class App():
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        glClearColor(0.3,0.1,0.1,1)
        base_path = os.path.dirname(__file__)
        self.shader = self.createShader(
            os.path.join(base_path, "shaders/vertex.txt"),
            os.path.join(base_path, "shaders/fragment.txt")
        )
        glUseProgram(self.shader)
        glUniform1i(glGetUniformLocation(self.shader, "imageTexture"), 0)
        self.square = Square()
        self.texture = Material(os.path.join(base_path, "gfx/wood.jpg"))
        self.mainLoop()

    def createShader(self, vertexFilepath, fragmentFilepath):
        with open(vertexFilepath, 'r') as f:
            vertex_src = f.readlines()
        
        with open(fragmentFilepath, 'r') as f:
            fragment_src = f.readlines()
        
        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )
        return shader

    def mainLoop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            glClear(GL_COLOR_BUFFER_BIT)

            glUseProgram(self.shader)
            self.texture.use()
            glBindVertexArray(self.square.vao)
            glDrawArrays(GL_QUADS, 0, self.square.vertex_count)

            pygame.display.flip()
            self.clock.tick(60)
        self.quit()

    def quit(self):
        self.square.destroy()
        self.texture.destroy()
        glDeleteProgram(self.shader)
        pygame.quit()

class Square():
    def __init__(self):
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0,
            0.5, -0.5, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0,
            0.5, 0.5, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0,
            -0.5, 0.5, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0
        )
        self.vertices = numpy.array(self.vertices, dtype=numpy.float32)
        self.vertex_count = 4
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))


    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))

class Material():
    def __init__(self, filepath):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        image = pygame.image.load(filepath).convert_alpha()
        image_width, image_height = image.get_rect().size
        image_data = pygame.image.tostring(image, "RGBA")
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
        glGenerateMipmap(GL_TEXTURE_2D)
    
    def use(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)
    
    def destroy(self):
        glDeleteTextures(1, (self.texture,))

if __name__ == "__main__":
    app = App(700,700)