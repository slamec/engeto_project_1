from collections import Counter
import collections

text = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# number of words
print(f'There are {len(text[0].split())} words in the selected text.')

# number of words starting with titlecase
count_title = 0 
for i in text[0].split():
    if i.istitle():
        count_title += 1
        
print(f'There are {count_title} titlecase words.')

        # number of words starting with uppercase
count_upper = 0 
for i in text[0].split():
    if i.isupper() and not i.istitle():
        count_upper += 1        
        
print(f'There are {count_upper} uppercase words.')

        # number of words starting with lowercase
count_lower = 0 
for i in text[0].split():
    if i.islower():
        count_lower += 1

print(f'There are {count_lower} lowercase words.')

        # number of numbers 
count_digit = 0 
for i in text[0].split():
    if i.isdigit():
        count_digit += 1

print(f'There are {count_digit} numeric strings.')

        # sum of digits
total = []

for d in text[0].split():
    if d.isdigit():
        
        total.append(int(d))
        
print(f'The sum of all the numbers {sum(total)}')

len_list = []

for i in text[0].split():
    len_list.append(len(i))

len_list_sort = sorted(set(len_list)) # len in the graph

# for i in len_list_sort:
#         print(str(i), end='')
#         print(' ', end='')
#         print(i * '*') # len of word


occurences = collections.Counter(len_list)

occurences_sorted = sorted(occurences.items())

print('LEN', 'Occurences'.capitalize(), 'NR.')

for k, v in occurences_sorted:
        
        print(k, '|', v * '*', '',v)
