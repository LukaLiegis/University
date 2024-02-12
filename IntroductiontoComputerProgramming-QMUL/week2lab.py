'''Very nice!  Although you could also have just cheated by simply opening the week2lab.py file in your web browser and reading this message there!  The bottom of that file contains a hidden comment, copy and paste it into this Jupyter Notebook and use the caesar function to decode it.'''

print('This module contains a function that encrypts/decrypts text strings using a famous cipher.\nUse the dir() function to list all functions defined in the week2lab module, and determine the name of this cipher function.\nOnce you have found the function, run it on the following encrypted message:\n\nTnq tamjb-mh nqjf() pahsbmgh suh tq acqr bg dqbdmqzq acqpaj mhpgdiubmgh utgab u igrajq.  Rah mb gh bnq yqqk2jut igrajq.')

def caesar(txt):
    out=''
    for i in txt:
        if 97<=ord(i)<=122:
            out+=chr((13-ord(i))%26+97)
        else:
            out+=i
    return out

# Exsqjjqhb ygdk!  Yga udq hgy dqurw bg igzq gh bg Exqdsmcq 2, mh ynmsn wga ymjj sghcbdasb wgad gyh igrajq.\n\n(Bw bnq yuw, bnq rmd() uhr nqjf() pahsbmghc suh ujcg tq acqr gh pahsbmghc uhr rubu bwfqc, uc yqjj uc igrajqc.)