"""
EXERCISE: THE TRAFFIC LIGHT TEST
================================

YOUR GOAL:
1. Create a "Red Light" test:
   - Draw a RED circle.
   - Wait 2.0 seconds using event.waitKeys(maxWait=2.0).
   - If the user presses ANY key during this time, print "FAIL: You ran the red light!"
   - If the user waits the full 2 seconds (returns None), print "PASS: Good stop."

2. Immediately follow with a "Green Light" test:
   - Draw a GREEN circle.
   - Wait 2.0 seconds using event.waitKeys(maxWait=2.0).
   - If the user presses a key, print "PASS: Good reaction!"
   - If the user does NOT press a key (returns None), print "FAIL: You fell asleep!"


EXERCISE 2: THE HOVER EFFECT (SIMPLIFIED)
=========================================

YOUR GOAL:
1. Create a static white Square in the center of the screen.
2. Create a Mouse object.
3. Create a loop that runs until 'q' is pressed.
4. INSIDE THE LOOP:
   - Check if the Mouse is currently inside the Square.
   - If YES: Change the Square's color to GREEN.
   - If NO: Change the Square's color back to WHITE.
   - Draw the square and flip the window.

HINT:
You do not need to track X/Y coordinates manually! 
You can simply pass the mouse object directly to the contains method:
if my_square.contains(my_mouse):
"""