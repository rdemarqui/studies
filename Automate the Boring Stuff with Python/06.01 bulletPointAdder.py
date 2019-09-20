#! python 3
# Script para adicionar bullet points

import pyperclip

# Copiando o conteúdo o do Clpboard
text = pyperclip.paste()
line = text.split('\n')

# Modificando a lista
for n in range(len(line)):
    line[n] = '* ' + line[n]

text = '\n'.join(line)

# Colando a lista modificada para o clipboard
pyperclip.copy(text)
    
    



