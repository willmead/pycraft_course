from pyglet.gl import *

class Model:
    def __init__(self):

        self.top = self.get_tex('grass_top.jpg')
        self.side = self.get_tex('grass_side.jpg')
        self.bottom = self.get_tex('dirt.jpg')

        self.batch = pyglet.graphics.Batch()

        tex_coords = ('t2f', (0,0, 1,0, 1,1, 0,1, ))

        # Co-Ordinates
        x,y,z = 0,0,-1
        X,Y,Z = x + 1, y + 1, z + 1
        face_coords_back = (X,y,z, x,y,z, x,Y,z, X,Y,z)
        face_coords_front = (x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)
        face_coords_left = (X,y,z, x,Y,z, X,Y,Z, X,y,Z)
        # face_coords_right = (x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)

        # Batch
        self.batch.add(4, GL_QUADS, self.side, ('v3f', face_coords_back), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f', face_coords_front), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f', face_coords_left), tex_coords)
        # self.batch.add(4, GL_QUADS, self.side, ('v3f', face_coords_right), tex_coords)


    def get_tex(self, file):
        tex = pyglet.image.load(file).get_texture()
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def draw(self):
        self.batch.draw()
