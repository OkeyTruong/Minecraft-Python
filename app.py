from ursina import *
from ursina.prefabs.first_person_controller import  FirstPersonController

app = Ursina()

# setup
grass_texture = Texture('assets/grass_block.png')
stone_texture = Texture('assets/stone_block.png')
brick_texture = Texture('assets/brick_block.png')
dirt_texture = Texture('assets/dirt_block.png')

block_pick = 1

def update():
    global block_pick
    if held_keys["1"]:block_pick = 1
    if held_keys["2"]:block_pick = 2
    if held_keys["3"]:block_pick = 3
    if held_keys["4"]:block_pick = 4

class Box(Button):
    def __init__(self,position=(0,0,0), texture = grass_texture):
        super().__init__(
            parent= scene,
            position = position,
            model = "assets/block",
            origin_y  = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5,
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1: box = Box(position = self.position + mouse.normal, texture = grass_texture )    
                if block_pick == 2: box = Box(position = self.position + mouse.normal, texture = stone_texture )    
                if block_pick == 3: box = Box(position = self.position + mouse.normal, texture = brick_texture )    
                if block_pick == 4: box = Box(position = self.position + mouse.normal, texture = dirt_texture )    
            if key == 'right mouse down':
               destroy(self)
        


for z in range(20):
    for x in range(20):
        box = Box(position=(x,0,z))

player = FirstPersonController()

app.run()