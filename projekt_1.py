"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""
import task_template as texts 


user = ['bob', 'mike', 'ann', 'liz']
password = ['123', 'pass123', 'password123', 'pass123']
# text has 3 indices
text = texts.TEXTS
text_dic = {}

# creates dictionary out of text list
for items in range(len(text)):
    text_dic[items] = text[items]



# user_input = input(str('Hello, please insert your user name and password (separated by whitespace): '))
# user_input_list = user_input.split(' ')


for k, v in text_dic.items():
    print(k+1)
    print('')
    print(v + '\n')


# try:
#     user_name = user_input_list[0]
#     user_pass = user_input_list[1]

# except IndexError:
#     print('Please insert also your password.')

# if user_name in user and user_pass in password:
#     print(f'Hello user {user_name.capitalize()}')

# else: 
#     print('Wrong user name or password. The program has been terminated')