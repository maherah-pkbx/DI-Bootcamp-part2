"""
Instructions
Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message.
"""

input_lengths = []
condition = True

while condition:
    sentence = input('Provide a sentence without the letter A: ').lower()
    if 'a' not in sentence and len(sentence) not in input_lengths:
        input_lengths.append(len(sentence))
        print('Congratulations!')
    elif 'a' not in sentence and len(sentence) in input_lengths:
        print('Try to provide a longer sentence without the letter A.')
    else:
        condition = False


        """"
        Output:
        Provide a sentence without the letter A: i no longer sleep
Congratulations!
Provide a sentence without the letter A: i no longer snore
Try to provide a longer sentence without the letter A.
Provide a sentence without the letter A: i no longer drink fizzy drinks just like my mother 
Congratulations!
Provide a sentence without the letter A: and eat and dance"""
