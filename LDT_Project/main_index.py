import os

#import helperFunctions, analytics
os.system('cls' if os.name =='nt' else 'clear')
#from datetime import datetime
from psychopy import logging, visual, core, event, gui
import pandas as pd
import numpy as np

### Key Functions ####
# https://thispointer.com/python-how-to-find-all-indexes-of-an-item-in-a-list/
def get_index_positions(list_of_elems, element):
    index_pos_list = []

    for i in range(len(list_of_elems)):
        if(list_of_elems[i]==element):
            index_pos_list.append(i)
    return index_pos_list

def showTextBox(text1="", text2="", text3=""):
    textBox = gui.Dlg(title='Type your response here')
    textBox.addField('First Name: ', text1)
    textBox.addField('Last Name: ', text2)
    textBox.addField('Age: ', text3)
    textBox.show()
    if textBox.OK:
        text1 = textBox.data[0]
        text2 = textBox.data[1]
        text3 = textBox.data[2]
        return text1, text2, text3
    else:
        return text1, text2, text3

def add_text_to_screen(win, txt, bold=True):
    text_to_screen = visual.TextStim(win, text=txt, bold=bold , pos=(0.0, 0.0), color=(1.0, 1.0, 1.0), wrapWidth=3000)
    text_to_screen.draw()
    return

def add_stimuli_to_screen(win, txt, height, bold=True):
    text_to_screen = visual.TextStim(win, text=txt, bold=bold , pos=(0.0, 0.0), color=(1.0, 1.0, 1.0), wrapWidth=3000, height=height)
    text_to_screen.draw()
    return

def feedback_to_screen(win, txt, bold, height=40):
    text_to_screen = visual.TextStim(win, text=txt, bold=bold , height = height, pos=(0.0, 0.0), color=(1.0, 1.0, 1.0))
    text_to_screen.draw()
    return

def cross_to_screen(win, txt, cross='X'):
    text_to_screen = visual.TextStim(win, text=txt, bold=True , pos=(0, 100), color=(1.0, 1.0, 1.0))
    text_to_screen.draw()
    text_to_screen = visual.TextStim(win, text=cross, bold=True , height = 60, pos=(0.0, 0.0), color=(1.0, 1.0, 1.0))
    text_to_screen.draw()
    return

def add_results_to_screen(win, txt, bold=True):
    text_to_screen = visual.TextStim(win, text=txt, bold=bold , pos=(0.0, 0.0), color=(1.0, 1.0, 1.0), wrapWidth=3000)
    text_to_screen.draw()
    return

### End Key Functions ####

# Reading stimulus data
stimulus_data = pd.read_csv("word_dataset_80.csv", delimiter='\t')
#print(stimulus_data)
stimulus_data = stimulus_data.sample(frac=1)
#print(stimulus_data)
#print(stimulus_data)
# word_1	word_2	condition	WUP_score	correct_incorrect
word_1 = stimulus_data["word_1"].to_list()
word_2 = stimulus_data["word_2"].to_list()
condition = stimulus_data["condition"].to_list()
WUP_score = stimulus_data["WUP_score"].to_list()
correct_incorrect = stimulus_data["correct_incorrect"].to_list()


for i in range(1, 5):
    print(get_index_positions(condition, i))
#print(word_1,	word_2,	condition,	WUP_score,	correct_incorrect)

#block_number_output = []
key_pressed = []
reaction_time = []
response_status = []
age_list = []
# Setting logging to Critical
logging.console.setLevel(logging.CRITICAL)
first_name, last_name, age = showTextBox("Siddharth", "Gupta", 22)

start_t = core.MonotonicClock()
monitor_resolution_x = 1920 #960
monitor_resolution_y = 1080 #540
screen_size_x = 1400
screen_size_y = 1000
screen_x_start = (monitor_resolution_x - screen_size_x)/2
screen_y_start = (monitor_resolution_y - screen_size_y)/2

win0 = visual.Window(screen =1 , size = (screen_size_x, screen_size_y), units='pix', 
monitor='testMonitor', color=(-1, -1, -1), pos = (screen_x_start, screen_y_start))

##### Instruction Screen ######
welcome_string = "Welcome %s %s! \n\n In this task, you will see two words at the time. If both words are REAL ENGLISH words, you press the button 'y'. \nIf ONE or BOTH words are non-sense words (for example 'FLUMMOL'), you press the button 'n'. \n\nRespond within 2 seconds. \n\nPress space bar to start the test." % (first_name, last_name)
add_text_to_screen(win0, welcome_string)
win0.flip()

space_reader_tuple =  event.waitKeys(maxWait=100000, keyList=['space'], timeStamped= True, clearEvents=True)

##### End Instruction Screen #####

#### Trial Block ######
#### End Trial Block ######

#### Here's our X, look here maybe ######
cross_instructions = "The words will appear here (at the position of X on this page), Press Space to continue \n\n"
cross_to_screen(win0, cross_instructions, 'X')
win0.flip()

space_reader_tuple =  event.waitKeys(maxWait=100000, keyList=['space'], timeStamped= True, clearEvents=True)


#### End X ######

for i in range(len(word_1)):
    age_list.append(age)
    stimuli_string = word_1[i].upper() + "\n" + word_2[i].upper() 
    add_stimuli_to_screen(win0, stimuli_string, 60)
    win0.flip()
    start_t = core.MonotonicClock()
    key_pressed_tuple =  event.waitKeys(maxWait=2, keyList=['y', 'n'], timeStamped= True, clearEvents=True)
    time_taken_to_click = start_t.getTime()
    #print(key_pressed_tuple[0][0], key_pressed_tuple[0][1])
    key_pressed_rn = '0'

    if(key_pressed_tuple == None):
        response_status.append(2) #Time out case = 2
        reaction_time.append(2000)
        feedback_to_screen(win0, txt = "Too slow", bold= False)
        win0.flip()
        temp_key_tuple = event.waitKeys(maxWait=0.2)
        print(response_status)
        print(reaction_time)

    else:
        key_pressed_rn = key_pressed_tuple[0][0]
        if((key_pressed_tuple[0][0] == 'y' and correct_incorrect[i] == 1) or (key_pressed_tuple[0][0] == 'n' and correct_incorrect[i] == 0)):
            print(key_pressed_tuple)
            response_status.append(1)
            reaction_time.append(time_taken_to_click*1000)
            feedback_to_screen(win0, txt = "Correct!", bold= False)
            win0.flip()
            temp_key_tuple = event.waitKeys(maxWait=0.2)
            print(response_status)
            print(reaction_time)

        else:
            print(key_pressed_tuple)
            response_status.append(0)
            reaction_time.append(time_taken_to_click*1000)
            feedback_to_screen(win0, txt = "Incorrect!", bold= False)
            win0.flip()
            temp_key_tuple = event.waitKeys(maxWait=0.1)
            print(response_status)
            print(reaction_time)
        
    key_pressed.append(key_pressed_rn)

    
csv_filename = "participants_data/" + first_name + '_' + last_name + '_' + str(age) +".csv"
all_data = [word_1,	word_2,	condition,	WUP_score,	correct_incorrect, key_pressed, reaction_time, response_status, age_list]

for i in all_data:
    print(len(i))


data = pd.DataFrame({"word_1":word_1, "word_2":word_2, "condition":condition, "WUP_score":WUP_score, "correct_incorrect":correct_incorrect,
"key_pressed":key_pressed, "response_status":response_status, "reaction_time":reaction_time, "age_list":age_list})

data.to_csv(csv_filename, index=False)

    #mazak = input("hey mazak")

case_1_indices = get_index_positions(condition, 1)
case_2_indices = get_index_positions(condition, 2)
case_3_indices = get_index_positions(condition, 3)
case_4_indices = get_index_positions(condition, 4)

case_1_accuracy = np.sum([response_status[i]%2 for i in case_1_indices])/20
case_2_accuracy = np.sum([response_status[i]%2 for i in case_2_indices])/20
case_3_accuracy = np.sum([response_status[i]%2 for i in case_3_indices])/20
case_4_accuracy = np.sum([response_status[i]%2 for i in case_4_indices])/20

accuracy_text = '''The accuracy of participants for different cases (In percentage) \n\n\n
Semantically closer real words %s \n\n
Semantically closer but shuffled second word (first and last letter in correct position) %s \n\n
Semantically closer but shuffled second word %s \n\n
Semantically far real words %s \n\n
''' % (case_1_accuracy*100, case_2_accuracy*100, case_3_accuracy*100, case_4_accuracy*100)

add_results_to_screen(win0, accuracy_text)
win0.flip()
space_reader_tuple =  event.waitKeys(maxWait=1000000, keyList=['space'], timeStamped= True, clearEvents=True)

win0.close()
core.quit()