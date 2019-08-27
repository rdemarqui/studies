"Exercício da paágina 141"
"Grade para imagem composta de caracteres"

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for coluna in range(len(grid[0])):
    print(end='\n')
    for linha in range(len(grid)):
        variavelLinha = grid[linha]
        print(variavelLinha[coluna], end='')
        