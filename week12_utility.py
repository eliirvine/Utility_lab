#Eli Irvine
#CSCI 102 - Section A
#Week 12 - Part A

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(file_name):
    with open(file_name, 'r') as f:
        content = f.read().splitlines()
        return content
