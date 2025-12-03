"""
PSYCHOPY WINDOW
===============================

1. Basic Setup (Size, Color)
2. The Coordinate Systems (Pixels vs. Normalized)
3. The "Flip" Mechanism (Double Buffering)
4. Dynamic Properties (Changing background on the fly)
5. Aspect Ratios (Height units)

"""

# 1. Import necessary libraries
from psychopy import visual, core, event

# --- Configuration Variables ---
# Define common colors in the PsychoPy -1 to 1 RGB format
BLACK = [-1, -1, -1]
WHITE = [1, 1, 1]
RED   = [1, -1, -1]
BLUE  = [-1, -1, 1]
GREEN = [-1, 1, -1]

# ------------------------------------------------------------------
# LESSON 1: BASIC SETUP - Creating the Canvas
# ------------------------------------------------------------------
print("--- Lesson 1: Basic Window Setup ---")

# 2. Create the main experiment window
# The Window object is the most important part of your experiment.
# It represents the physical screen.

win = visual.Window(
    size=[800, 600],    # [width, height]. We use a smaller window for this demo.
    fullscr=False,      # False = Windowed mode (good for coding). True = Fullscreen (for data).
    units="pix",        # **CRITICAL**: The default unit of measurement. "pix" = pixels.
    color=BLACK,        # Background color (-1 to 1 scale).
    allowGUI=True,      # Show the close button/title bar? (False for final experiments)
    title="Window Tutorial"
)

# Create a text stimulus to talk to the user
# Note: We position it at (0, 0), which is the CENTER of the screen in PsychoPy.
instruction_text = visual.TextStim(
    win,
    text="LESSON 1: The Basic Window\n\n"
         "You are looking at an 800x600 pixel window.\n"
         "The units are set to 'pix'.\n"
         "(0, 0) is the exact center of the screen.\n\n"
         "Press SPACE to learn about Coordinates.",
    color=WHITE,
    height=30
)

# Draw the text to the buffer and flip it to the screen
instruction_text.draw()
win.flip()
event.waitKeys(keyList=['space', 'escape'])


# ------------------------------------------------------------------
# LESSON 2: COORDINATE SYSTEMS - Pixels vs. Normalized
# ------------------------------------------------------------------
# PsychoPy windows can use different "units".
# 1. "pix" (Pixels): Absolute. 400 is 400 pixels right.
# 2. "norm" (Normalized): Relative. -1 is left edge, +1 is right edge.

print("--- Lesson 2: Coordinate Systems ---")

# Let's switch the window units to "norm" dynamically
win.units = "norm"

# Create a square that is positioned using Normalized units
# Position (-0.5, 0.5) means: 
# X = Halfway to the Left (Range is -1 to 1)
# Y = Halfway to the Top (Range is -1 to 1)
norm_square = visual.Rect(
    win,
    width=0.2, height=0.2, # 20% of the screen width/height
    pos=(-0.5, 0.5),       # Top-Left Quadrant
    fillColor=BLUE,
    lineColor=WHITE
)

instruction_text.text = (
    "LESSON 2: Normalized Units ('norm')\n\n"
    "We switched win.units to 'norm'.\n"
    "The BLUE square is at (-0.5, 0.5).\n"
    "In 'norm', edges are always -1 and +1.\n\n"
    "Press SPACE to switch back to Pixels."
)

instruction_text.draw()
norm_square.draw()
win.flip()
event.waitKeys(keyList=['space', 'escape'])

# --- Switch back to Pixels ---

win.units = "pix"

# Create a square positioned using Pixel units
# Position (200, -200) means:
# X = 200 pixels Right
# Y = 200 pixels Down
pix_square = visual.Rect(
    win,
    width=100, height=100, # 100 pixels wide
    pos=(200, -200),       # Bottom-Right Quadrant
    fillColor=RED,
    lineColor=WHITE
)

instruction_text.text = (
    "LESSON 3: Pixel Units ('pix')\n\n"
    "We switched win.units back to 'pix'.\n"
    "The RED square is at (200, -200).\n"
    "These are absolute screen coordinates.\n\n"
    "Press SPACE to learn about The Flip."
)

instruction_text.draw()
pix_square.draw()
win.flip()
event.waitKeys(keyList=['space', 'escape'])


# ------------------------------------------------------------------
# LESSON 3: THE "FLIP" - Double Buffering
# ------------------------------------------------------------------
# PsychoPy uses "Double Buffering".
# Buffer 1: The screen you see.
# Buffer 2: The "Back Buffer" where we draw things hidden from view.
# win.flip() swaps them.

print("--- Lesson 3: The Flip Mechanism ---")

instruction_text.text = (
    "LESSON 3: The Flip\n\n"
    "I am going to draw a GREEN circle.\n"
    "However, I will NOT run win.flip() immediately.\n\n"
    "Press SPACE. The screen will stay black for 2 seconds,\n"
    "THEN the circle will appear."
)
instruction_text.draw()
win.flip()
event.waitKeys(keyList=['space', 'escape'])

# 1. Clear screen (flip a blank screen)
win.flip() 

# 2. Draw the circle (This goes to the hidden Back Buffer)
green_circle = visual.Circle(win, radius=50, fillColor=GREEN)
green_circle.draw()

# 3. Wait (The user sees nothing because we haven't flipped yet!)
core.wait(2.0)

# 4. NOW we flip
win.flip()

# Add explanation text after the circle appears
instruction_text.text = (
    "See?\n"
    "The circle was drawn 2 seconds ago,\n"
    "but you only saw it when I called win.flip().\n\n"
    "Press SPACE to continue."
)
instruction_text.pos = (0, -100) # Move text down
instruction_text.draw()
green_circle.draw() # We must redraw the circle for this new frame!
win.flip()
event.waitKeys(keyList=['space', 'escape'])


# ------------------------------------------------------------------
# LESSON 4: DYNAMIC ATTRIBUTES - Changing the Window
# ------------------------------------------------------------------
# You can change window properties like color while the experiment is running.

print("--- Lesson 4: Dynamic Window Properties ---")

instruction_text.pos = (0, 0) # Reset position
instruction_text.text = (
    "LESSON 4: Dynamic Attributes\n\n"
    "We can change the window background color instantly.\n"
    "Press SPACE to see the window flash."
)
instruction_text.draw()
win.flip()
event.waitKeys(keyList=['space', 'escape'])

# Flash sequence
colors = [RED, BLUE, GREEN, BLACK]

for color in colors:
    win.color = color # Change the window property
    
    instruction_text.text = f"Window Color: {color}"
    instruction_text.draw()
    
    win.flip() # Update the screen to show the new background
    core.wait(0.5)

# ------------------------------------------------------------------
# LESSON 5: "HEIGHT" UNITS - Solving Aspect Ratio
# ------------------------------------------------------------------
# "norm" units stretch if your screen isn't square (making circles look like ovals).
# "height" units scale everything relative to the screen height.

print("--- Lesson 5: Height Units ---")

win.units = "height" # Set units to height

instruction_text.text = (
    "LESSON 5: Height Units\n\n"
    "In 'norm', a square might look rectangular on wide screens.\n"
    "In 'height', (1, 1) is the top/right of a square area.\n"
    "This ensures shapes keep their proportions.\n\n"
    "Press SPACE to exit."
)

# Draw a perfect circle using height units
# radius=0.2 means 20% of the screen height
perfect_circle = visual.Circle(
    win, 
    radius=0.2, 
    pos=(0, 0.25), 
    fillColor=WHITE, 
    lineColor=BLACK
)

instruction_text.draw()
perfect_circle.draw()
win.flip()

# ------------------------------------------------------------------
# CLEAN UP
# ------------------------------------------------------------------
event.waitKeys(keyList=['space', 'escape'])

print("--- Closing Window ---")
win.close()
core.quit()