"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""
from typing import Text
import task_template as texts 


user = ['bob', 'mike', 'ann', 'liz']
password = ['123', 'pass123', 'password123', 'pass123']
# text has 3 indices
text = texts.TEXTS
text_dic = {}

# creates dictionary out of text list
for items in range(len(text)):
    text_dic[items] = text[items]



user_input = input(str('Hello, please insert your user name and password (separated by whitespace): '))
user_input_list = user_input.split(' ')


for k, v in text_dic.items():
    print(k+1)
    print('')
    print(v + '\n')


try:
    user_name = user_input_list[0]
    user_pass = user_input_list[1]

except IndexError:
    print('Please insert also your password.')

if user_name in user and user_pass in password:
    print(f'Hello user {user_name.capitalize()}')
    print('')
    print('Texts to analyze: ')
    print('')

    for k, v in text_dic.items():
        print(k+1)
        print('')
        print(v + '\n')

    text_number = int(input('Insert number of the text to analyze: ')) - 1 

    if text_number == 0:
        # number of words
        print(f'There are {len(text[text_number].split())} words in the selected text.')

        # number of words starting with titlecase
        count_title = 0 
        for i in text[text_number].split():
            if i.istitle():
                count_title += 1
        
        print(f'There are {count_title} titlecase words.')

        # number of words starting with uppercase
        count_upper = 0 
        for i in text[text_number].split():
            if i.isupper() and not i.istitle():
                count_upper += 1        
        
        print(f'There are {count_upper} uppercase words.')

        # number of words starting with lowercase
        count_lower = 0 
        for i in text[text_number].split():
            if i.islower():
                count_lower += 1

        print(f'There are {count_lower} lowercase words.')

        # number of numbers 
        count_digit = 0 
        for i in text[text_number].split():
            if i.isdigit():
                count_digit += 1

        print(f'There are {count_digit} numeric strings.')

        # sum of digits
        total = []

        for d in text[text_number].split():
            if d.isdigit():
        
                total.append(int(d))
        
        print(f'The sum of all the numbers {sum(total)}')


    elif text_number == 1:
        # number of words
        print(f'There are {len(text[text_number].split())} words in the selected text.')

        # number of words starting with titlecase
        count_title = 0 
        for i in text[text_number].split():
            if i.istitle():
                count_title += 1
        
        print(f'There are {count_title} titlecase words.')

        # number of words starting with uppercase
        count_upper = 0 
        for i in text[text_number].split():
            if i.isupper() and not i.istitle():
                count_upper += 1        
        
        print(f'There are {count_upper} uppercase words.')

        # number of words starting with lowercase
        count_lower = 0 
        for i in text[text_number].split():
            if i.islower():
                count_lower += 1

        print(f'There are {count_lower} lowercase words.')    

        # number of numbers 
        count_digit = 0 
        for i in text[text_number].split():
            if i.isdigit():
                count_digit += 1

        print(f'There are {count_digit} numeric strings.')

        # sum of digits
        total = []

        for d in text[text_number].split():
            if d.isdigit():
        
                total.append(int(d))
        
        print(f'The sum of all the numbers {sum(total)}')

    elif text_number == 2:
        # number of words
        print(f'There are {len(text[text_number].split())} words in the selected text.')

        # number of words starting with titlecase
        count_title = 0 
        for i in text[text_number].split():
            if i.istitle():
                count_title += 1
        
        print(f'There are {count_title} titlecase words.')

        # number of words starting with uppercase
        count_upper = 0 
        for i in text[text_number].split():
            if i.isupper() and not i.istitle():
                count_upper += 1        
        
        print(f'There are {count_upper} uppercase words.')

        # number of words starting with lowercase
        count_lower = 0 
        for i in text[text_number].split():
            if i.islower():
                count_lower += 1

        print(f'There are {count_lower} lowercase words.')

        # number of numbers 
        count_digit = 0 
        for i in text[text_number].split():
            if i.isdigit():
                count_digit += 1

        print(f'There are {count_digit} numeric strings.')

        # sum of digits
        total = []

        for d in text[text_number].split():
            if d.isdigit():
        
                total.append(int(d))
        
        print(f'The sum of all the numbers {sum(total)}')

    else: 
        print('Wrong number!')
       

else: 
    print('Wrong user name or password. The program has been terminated')