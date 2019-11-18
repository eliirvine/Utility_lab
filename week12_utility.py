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
