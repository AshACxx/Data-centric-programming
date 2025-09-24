import py5

mode = 0
shape_size = 50  


def key_pressed():
    
    global mode, shape_size

    if py5.key >= '0' and py5.key <='9':
        mode = int(py5.key) - int ('0')
        print(mode)
    
    if py5.key == '1' or py5.key == '2':
        shape_size += 10

    if py5.key == '3' or py5.key == '4':
        shape_size -= 10

def setup():

    py5.size(400, 400)
    py5.ellipse_mode(py5.CENTER)
    

def draw():

    py5.background(0)
    global mode, shape_size
    print(mode)

#if u press 1 u enlarge a green square
    if mode == 1:
        py5.rect(py5.mouse_x, py5.mouse_y, shape_size,shape_size) 
        py5.fill(0,255,0)

#if u press 2 u enlarge a red circle
    elif mode == 2:
        py5.circle(py5.mouse_x, py5.mouse_y,shape_size) 
        py5.fill(255,0,0)

#if u press 3 u reduce the red circle
    elif mode == 3:
        py5.circle(py5.mouse_x, py5.mouse_y,shape_size) 
        py5.fill(255,0,0)

#if u press 1 u reduces a green square
    elif mode == 4:
        py5.rect(py5.mouse_x, py5.mouse_y, shape_size,shape_size) 
        py5.fill(0,255,0)


py5.run_sketch()