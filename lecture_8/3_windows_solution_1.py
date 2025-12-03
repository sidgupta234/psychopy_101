from psychopy import visual, event

# 1. Setup
win = visual.Window(size=[800, 600], color=[-1, -1, -1])

# 2. Pixel Logic
win.units = "pix"
pixel_square = visual.Rect(
    win, 
    width=100, height=100, 
    pos=[200, 200], # Top Right in pixels
    fillColor=[1, -1, -1] # Red
)

# 3. Norm Logic
win.units = "norm"
norm_circle = visual.Circle(
    win,
    radius=0.1,
    pos=[-0.75, -0.75], # Bottom Left in norm
    fillColor=[-1, -1, 1] # Blue
)

# 4. Draw and Display
pixel_square.draw()
norm_circle.draw()
win.flip()

print("Showing Shapes. Press any key to exit.")
event.waitKeys()
win.close()