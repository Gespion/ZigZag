from time import sleep
from sys import exit

def zigzag(char_to_print):

    print("Welcome.\nWe'll undefinitely print a nice ZigZag until you stop the program by pressing: Ctrl+C or Cmd+C :) ")
    for countdown in range(5,-1,-1):
        print(countdown, " ...")
        sleep(1)

    while True:
        for i in range(5):
            for j in range(4-i):
                print(" ",end='')
            for k in range(4-i,12-i):
                print(char_to_print,end='')
                sleep(0.2)
            print(end='\n')
        for l in range(4):
            for m in range(-1,l+1-1):
                print(" ",end='')
            for n in range(4+l,12+l):
                print(char_to_print,end='')
                sleep(0.2)
            print(end='\n')
try:
    zigzag('<')
except KeyboardInterrupt:
    exit()
