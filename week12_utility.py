#Eli Irvine
#CSCI 102 - Section A
#Week 12 - Part A

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(file_name):
    with open(file_name, 'r') as f:
        content = f.read().splitlines()
        return content

def UpdateString(str_1, str_2, index):
    first_half = str_1[0:index]
    second_half = str_1[index+1:]
    updated_str = first_half + str_2 + second_half
    PrintOutput(updated_str)

def FindWordCount(my_list, my_str):
    content_str = ''.join(my_list)
    PrintOutput(str(content_str.count(my_str)))

def ScoreFinder(list_1, list_2, a_string):
    word = a_string.capitalize()
    for index, name in enumerate(list_1):
        if name == word:
            print('OUTPUT %s got a score of %d' % (name, list_2[index]))
        if word not in list_1:
            print('OUTPUT player not found')
            break
    
    
