from psychopy import gui, core

# 1. Create Dialog
startupDlg = gui.Dlg(title="Experiment Setup")

# 2. Add Fields
startupDlg.addField("Participant ID")
startupDlg.addField("Condition", choices=["Control", "Treatment"])
startupDlg.addField("Full Screen Mode?", initial=False)

# 3. Show and Capture
exp_info = startupDlg.show()

# 4. Process Data (Check if OK was pressed)
if startupDlg.OK:
    # exp_info is a list: [ID, Condition, FullScreenBool]
    p_id = exp_info[0]
    condition = exp_info[1]
    
    print(f"Participant {p_id} is in the {condition} group.")
else:
    print("User cancelled the experiment.")

print(exp_info)