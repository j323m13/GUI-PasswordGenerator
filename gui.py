from tkinter.ttk import Style
from guizero import *
import password_generator

# generate and display a random string password
def display_new_string_password(numberOfChar):
    new_password_string =  password_generator.generate_password(password_generator.build_string,int(numberOfChar))
    message_password.value = str(new_password_string)

# generate and display a random words password
def display_new_words_password():
    WORDS = []
    WORDS = password_generator.build_word_password()
    new_password_string =  password_generator.generate_word_password(WORDS,4)
    message_password.value = str(new_password_string)

# check if the checkbox is equals to 1 or 0. 
# controll if the number of chars is not null or not a negative intergers
# call the string or words password generator display methods
def generate_pwd():
    numberOfChar = set_numberOfChar.value
    checkbox = set_checkbox.value
    if(checkbox==1):
       display_new_words_password()
    elif(int(numberOfChar)<0):
        message_password.value = "negative integer."
    elif(numberOfChar==""):
        message_password.value = "give the length of the password."
    elif(int(numberOfChar)== 0):
        message_password.value ="why 0?"
    else:
        display_new_string_password(numberOfChar)

## set GUI Elements (widgets)       
app = App(title="Password generator")
app.bg = "white"

# set alignment
title_box = Box(app, width="fill", align="top")
center_box = Box(app, width="fill", layout="grid")
button_box = Box(app, width="fill", align="bottom")

# set all the widgets
message_welcome = Text(title_box, text="Click to generate a random password!\n", align="center")
message_welcome.text_size = 15
set_checkbox = CheckBox(title_box, text="words passphrase?")
lowerCase_label = Text(center_box, text="Lower case:", grid=[0,0])
message_lowerCase = Text(center_box, text=password_generator.lowerCase, grid=[1,0], align="left")
upperCase_label = Text(center_box, text="Upper case:", grid=[0,1])
message_upperCase = Text(center_box, text=password_generator.upperCase, grid=[1,1], align="left")
specialChars = Text(center_box, text="Special chars:", grid=[0,2])
message_specialChar = Text(center_box, text=password_generator.specialChar, grid=[1,2], align="left")
numbres = Text(center_box, text="Numbers:", grid=[0,3])
message_numbers = Text(center_box, text=password_generator.numbers, grid=[1,3], align="left")

numberOfChar_label = Text(center_box, text="Set number of chars:", grid=[0,4])
set_numberOfChar = TextBox(center_box, grid=[1,4], align="left")

password_label = Text(center_box, text="Your generated password: ", grid=[0,5])
message_password = Text(center_box, text="\n", grid=[1,5], align="left")
message_password.text_color = "red"

# spacer (not pretty)
spacer = Text(center_box, text="", grid=[0,6])

# a picture because I wanted to try it (and it helps to know what is a good password.)
picture = Picture(app, image="python\GUI-PasswordGenerator\img\password_strength_small_small.png", width=400, height=325)

# press it
button = PushButton(button_box, text="Generate PW", command=generate_pwd)

# set app widht and height and start the window
app.width = 600
app.height = 650
app.display()