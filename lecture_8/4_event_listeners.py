"""
PSYCHOPY EVENT LISTENER
=======================================

This script is a comprehensive guide to the `psychopy.event` module.
It covers:
1. Blocking Keyboard Input (Pausing the experiment)
2. Reaction Times & Timed Input (Recording data)
3. Non-Blocking Input (Real-time movement)
4. Mouse Tracking (Coordinates)
5. Object Interaction (Clicking specific buttons)

"""

# --- IMPORTS ---
from psychopy import visual, core, event, gui
import sys

# --- SETUP: WINDOW & CONSTANTS ---

# Define some useful colors (R, G, B) in PsychoPy's -1 to +1 scale
BLACK = [-1, -1, -1]
WHITE = [1, 1, 1]
GREEN = [-1, 1, -1]
RED   = [1, -1, -1]
BLUE  = [-1, -1, 1]

print("--- Initializing Window ---")
# We create a window 1024x768. 'fullscr=False' makes it easier to close if it crashes.
win = visual.Window(
    size=[1024, 768],
    units="pix",       # We use pixels for easy coordinate understanding
    color=BLACK,       # Background color
    fullscr=False,     
    title="Event Listener Tutorial"
)

# A generic text object we will reuse to give instructions
instr_text = visual.TextStim(
    win, 
    text="", 
    pos=(0, 200), 
    height=30, 
    color=WHITE,
    wrapWidth=900
)

# A generic feedback object for showing what you pressed
feedback_text = visual.TextStim(
    win, 
    text="", 
    pos=(0, 0), 
    height=40, 
    color=GREEN
)

# ------------------------------------------------------------------
# LESSON 1: THE BASICS - Blocking Input (event.waitKeys)
# ------------------------------------------------------------------
# Concept: "Blocking" means the code stops (hangs) at that line 
# until the event happens. This is used for instructions.

instr_text.text = (
    "LESSON 1: Blocking Input\n\n"
    "The script is currently PAUSED using event.waitKeys().\n"
    "Nothing else will happen until you press a specific key.\n\n"
    "Press the 'LEFT' or 'RIGHT' arrow key to continue."
)
instr_text.draw()
win.flip() # Flip puts the drawing onto the physical screen

# event.waitKeys() pauses the script.
# keyList=['left', 'right'] means ONLY those keys will trigger the next line.
# Pressing 'space' or 'a' here will do nothing.
keys = event.waitKeys(keyList=['left', 'right'])

# 'keys' is a LIST of strings, e.g., ['left']
feedback_text.text = f"Great! You pressed: {keys[0]}"
feedback_text.draw()
win.flip()
core.wait(2.0) # Wait 2 seconds so you can read the feedback

# ------------------------------------------------------------------
# LESSON 2: REACTION TIME - Timed Input & Data Capture
# ------------------------------------------------------------------
# Concept: Measuring how fast someone responds. We need the Key AND the Time.

instr_text.text = (
    "LESSON 2: Reaction Time (Data Capture)\n\n"
    "When the screen turns GREEN, press 'SPACE' as fast as you can.\n"
    "You have a 2-second time limit.\n\n"
    "Press any key to start the countdown."
)
instr_text.draw()
win.flip()
event.waitKeys() # Wait for ANY key

# Countdown
for i in [3, 2, 1]:
    feedback_text.text = str(i)
    feedback_text.color = WHITE
    feedback_text.draw()
    win.flip()
    core.wait(1.0)

# Change screen to green stimulus
circle = visual.Circle(win, radius=50, fillColor=GREEN, lineColor=GREEN)
circle.draw()
win.flip()

# Start a high-precision clock exactly when we flip the screen
rt_clock = core.Clock()

# event.waitKeys parameters:
# 1. maxWait=2.0: If no key is pressed in 2s, it returns None.
# 2. timeStamped=rt_clock: Returns a tuple (key, time_relative_to_clock)
# 3. keyList=['space']: Only accept spacebar
user_response = event.waitKeys(maxWait=2.0, keyList=['space'], timeStamped=rt_clock)

# Check results
if user_response is None:
    # This happens if 2 seconds passed with no input
    feedback_text.text = "Too slow! (Timed out)"
    feedback_text.color = RED
else:
    # user_response looks like: [['space', 0.452]]
    key_name = user_response[0][0] # The key ('space')
    rt_time  = user_response[0][1] # The time (e.g., 0.452)
    
    feedback_text.text = f"Got it! RT: {rt_time:.3f} seconds"
    feedback_text.color = WHITE

feedback_text.draw()
win.flip()
event.waitKeys() # Wait for user to read feedback

# ------------------------------------------------------------------
# LESSON 3: REAL-TIME - Non-Blocking Input (event.getKeys)
# ------------------------------------------------------------------
# Concept: "Polling". We check if a key is pressed, but if not, 
# we keep running the code (drawing frames). This allows animation.

instr_text.text = (
    "LESSON 3: Real-Time Movement (Non-Blocking)\n\n"
    "Use Arrow Keys (Up/Down/Left/Right) to move the blue square.\n"
    "Press 'Q' to finish this lesson."
)

# Create a character to move
player = visual.Rect(win, width=50, height=50, fillColor=BLUE)
player_pos = [0, 0] # Start center

# We use a While loop to create an animation frame
# We must clear old keystrokes first so the square doesn't jump immediately
event.clearEvents() 

lesson_active = True
while lesson_active:
    # 1. Draw instructions and player
    instr_text.draw()
    player.pos = player_pos
    player.draw()
    win.flip()

    # 2. Check for keys WITHOUT pausing (getKeys vs waitKeys)
    # This returns immediately, even if the list is empty.
    keys_pressed = event.getKeys(keyList=['left', 'right', 'up', 'down', 'q'])

    # 3. Process inputs
    if 'q' in keys_pressed:
        lesson_active = False # Break the loop
    
    if 'left' in keys_pressed:
        player_pos[0] -= 20 # Move x left
    if 'right' in keys_pressed:
        player_pos[0] += 20 # Move x right
    if 'up' in keys_pressed:
        player_pos[1] += 20 # Move y up
    if 'down' in keys_pressed:
        player_pos[1] -= 20 # Move y down

feedback_text.text = "Movement Demo Complete!"
feedback_text.color = WHITE
feedback_text.draw()
win.flip()
core.wait(1.5)

# ------------------------------------------------------------------
# LESSON 4: THE MOUSE - Tracking Coordinates
# ------------------------------------------------------------------
# Concept: Using the visual.CustomMouse object or event.Mouse

instr_text.text = (
    "LESSON 4: Mouse Tracking\n\n"
    "Move your mouse. The text will show coordinates.\n"
    "Click the LEFT mouse button to finish."
)

# Create the mouse object
# visible=False would hide the standard cursor (good for experiments)
my_mouse = event.Mouse(visible=True, win=win)

# Reset any previous clicks so we don't accidentally skip
my_mouse.clickReset()

lesson_active = True
while lesson_active:
    # 1. Get Mouse Position (x, y)
    mouse_x, mouse_y = my_mouse.getPos()

    # 2. Get Mouse Buttons
    # Returns [Left_Pressed, Center_Pressed, Right_Pressed] (0 or 1)
    buttons = my_mouse.getPressed()
    
    # 3. Update Text
    feedback_text.text = f"X: {mouse_x:.0f}, Y: {mouse_y:.0f}"
    feedback_text.pos = (0, 0)
    
    # Draw elements
    instr_text.draw()
    feedback_text.draw()
    win.flip()

    # 4. Check for exit condition (Left Click)
    if buttons[0] == 1: # buttons[0] is Left Click
        lesson_active = False

core.wait(0.5) # Slight pause to prevent accidental double clicks

# ------------------------------------------------------------------
# LESSON 5: MOUSE INTERACTION - Clicking Objects (isPressedIn)
# ------------------------------------------------------------------
# Concept: Detecting if the mouse was clicked specifically INSIDE a shape.

instr_text.text = (
    "LESSON 5: Clicking Objects\n\n"
    "There are two buttons below.\n"
    "Click the RED button to exit the tutorial."
)

# Create two buttons
btn_safe = visual.Rect(win, width=150, height=80, pos=(-200, -100), fillColor=GREEN)
txt_safe = visual.TextStim(win, text="Stay", pos=(-200, -100), height=25)

btn_exit = visual.Rect(win, width=150, height=80, pos=(200, -100), fillColor=RED)
txt_exit = visual.TextStim(win, text="EXIT", pos=(200, -100), height=25)

my_mouse.clickReset() # Reset mouse state again

lesson_active = True
while lesson_active:
    # Check if the mouse is hovering over buttons (for visual effect)
    if btn_safe.contains(my_mouse):
        btn_safe.opacity = 0.5 # Dim if hovering
    else:
        btn_safe.opacity = 1.0 # Full brightness

    if btn_exit.contains(my_mouse):
        btn_exit.opacity = 0.5
    else:
        btn_exit.opacity = 1.0

    # Draw everything
    instr_text.draw()
    btn_safe.draw()
    txt_safe.draw()
    btn_exit.draw()
    txt_exit.draw()
    
    # Show status message
    feedback_text.pos = (0, -250)
    feedback_text.draw()
    
    win.flip()

    # Check for clicks using isPressedIn
    # This checks: 1. Is the button currently down? AND 2. Is it inside this shape?
    if my_mouse.isPressedIn(btn_safe):
        feedback_text.text = "You clicked the GREEN button!"
        feedback_text.color = GREEN
        
        # Important: Wait until button is released so we don't register 60 clicks a second
        while my_mouse.getPressed()[0] == 1:
            pass 

    if my_mouse.isPressedIn(btn_exit):
        feedback_text.text = "Exiting..."
        feedback_text.color = RED
        feedback_text.draw()
        win.flip()
        core.wait(1.0)
        lesson_active = False

# ------------------------------------------------------------------
# CLEANUP
# ------------------------------------------------------------------
# Always close the window and quit core to free up your computer's resources
win.close()
core.quit()