from psychopy import gui, core

# 1. Create Dialog
configDlg = gui.Dlg(title="Lab Configuration")

# 2. Add Disabled Field (Read-only)
configDlg.addField("Lab ID", initial="LAB-001", enabled=False)

# 3. Add Styled Field (Color + Tooltip)
configDlg.addField("Experimenter Name", color="blue", tip="Enter your initials")

# 4. Add Required Field
configDlg.addField("Session Number", required=True)

# 5. Show Dialog
result = configDlg.show()

# 6. Check Logic
if configDlg.OK:
    print("Configuration Saved")
    print("Session:", result[2]) # Index 2 is the session number
else:
    print("Setup Aborted")