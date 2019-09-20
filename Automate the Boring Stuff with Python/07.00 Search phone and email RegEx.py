#! python3
#Project to extract phone number and e-mail from clipboard

import pyperclip, re

#Creating Regex patterns
phone = re.compile(r'''(
                   (\d{3}|\(\d{3}\))?    # area code (optional)
                   (\s|-|\.)?            # separator
                   (\d{3})               # first tree digits
                   (\s|-|\.)?            # separator
                   (\d{4})               # last four digits
                   )''', re.VERBOSE)

email = re.compile(r'''(
                   [a-zA-Z0-9._%+-]+     # user name
                   @                     # @ simbol
                   [a-zA-Z0-9.-]+        # domain name
                   (\.[a-zA-Z]{2,4})     # point followed by another chars
                   )''', re.VERBOSE)

# Obtaining text form clipboard
text = str(pyperclip.paste())

# Finding all phone numbers and e-mails

matches=[]

for groups in phone.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)

for groups in email.findall(text):
    matches.append(groups[0])

# Pasting all results to clipboard
if matches == []:
    print('There is no e-mail or phone number')
else:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))