import os
from time import sleep

#os.system("clear") # linux

worddata = [
'#     # ####### #       #       #######  #  #  # ####### ####### #       ###### ',
'#     # #       #       #       #     #  #  #  # #     # #     # #       #     #',
'#     # #       #       #       #     #  #  #  # #     # ####### #       #     #',
'####### ####### #       #       #     #  #  #  # #     # # #     #       #     #',
'#     # #       #       #       #     #  #  #  # #     # #  #    #       #     #',
'#     # #       #       #       #     #  #  #  # #     # #   #   #       #     #',
'#     # ####### ####### ####### #######  ####### ####### #    ## ####### ###### ']
worddata_h = len(worddata)
worddata_w = len(worddata[0])
add = ''
num = 10
worddata_new =  ['' for i in xrange(worddata_h * num)]
for i in xrange(num):
    add += ' '
    for y in xrange(worddata_h):
        worddata_new[i * worddata_h + y] = add + worddata[y]
        
while(1):
    string = 'HELLO WORLD'
    tap = '|'
    os.system("clear") 
    sleep(0.2)
    string_new = ''
    for i in xrange(len(string)):
        string_new += string[i]
        print string_new
        sleep(0.1)
        os.system("clear") 
        print string_new + tap
        sleep(0.1)
        os.system("clear") 
        print string_new
        sleep(0.1)
        os.system("clear") 
        
    for i in xrange(num):
        for y in xrange(worddata_h):
            y_out = worddata_new[i * worddata_h + y]
            print y_out
        sleep(0.1)
        os.system("clear")
        
    for i in xrange(num):
        for y in xrange(worddata_h):
            y_out = worddata_new[(num - i - 1) * worddata_h + y]
            print y_out
        sleep(0.1)
        os.system("clear")
