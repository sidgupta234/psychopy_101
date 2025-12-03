from psychopy import visual, core, event

# 1. Setup
win = visual.Window(size=[800, 600], color=[-1, -1, -1]) # Black

# 2. The Setup Screen
text = visual.TextStim(win, text="Preparing Magic...", color=[1, 1, 1])
text.draw()
win.flip() # User sees this now

# 3. The "Behind the Scenes" work
win.color = [-1, 1, -1] # Set background to Green (in memory)
circle = visual.Circle(win, radius=0.2, fillColor=[1, -1, -1]) # Red Circle
circle.draw() # Draw circle (to back buffer)

# 4. The Suspense
print("Waiting 2 seconds...")
core.wait(2.0) # The screen is STILL showing "Preparing Magic" here!

# 5. The Reveal
win.flip() # NOW the background turns green and circle appears

print("Tada! Press any key to exit.")
event.waitKeys()
win.close()