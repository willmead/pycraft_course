import math

from pyglet.gl import *
from pyglet.window import key

from model import Model
from player import Player

class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(300,200)
        self.model = Model()
        self.player = Player()
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)

        self.locked = False

    def on_draw(self):
        self.clear()
        self.set3d()
        rot = self.player.rot
        glRotatef(-rot[0], 1, 0, 0)
        glRotatef(-rot[1], 0, 1, 0)
        x, y, z = self.player.pos
        glTranslatef(-x, -y, -z)
        self.model.draw()

    def update(self, dt):
        self.player.update(dt, self.keys)

    def Projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def Model(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def set2d(self):
        self.Projection()
        gluOrtho2D(0, self.width, 0, self.height)
        self.Model()

    def set3d(self):
        self.Projection()
        gluPerspective(70, self.width/self.height, 0.05, 1000)
        self.Model()

    def set_lock(self, state):
        self.lock = state
        self.set_exclusive_mouse(state)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.locked:
            self.player.mouse_motion(dx, dy)

    def on_key_press(self, KEY, MOD):
        if KEY == key.ESCAPE:
            self.close()
        elif KEY == key.E:
            self.locked = True
            self.set_exclusive_mouse(True)

if __name__ == '__main__':
    window = Window(width=400, height=300, caption="Pycraft", resizable=True)
    glClearColor(0.5,0.7,1,1)
    pyglet.app.run()
