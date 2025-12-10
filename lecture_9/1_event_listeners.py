"""
PSYCHOPY EVENT LISTENER (NO REUSABILITY VERSION)
================================================

This script demonstrates the same features but instantiates 
new objects for every single step instead of reusing variables.
"""

# --- IMPORTS ---
from psychopy import visual, core, event, gui
import sys

print("--- Initializing Window ---")

win = visual.Window(
    size=[1024, 768],
    units="pix",
    color=[-1, -1, -1], # Hardcoded Black
    fullscr=False,     
    title="Event Listener Tutorial"
)

# ------------------------------------------------------------------
# LESSON 1: THE BASICS - Blocking Input
# ------------------------------------------------------------------

# Create a specific text object just for Lesson 1 instructions
lesson1_intro = visual.TextStim(
    win, 
    text=(
        "LESSON 1: Blocking Input\n\n"
        "The script is currently PAUSED using event.waitKeys().\n"
        "Nothing else will happen until you press a specific key.\n\n"
        "Press the 'LEFT' or 'RIGHT' arrow key to continue."
    ), 
    pos=(0, 200), 
    height=30, 
    color=[1, 1, 1], # Hardcoded White
    wrapWidth=900
)

lesson1_intro.draw()
win.flip()

# Blocking wait
keys = event.waitKeys(keyList=['left', 'right'])

# Create a NEW specific text object just for Lesson 1 feedback
lesson1_feedback = visual.TextStim(
    win, 
    text=f"Great! You pressed: {keys[0]}", 
    pos=(0, 0), 
    height=40, 
    color=[-1, 1, -1] # Hardcoded Green
)

lesson1_feedback.draw()
win.flip()
core.wait(2.0)

# ------------------------------------------------------------------
# LESSON 2: REACTION TIME - Timed Input & Data Capture
# ------------------------------------------------------------------

# Create a specific text object for Lesson 2 instructions
lesson2_intro = visual.TextStim(
    win, 
    text=(
        "LESSON 2: Reaction Time (Data Capture)\n\n"
        "When the screen turns GREEN, press 'SPACE' as fast as you can.\n"
        "You have a 2-second time limit.\n\n"
        "Press any key to start the countdown."
    ), 
    pos=(0, 200), 
    height=30, 
    color=[1, 1, 1],
    wrapWidth=900
)

lesson2_intro.draw()
win.flip()
event.waitKeys() 

# Countdown loop
for i in [3, 2, 1]:
    # Create a specific text object for the countdown number
    countdown_text = visual.TextStim(
        win, 
        text=str(i), 
        pos=(0, 0), 
        height=60, 
        color=[1, 1, 1]
    )
    countdown_text.draw()
    win.flip()
    core.wait(1.0)

# Create specific circle for Lesson 2
reaction_circle = visual.Circle(
    win, 
    radius=50, 
    fillColor=[-1, 1, -1], # Green
    lineColor=[-1, 1, -1]
)
reaction_circle.draw()
win.flip()

# Start Clock
rt_clock = core.Clock()

user_response = event.waitKeys(maxWait=2.0, keyList=['space'], timeStamped=rt_clock)

# Create a specific text object for Lesson 2 results
lesson2_result = visual.TextStim(
    win, 
    text="", 
    pos=(0, 0), 
    height=40
)

if user_response is None:
    lesson2_result.text = "Too slow! (Timed out)"
    lesson2_result.color = [1, -1, -1] # Red
else:
    key_name = user_response[0][0]
    rt_time  = user_response[0][1]
    lesson2_result.text = f"Got it! RT: {rt_time:.3f} seconds"
    lesson2_result.color = [1, 1, 1] # White

lesson2_result.draw()
win.flip()
event.waitKeys()

# ------------------------------------------------------------------
# LESSON 3: REAL-TIME - Non-Blocking Input
# ------------------------------------------------------------------

# Specific instructions for Lesson 3
lesson3_intro = visual.TextStim(
    win,
    text=(
        "LESSON 3: Real-Time Movement (Non-Blocking)\n\n"
        "Use Arrow Keys (Up/Down/Left/Right) to move the blue square.\n"
        "Press 'Q' to finish this lesson."
    ),
    pos=(0, 200),
    height=30,
    color=[1, 1, 1],
    wrapWidth=900
)

# Specific player object
l3_player = visual.Rect(
    win, 
    width=50, 
    height=50, 
    fillColor=[-1, -1, 1] # Blue
)
player_pos = [0, 0]

event.clearEvents() 
lesson_active = True

while lesson_active:
    # Use the Lesson 3 objects
    lesson3_intro.draw()
    l3_player.pos = player_pos
    l3_player.draw()
    win.flip()

    keys_pressed = event.waitKeys(keyList=['left', 'right', 'up', 'down', 'q'])
    #keys_pressed = event.waitKeys(keyList=['left', 'right', 'up', 'down', 'q'])
    
    player_pos[1] -= 1 

    if 'q' in keys_pressed:
        lesson_active = False 
    
    if 'left' in keys_pressed:
        player_pos[0] -= 20
    if 'right' in keys_pressed:
        player_pos[0] += 20
    if 'up' in keys_pressed:
        player_pos[1] += 20
    if 'down' in keys_pressed:
        player_pos[1] -= 20

# Specific feedback for Lesson 3
lesson3_end = visual.TextStim(
    win, 
    text="Movement Demo Complete!", 
    color=[1, 1, 1], 
    pos=(0,0), 
    height=40
)
lesson3_end.draw()
win.flip()
core.wait(1.5)

# ------------------------------------------------------------------
# LESSON 4: THE MOUSE
# ------------------------------------------------------------------

# Specific instructions for Lesson 4
lesson4_intro = visual.TextStim(
    win,
    text=(
        "LESSON 4: Mouse Tracking\n\n"
        "Move your mouse. The text will show coordinates.\n"
        "Click the LEFT mouse button to finish."
    ),
    pos=(0, 200),
    height=30,
    color=[1, 1, 1],
    wrapWidth=900
)

# Specific text object to display coordinates
lesson4_coords = visual.TextStim(
    win,
    text="",
    pos=(0, 0),
    height=40,
    color=[-1, 1, -1] # Green
)

my_mouse = event.Mouse(visible=True, win=win)
my_mouse.clickReset()

lesson_active = True
while lesson_active:
    mouse_x, mouse_y = my_mouse.getPos()
    buttons = my_mouse.getPressed()
    
    # Update the specific Lesson 4 object
    lesson4_coords.text = f"X: {mouse_x:.0f}, Y: {mouse_y:.0f}"
    
    lesson4_intro.draw()
    lesson4_coords.draw()
    win.flip()
    
    if buttons[0] == 1:
        lesson_active = False

core.wait(0.5)

# ------------------------------------------------------------------
# LESSON 5: MOUSE INTERACTION
# ------------------------------------------------------------------

# Specific instructions for Lesson 5
lesson5_intro = visual.TextStim(
    win,
    text=(
        "LESSON 5: Clicking Objects\n\n"
        "There are two buttons below.\n"
        "Click the RED button to exit the tutorial."
    ),
    pos=(0, 200),
    height=30,
    color=[1, 1, 1],
    wrapWidth=900
)

# Specific objects for Lesson 5 buttons
l5_btn_safe = visual.Rect(win, width=150, height=80, pos=(-200, -100), fillColor=[-1, 1, -1])
l5_txt_safe = visual.TextStim(win, text="Stay", pos=(-200, -100), height=25)

l5_btn_exit = visual.Rect(win, width=150, height=80, pos=(200, -100), fillColor=[1, -1, -1])
l5_txt_exit = visual.TextStim(win, text="EXIT", pos=(200, -100), height=25)

# Specific feedback text for Lesson 5
l5_feedback = visual.TextStim(win, text="", pos=(0, -250), height=40, color=[1, 1, 1])

my_mouse.clickReset()

lesson_active = True
while lesson_active:
    # Handling opacity locally
    if l5_btn_safe.contains(my_mouse):
        l5_btn_safe.opacity = 0.5
    else:
        l5_btn_safe.opacity = 1.0

    if l5_btn_exit.contains(my_mouse):
        l5_btn_exit.opacity = 0.5
    else:
        l5_btn_exit.opacity = 1.0

    lesson5_intro.draw()
    l5_btn_safe.draw()
    l5_txt_safe.draw()
    l5_btn_exit.draw()
    l5_txt_exit.draw()
    l5_feedback.draw()
    
    win.flip()

    if my_mouse.isPressedIn(l5_btn_safe):
        l5_feedback.text = "You clicked the GREEN button!"
        l5_feedback.color = [-1, 1, -1]
        while my_mouse.getPressed()[0] == 1: pass 

    if my_mouse.isPressedIn(l5_btn_exit):
        l5_feedback.text = "Exiting..."
        l5_feedback.color = [1, -1, -1]
        l5_feedback.draw()
        win.flip()
        core.wait(1.0)
        lesson_active = False

# ------------------------------------------------------------------
# CLEANUP
# ------------------------------------------------------------------
win.close()
core.quit()