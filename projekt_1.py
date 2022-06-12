"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""
from typing import Text
import task_template as texts 
import collections

lines = 30 * '-'
user = ['bob', 'mike', 'ann', 'liz']
password = ['123', 'pass123', 'password123', 'pass123']
# text has 3 indices
text = texts.TEXTS
text_dic = {}

# creates dictionary out of text list
for items in range(len(text)):
    text_dic[items] = text[items]

print(lines)

user_name = input(str('Hello, insert your username: '))
user_pass = input(str('Now please insert your password: '))

print(lines)

if user_name in user and user_pass in password:
    print(f'Hello {user_name.capitalize()}')
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

        len_list = []

        for i in text[text_number].split():
            len_list.append(len(i))

        len_list_sort = sorted(set(len_list)) # len in the graph

        occurences = collections.Counter(len_list)
        occurences_sorted = sorted(occurences.items())

        for k, v in occurences_sorted:
            pass

        lines = 35 * '-'
        space = (6 * v) * ' '

        print(lines)
        print(f'LEN|{space}Occurences{space}|NR.' )
        print(lines)

        for k, v in occurences_sorted:

            stars = v * '*'

            if k <= 9:
                print((f'  {k:<0}|{stars:<16}{space}|{v}'))

            else:
                print((f' {k:<0}|{stars:<16}{space}|{v}'))


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

        len_list = []

        for i in text[text_number].split():
            len_list.append(len(i))

        len_list_sort = sorted(set(len_list)) # len in the graph

        occurences = collections.Counter(len_list)
        occurences_sorted = sorted(occurences.items())

        for k, v in occurences_sorted:
            pass

        lines = 35 * '-'
        space = (6 * v) * ' '

        print(lines)
        print(f'LEN|{space}Occurences{space}|NR.' )
        print(lines)

        for k, v in occurences_sorted:

            stars = v * '*'

            if k <= 9:
                print((f'  {k:<0}|{stars:<16}{space}|{v}'))

            else:
                print((f' {k:<0}|{stars:<16}{space}|{v}'))

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

        len_list = []

        for i in text[text_number].split():
            len_list.append(len(i))

        len_list_sort = sorted(set(len_list)) # len in the graph

        occurences = collections.Counter(len_list)
        occurences_sorted = sorted(occurences.items())

        for k, v in occurences_sorted:
            pass

        lines = 35 * '-'
        space = (6 * v) * ' '

        print(lines)
        print(f'LEN|{space}Occurences{space}|NR.' )
        print(lines)

        for k, v in occurences_sorted:

            stars = v * '*'

            if k <= 9:
                print((f'  {k:<0}|{stars:<16}{space}|{v}'))

            else:
                print((f' {k:<0}|{stars:<16}{space}|{v}'))

    else: 
        print('Wrong number! You have inserted wrong number or a letter')
       

else: 
    print('Wrong user name or password. The program has been terminated')