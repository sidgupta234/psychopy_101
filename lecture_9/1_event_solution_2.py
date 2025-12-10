# --- SOLUTION ---

from psychopy import visual, core, event

# 1. Initialize Window
win = visual.Window(size=[600, 600], units="pix", color=[0, 0, 0])

# 2. Create the Static Object (The Button)
# We won't move this one, it stays in the center
button = visual.Rect(win, width=150, height=150, fillColor='white')

# 3. Create Mouse
my_mouse = event.Mouse(win=win, visible=True)

print("--- Starting Hover Exercise ---")

running = True
while running:
    
    # Check for quit key
    if 'q' in event.getKeys():
        running = False

    # --- THE CORE LOGIC ---
    # We ask: Does the 'button' object currently contain the 'mouse'?
    if button.contains(my_mouse):
        button.fillColor = 'green'  # Hovering
    else:
        button.fillColor = 'white'  # Not hovering
    
    # Draw and show
    button.draw()
    win.flip()

win.close()
core.quit()