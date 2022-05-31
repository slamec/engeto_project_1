"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""

from tkinter import E
import task_template as texts 


user = ['bob', 'mike', 'ann', 'liz']
password = ['123', 'pass123', 'password123', 'pass123']
text = texts.TEXTS

user_input = input(str('Hello, please insert your user name and password (separated by whitespace): '))
user_input_list = user_input.split(' ')

try:
    user_name = user_input_list[0]
    user_pass = user_input_list[1]

except IndexError:
    print('xx')

if user_name in user and user_pass in password:
    pass 

else: 
    print('wrong')