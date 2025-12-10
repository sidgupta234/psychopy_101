# --- SOLUTION ---

from psychopy import visual, core, event

# Setup
win = visual.Window(size=[600, 600], units="pix", color=[0, 0, 0])

# --- PART 1: RED LIGHT (Test inhibition) ---

# Draw Red Light
red_light = visual.Circle(win, radius=100, fillColor='red', lineColor='red')
text_stop = visual.TextStim(win, text="STOP! (Don't press)", pos=(0, 150))

red_light.draw()
text_stop.draw()
win.flip()

# Wait for 2 seconds max
keys = event.waitKeys(maxWait=2.0)

# Logic: We want keys to be None (meaning time ran out)
if keys is None:
    feedback = "PASS: Good stop."
    print(feedback)
else:
    feedback = "FAIL: You ran the red light!"
    print(feedback)

# Show feedback briefly
visual.TextStim(win, text=feedback).draw()
win.flip()
core.wait(1.5)

# --- PART 2: GREEN LIGHT (Test reaction) ---

# Draw Green Light
green_light = visual.Circle(win, radius=100, fillColor='green', lineColor='green')
text_go = visual.TextStim(win, text="GO! (Press Space)", pos=(0, 150))

green_light.draw()
text_go.draw()
win.flip()

# Wait for 2 seconds max
keys = event.waitKeys(maxWait=2.0)

# Logic: We want keys to NOT be None (meaning they pressed something)
if keys is None:
    feedback = "FAIL: You fell asleep!"
    print(feedback)
else:
    feedback = "PASS: Good reaction!"
    print(feedback)

# Show feedback briefly
visual.TextStim(win, text=feedback).draw()
win.flip()
core.wait(1.5)

win.close()
core.quit()