spam = ['apples', 'bananas', 'tofu', 'cats']

string = ''
tamanhoLista = len(spam) - 1
n = 0

while n <= tamanhoLista:
    if n == 0:
        string = spam[n]
    elif n == tamanhoLista:
        string = string + " and " + spam[n]
    else:
        string = string + ", " + spam[n]
    n = n + 1

print(string)