import moderngl
import moderngl_window as mglw
import struct


class Triangle(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (800, 600)
    title = "Triangle"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        vertices = [
            -0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0, 0.5, 0.0,
        ]

        vertex_shader = '''
        #version 330
        in vec3 in_position;
        void main() {
            gl_Position = vec4(in_position, 1.0);
        }
        '''

        fragment_shader = '''
        #version 330
        out vec4 fragColor;
        void main() {
            fragColor = vec4(1.0, 0.0, 0.0, 1.0);
        }
        '''

        self.program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        self.vbo = self.ctx.buffer(struct.pack('9f', *vertices))
        self.vao = self.ctx.vertex_array(self.program, [(self.vbo, '3f', 'in_position')])

    def on_render(self, time, frame_time):
        self.ctx.clear(0.1, 0.1, 0.1, 1.0)
        self.vao.render()


if __name__ == '__main__':
    import os

    os.environ['MODERNGL_WINDOW'] = 'glfw'
    Triangle.run()