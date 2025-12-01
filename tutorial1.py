from psychopy import logging, visual, core, event, gui
import pandas as pd
import numpy as np


# "core" contains various functions used for timing and quitting the experiment.
# "gui" allows you to create a dialog box to collect participant information
# "visual" allows you to draw various stimuli
# "event" allows you to collect responses

stimulus_data = pd.read_csv("LDT_Project/word_dataset_80.csv", delimiter='\t')

textBox = gui.Dlg(title='Type your response here')
textBox.addField('First Name')
textBox.addField('Last Name')
textBox.addField('Age')
show_dlg = textBox.show()

print(show_dlg)

text1 = textBox.data[0]
text2 = textBox.data[1]
text3 = textBox.data[2]

core.quit()
# you can save your file of reaction data
# using the combination of these things to annotate


# With default values
# textBox = gui.Dlg(title='Type your response here')
# textBox.addField('First Name: ', "Siddharth")
# textBox.addField('Last Name: ', "Gupta")
# textBox.addField('Age: ', "100")
# textBox.show()

# text1 = textBox.data[0]
# text2 = textBox.data[1]
# text3 = textBox.data[2]

# With more fields..
# my_dlg = gui.Dlg(title="my experiment")
# my_dlg.addText('exp_info')
# my_dlg.addField('age:',0)
# my_dlg.addField('gender:', choices=['female', 'male', 'other', 'prefer not to say'])
# my_dlg.addField('handedness:', choices=['right', 'left'])
# my_dlg.addField('subject_nr:',0)
# show_dlg = my_dlg.show()


# Dialog from Dict

# exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
#             'gender':('male','female','other','prefer not to say')}

# my_dlg = gui.DlgFromDict(dictionary=exp_info)
# show_dlg = my_dlg.show()