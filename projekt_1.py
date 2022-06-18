"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""

from task_template import TEXTS as text 
import collections

lines = 35 * '-'

user_login = {'bob': '123', 'mike': 'pass123', 'ann': 'password123', 'liz': 'pass123'}

# appended list
text_list = []

# creates list from the texts
for items in text:
    text_list.append(items.replace('\n', ' '))

print(lines)

# ask user for username and password
user_name = input('Hello, insert your username: ')
user_pass = input('Now please insert your password: ')

print(lines)

# check if user in user and password list
if user_pass == user_login[user_name]:
    print(f'Hello {user_name.capitalize()},')
    print('')
    print('here are the texts to be analyzed: ')
    print(lines)
    print('')

    # show texts and numbers for user
    for (num,item) in enumerate(text_list):
        print(num + 1)
        print(item + '\n')


    print(lines)

    # -1 to match with list index
    text_number = int(input('Insert number of the text to analyze: ')) - 1 

    print(lines)

    def text_analyze():
        """Analyzes given text and returns statistics"""

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

        # lenght of the words
        len_list = []

        for i in text[text_number].split():
            len_list.append(len(i))

        # len_list set to avoid duplicies 
        len_list_sort = sorted(set(len_list)) # len in the graph

        # occurences of the len returns dictionary
        occurences = collections.Counter(len_list)
        occurences_sorted = sorted(occurences.items())

        space = 6 * ' '

        print(lines)
        print(f'LEN|{space}Occurences{space}|NR.' )
        print(lines)

        for k, v in occurences_sorted:

            stars = v * '*'

            # <16 to center string
            if k <= 9:
                print((f'  {k:<0}|{stars:<16}{space}|{v}'))

            else:
                print((f' {k:<0}|{stars:<16}{space}|{v}'))

    if text_number == text_number:
        text_analyze()

    else: 
        print('Wrong number! You have inserted wrong number or a letter.')
       

else: 
    print('Wrong user name or password. The program has been terminated.')