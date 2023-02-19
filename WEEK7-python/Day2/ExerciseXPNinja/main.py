"""
Exercise 1 : Box Of Stars
Instructions
Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
"""

def box_printer(*strings):
    string_lengths = []

    for i in strings:
        string_lengths.append(len(i))

    box_width = max(string_lengths) + 4
    box_height = len(list(strings)) + 2

    print('*' * box_width)
    for string in strings:
        spaces_num = (box_width - 4) - len(string)
        print('* ' + string + ' ' * spaces_num + ' *')
    print('*' * box_width)


box_printer("Hello", "World", "in", "reallylongword", "a", "frame")





"""
Exercise2
Analyse this code before executing it. What is the purpose of this code?

ANSWER:
It's a sorting algorithm, it checks if the value from the preceeding index is larger than the value of index being
iterated over. If so, it swaps the values.
"""


def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)