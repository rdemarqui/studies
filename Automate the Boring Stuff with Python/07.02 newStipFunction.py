#! python3
# New strip function

import re

def RegexStrip(mainString, charsToBeRemoved=None):
    if(charsToBeRemoved!=None):
        regex=re.compile(r'[%s]'%charsToBeRemoved)
        print(regex.sub('',mainString))
    else:
        regex=re.compile(r'^\s+')
        regex1=re.compile(r'$\s+')
        newString=regex1.sub('',mainString)
        newString=regex.sub('',newString)
        print(newString)
    