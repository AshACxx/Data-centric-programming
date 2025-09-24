import py5
import random

box_x= 50
box_y =50 
box_size= 25
def setup():

    py5.size(400, 400)
    


def mouse_pressed():
    
    global box_x, box_y, box_size
    
    #checks if the mouse in inside the box (AI USED FOR THIS PART)
    if box_x <= py5.mouse_x <= box_x + box_size and box_y <= py5.mouse_y <= box_y + box_size:
        box_x = random.randint(0, py5.width - box_size)
        box_y = random.randint(0, py5.height - box_size)
        box_size = random.randint(20, 50)

def draw():

    py5.background (225)
    py5.fill(255,0,0)
    py5.rect(box_x, box_y, box_size, box_size)




py5.run_sketch()