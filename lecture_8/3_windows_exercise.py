# Exercise 1: The Coordinate Mixer

# Goal: Create a window and place two shapes using different units on the same screen.

#     Create a window of size [800, 600].

#     Set the window units to "pix""pix". Create a Red Square positioned in the Top-Right corner (e.g., [200, 200]).

#     Switch the window to "norm". Create a Blue Circle positioned in the Bottom-Left corner (e.g., [-0.75, -0.75]).

#     Draw both shapes and flip the window to show them simultaneously.

# Exercise 2: The "Magic Trick" (Flip Timing)

# Goal: Prove you understand that draw()does not put things on the screen until flip()is called.

#     Create a window with a Black background.

#     Draw a White Text stimulus that says "Preparing Magic...". Flip the screen so the user sees this.

#     Behind the scenes (Do not flip yet):

#         Change the window color to Green.

#         Draw a Red Circle in the center.

#     Add a core.wait(2.0)before the final flip.

#     Finally, call win.flip().

#         Expected Result: The user sits at "Preparing Magic" for 2 seconds, and then damn eyes a Green screen with a Red Circle.