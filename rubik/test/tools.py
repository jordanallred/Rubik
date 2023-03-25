from rubik.model.cube import Cube
from rubik.model.constants import *
import random, string

def create_cube():
    encodedCube = ""
    for index in range(NUM_FACES):
        colors = string.ascii_uppercase + string.ascii_lowercase + string.digits
        color = random.choice(colors)
        encodedCube += color * (NUM_ELEMENTS // NUM_FACES)
        colors.replace(color, '')
    cube = Cube(encodedCube)
    cube.rotate(random.choices(list(VALID_DIRECTIONS), k=10))
    return cube