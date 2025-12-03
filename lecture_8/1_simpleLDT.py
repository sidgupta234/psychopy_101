# Minimal PsychoPy Lexical Decision Task

import os
from psychopy import visual, core, event, gui # Core modules for psychophysics
import pandas as pd # For data handling/saving
import numpy as np  # For numerical operations

# "core" contains various functions used for timing and quitting the experiment.
# "gui" allows you to create a dialog box to collect participant information
# "visual" allows you to draw various stimuli
# "event" allows you to collect responses

# --- 1. Stimuli Data Setup (5 Trials) ---
word_1 = ['tea', 'doctor', 'bread', 'truck', 'fruit']
word_2 = ['coffee', 'shampoo', 'buettr', 'ilevehc', 'orange']
condition = [1, 4, 2, 3, 1]
correct_incorrect = [1, 1, 0, 0, 1]

print(f"DEBUG: Stimuli data loaded. Total trials: {len(word_1)}")

# --- 2. Setup and Initialization ---
# Get participant info using a simple dialog box
info_dlg = gui.Dlg(title='Participant Info')
info_dlg.addField('Name: ', 'Tester')
info_dlg.show()
name = info_dlg.data[0] 
print(f"DEBUG: Participant Name captured: {name}")

# Initialize the main experiment window (800x600 pixels)
win0 = visual.Window(size=(800, 600), units='pix', color=(-1, -1, -1))
print("DEBUG: PsychoPy Window initialized.")

# Define reusable text objects (TextStim)
text_stimulus = visual.TextStim(win0, text='', bold=True, pos=(0.0, 0.0), color=(1.0, 1.0, 1.0), height=60)
feedback_stim = visual.TextStim(win0, text='', bold=False, pos=(0.0, 0.0), color=(1.0, 1.0, 1.0), height=40)
welcome_text = visual.TextStim(win0, text='''You will be shown two words, press "y" if both are legit, "n" if not both legit,
                               Press space to start the 5-trial test!''', bold=True, pos=(0.0, 0.0), color=(1.0, 1.0, 1.0))

# Lists to store the results collected during the experiment
key_pressed = []
reaction_time = []
response_status = [] # 1=Correct, 0=Incorrect, 2=Timeout

# Show Start Screen
welcome_text.draw()
win0.flip()
print("DEBUG: Instruction screen displayed. Waiting for SPACE key.")
event.waitKeys(keyList=['space'])
print("DEBUG: SPACE key pressed. Starting trials.")

# --- 3. The Core Trial Loop (5 iterations) ---

for i in range(len(word_1)):
    trial_num = i + 1
    print(f"\nDEBUG: --- Starting Trial {trial_num} ---")
    
    # 3.1 Display Stimuli
    current_word_1 = word_1[i].upper()
    current_word_2 = word_2[i].upper()
    current_condition = condition[i]
    
    # Set the word pair text and draw it
    text_stimulus.text = current_word_1 + "\n" + current_word_2
    text_stimulus.draw()
    win0.flip() # Show the words immediately
    print(f"DEBUG: Displaying stimuli: {current_word_1} / {current_word_2} (Condition: {current_condition})")

    # 3.2 Wait for Response
    start_t = core.MonotonicClock() # Start the trial timer
    print(f"DEBUG: Clock started at {start_t.getTime():.4f} seconds.")
    
    # MODIFICATION: Removed timeStamped=True. The output will now be a list of strings (keys).
    key_pressed_list = event.waitKeys(maxWait=2, keyList=['y', 'n'])
    
    # Get the elapsed time since the clock started. This is the RT.
    time_taken = start_t.getTime() 
    key_pressed_rn = '0' # Default key press for timeout
    
    current_correct_answer = correct_incorrect[i]
    
    # 3.3 Process and Store Results
    if key_pressed_list == None: # key_pressed_list will be None if maxWait is reached
        # Case A: Timeout (2)
        response_status.append(2)
        reaction_time.append(2000) # Store 2000ms (2 seconds) for a timeout
        feedback_stim.text = "Too slow! (Trial %d)" % trial_num
        print(f"DEBUG: Timeout (Reaction Time: 2000ms). Correct answer was {current_correct_answer}.")
        
    else:
        # Case B: Response made
        # MODIFICATION: We now access the key directly from the list's first element [0]
        key_pressed_rn = key_pressed_list[0]
        print(f"DEBUG: key pressed data: {key_pressed_list}") 
        reaction_time.append(time_taken * 1000) # Store time in ms

        # Check for correctness
        is_correct = (key_pressed_rn == 'y' and current_correct_answer == 1) or \
                     (key_pressed_rn == 'n' and current_correct_answer == 0)
        
        if is_correct:
            response_status.append(1) # Correct (1)
            feedback_stim.text = "Correct! (Trial %d)" % trial_num
            print(f"DEBUG: Correct response '{key_pressed_rn}' (RT: {reaction_time[-1]:.0f}ms).")
        else:
            response_status.append(0) # Incorrect (0)
            feedback_stim.text = "Incorrect! (Trial %d)" % trial_num
            print(f"DEBUG: INCORRECT response '{key_pressed_rn}' (RT: {reaction_time[-1]:.0f}ms). Correct was {current_correct_answer}.")
        
    key_pressed.append(key_pressed_rn)
    
    # 3.4 Show Feedback and Pause
    feedback_stim.draw()
    win0.flip()
    core.wait(0.5)

# --- 4. Data Saving and Exit ---

# Create DataFrame to organize all collected data
data = pd.DataFrame({
    "word_1": word_1, 
    "word_2": word_2, 
    "condition": condition, 
    "correct_incorrect": correct_incorrect,
    "key_pressed": key_pressed, 
    "response_status": response_status, 
    "reaction_time": reaction_time, 
})

# Create the save folder and filename using the user's name
data_folder = 'participants_data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    print(f"DEBUG: Created directory '{data_folder}'")
    
csv_filename = os.path.join(data_folder, name.replace(' ', '_') + '_LDT_results.csv')
data.to_csv(csv_filename, index=False)

print(f"\nDEBUG: --- Data Saving Complete ---")
print(f"DEBUG: Data saved to: {csv_filename}")
print("\n--- Final Results (5 Trials) ---\n")
print(data)
print("\n-------------------------------\n")

# Show End Screen
welcome_text.text = "5 Trials Complete! Data saved as %s. Press space to exit. " % os.path.basename(csv_filename)
welcome_text.draw()
win0.flip()
event.waitKeys(keyList=['space'])

print("DEBUG: SPACE pressed on end screen. Shutting down.")
win0.close()
core.quit()

# // 1. SETUP & STIMULI
# DEFINE stimuli_list (words, images, or conditions for the trials)
# CREATE empty list called 'experiment_data' to store results
# # Also can define here parameters that will remain constant throughout the experiment
# WIN_SIZE = [800, 600]
# BACKGROUND_COLOR = [-1, -1, -1] # Black in PsychoPy
# TEXT_COLOR = [1, 1, 1]          # White
# MAX_WAIT_TIME = 2.0             # Max time to wait for a keypress
# FIXATION_TIME = 0.5             # How long the crosshair stays on screen

# // 2. PARTICIPANT INFO
# SHOW dialog box ("Enter Participant ID", "Session Number")
# WAIT for user to click OK
# STORE participant_info variables

# // 3. CREATE WINDOW
# OPEN Window (width, height, background_color, units)
# DEFINE text_stimulus (for instructions and trials)
# DEFINE feedback_stimulus (for correct/incorrect/timeout messages)

# // 4. INSTRUCTIONS
# SET text_stimulus content to "Welcome. Press SPACE to start."
# DRAW text_stimulus
# FLIP Window (to show it on screen)
# WAIT for key press ("space")

# // 5. EXPERIMENT LOOP
# FOR EACH trial IN stimuli_list:

#     // A. Prepare Trial
#     UPDATE text_stimulus with current trial information
    
#     // B. Show Stimulus
#     DRAW text_stimulus
#     FLIP Window
#     RESET Clock (Start timing exactly when screen flips)
    
#     // C. Listen for Response (The Key Press Cycle)
#     LISTEN for keys (valid keys: 'a', 'l', 'escape') with MAX_WAIT time
    
#     // D. Analyze Response
#     IF key was pressed:
#         RECORD Reaction Time (RT) = time elapsed on Clock
        
#         IF key matches Correct Answer:
#             SET response_status = "Correct"
#         ELSE IF key is 'escape':
#             QUIT experiment
#         ELSE:
#             SET response_status = "Incorrect"
            
#     ELSE (if time ran out):
#         SET response_status = "Timeout"
#         SET RT = MAX_WAIT
        
#     // E. Save Trial Data to Memory
#     APPEND [Participant ID, Trial Name, Key Pressed, RT, Status] to 'experiment_data'
    
#     // F. Optional: Show Feedback or Clear Screen
#     DRAW feedback (based on status)
#     FLIP Window
#     WAIT (Inter-trial interval)

# // 6. SAVE DATA
# CONVERT 'experiment_data' into a file format (CSV or Excel)
# NAME file using "Participant_ID" + "Date"
# SAVE file to disk

# // 7. CLEANUP
# CLOSE Window
# EXIT Python