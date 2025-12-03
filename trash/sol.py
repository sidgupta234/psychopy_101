"""
PSYCHOPY SOLUTIONS (SET 2)
==========================
Detailed solutions focusing on Pixels, Logic, and Animation.
"""

from psychopy import visual, core, event, gui
import random

# ==============================================================================
# SOLUTION 1: The Four Corners (Pixel Coordinates)
# ==============================================================================
print("--- Running Exercise 1 ---")
win = visual.Window(size=[800, 600], units='pix', color=[-1, -1, -1])

# Create 4 shapes at specific coordinates relative to center (0,0)
sq_tr = visual.Rect(win, width=100, height=100, fillColor='red', pos=(200, 200))
sq_tl = visual.Rect(win, width=100, height=100, fillColor='blue', pos=(-200, 200))
sq_bl = visual.Rect(win, width=100, height=100, fillColor='green', pos=(-200, -200))
sq_br = visual.Rect(win, width=100, height=100, fillColor='yellow', pos=(200, -200))

# Draw them all
sq_tr.draw()
sq_tl.draw()
sq_bl.draw()
sq_br.draw()

win.flip()
event.waitKeys()
win.close()

# ==============================================================================
# SOLUTION 2: The Logic GUI
# ==============================================================================
print("--- Running Exercise 2 ---")

# 1. Get Input
info = gui.Dlg(title="Choose Condition")
info.addField("Condition:", choices=["A", "B"])
user_data = info.show()

if info.OK:
    condition = user_data[0]
else:
    core.quit() # Exit if cancelled

# 2. Create Window
win = visual.Window(size=[800, 600], units='pix', color='black')
instruction = visual.TextStim(win, text=f"You chose Condition {condition}", pos=(0, 200))

# 3. Logic decision
if condition == 'A':
    shape = visual.Circle(win, radius=50, fillColor='blue')
elif condition == 'B':
    shape = visual.Rect(win, width=100, height=100, fillColor='red')

# 4. Display
instruction.draw()
shape.draw()
win.flip()
core.wait(2.0)
win.close()

# ==============================================================================
# SOLUTION 3: The "Go / No-Go" Task
# ==============================================================================
print("--- Running Exercise 3 ---")

win = visual.Window(size=[800, 600], units='pix', color='black')
stimulus = visual.Circle(win, radius=60)
feedback = visual.TextStim(win, text="", height=40)

# Run 5 Trials
for i in range(5):
    # Determine trial type randomly
    trial_type = random.choice(['go', 'nogo'])
    
    if trial_type == 'go':
        stimulus.fillColor = 'green'
        correct_key = 'space'
    else:
        stimulus.fillColor = 'red'
        correct_key = None # No key should be pressed

    # Draw Stimulus
    stimulus.draw()
    win.flip()

    # Wait for response (max 1.5 seconds)
    # clearEvents is vital here to ensure we don't catch old keypresses
    event.clearEvents()
    keys = event.waitKeys(maxWait=1.5, keyList=['space'])

    # Determine Feedback Logic
    if trial_type == 'go':
        if keys and 'space' in keys:
            feedback.text = "Correct! (Hit)"
            feedback.color = 'green'
        else:
            feedback.text = "Missed!"
            feedback.color = 'white'
            
    elif trial_type == 'nogo':
        if keys:
            feedback.text = "False Alarm! (Pressed on Red)"
            feedback.color = 'red'
        else:
            feedback.text = "Correct! (Withheld)"
            feedback.color = 'green'

    # Show Feedback
    feedback.draw()
    win.flip()
    core.wait(1.0) # Wait 1s so user can read feedback

win.close()

# ==============================================================================
# SOLUTION 4: The Bouncing Ball (Animation)
# ==============================================================================
print("--- Running Exercise 4 ---")

win = visual.Window(size=[800, 600], units='pix', color='black')
ball = visual.Circle(win, radius=20, fillColor='white', pos=[0,0])

# Speed variables (pixels per frame)
speed_x = 6

instruction = visual.TextStim(win, text="Press ESC to quit", pos=(0, 250))

is_animating = True

while is_animating:
    # 1. Update Position
    # ball.pos is a list-like object [x, y]
    # We take current X (ball.pos[0]) and add speed
    new_x = ball.pos[0] + speed_x
    ball.pos = [new_x, 0] # We only change X, keep Y at 0

    # 2. Check Collisions (Window width is 800, so edges are +/- 400)
    # We subtract the radius (20) so it bounces when the *edge* hits, not the center
    if ball.pos[0] > 380:
        speed_x = -6 # Reverse direction to Left
    elif ball.pos[0] < -380:
        speed_x = 6  # Reverse direction to Right

    # 3. Check Input
    if 'escape' in event.getKeys():
        is_animating = False

    # 4. Draw
    instruction.draw()
    ball.draw()
    win.flip()

win.close()

# ==============================================================================
# SOLUTION 5: The "Draggable" Shape
# ==============================================================================
print("--- Running Exercise 5 ---")

win = visual.Window(size=[800, 600], units='pix', color='black')

# Create a triangle
triangle = visual.Polygon(win, edges=3, radius=60, fillColor='orange', pos=(0,0))
instruction = visual.TextStim(win, text="Click and Drag the Triangle\nPress Q to quit", pos=(0, 250))

mouse = event.Mouse(win=win)

is_running = True
while is_running:
    # Get quit key
    if 'q' in event.getKeys():
        is_running = False

    # Drag Logic
    # 1. Is left button (0) pressed?
    if mouse.getPressed()[0]:
        # 2. Is mouse inside the shape?
        if triangle.contains(mouse):
            # 3. Update position
            triangle.pos = mouse.getPos()
            
            # Optional visual feedback
            triangle.opacity = 0.5
        else:
            triangle.opacity = 1.0
    else:
        triangle.opacity = 1.0

    instruction.draw()
    triangle.draw()
    win.flip()

win.close()
core.quit()