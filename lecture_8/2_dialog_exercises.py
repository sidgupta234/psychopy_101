# Exercise 1: The Experiment Startup Screen

# Goal: Create a dialog that captures a mix of text, categorical choice, and boolean (yes/no) data, then accesses that data from the list.

# Instructions:

#     Create a gui.DlgWith the title "Experiment Setup".

#     Add a field for "Participant ID" (text input).

#     Add a field for "Condition" that selects that simply 'Control' or 'Treatment' (dropdown).

#     Add a field for "Full Screen Mode?" default that to unchecked (checkbox).

#     Show the dialog and store the result in a variable exp_info.

#     Challenge: Print a sentence using the data, like: "Participant [ID] is in the [Condition] group."

# Exercise 2: The "Locked" Settings Menu

# Goal: Use advanced features like disabled fields, colors, tooltips, and required fields.

# Instructions:

#     Create a gui.Dlgwith the title "Lab Configuration".

#     Add a field "Lab ID" with the value LAB-001. Make this field disabled (read-only) so the user cannot change it.

#     Add a field "Experiment Name". Make the text blue and add a tooltip that says "Enter your initials".

#     Add a field "Session Number". Make this field Required (the dialog should't close if this is empty).

#     Show the dialog.

#     Check if the user pressed OK. If they did, print "Configuration Saved." If they pressed Cancel, print "Setup Aborted".