import time

bd_filmes = []

def cadastra_filmes(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd

def lista_filmes(bd):
    for i in range(len(bd)):
       print(f"{i+1} | {bd[i][1]} | {bd[i][0]}")

def altera_filmes(bd, indice, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano
    return bd





while True:
     print("1 - cadastrar filme")
     print("2 - Listar filmes")
     print("3 - Alterar Filme")

     op = int(input("Digite a opção:"))

     if op == 1:
         titulo = input("digite o nome do filme:")
         ano = int(input("digite o ano do filme:"))
         bd_filmes = cadastra_filmes(bd=bd_filmes, titulo=titulo, ano=ano)
         print("Filme Cadastrado!")
     elif op == 2:
         lista_filmes(bd_filmes)
         print("filmes Listados!")
     elif op == 3:
         lista_filmes(bd_filmes)
         i = int(input("qual filme deseja alterar?"))
         titulo = input("digite o novo titulo:")
         ano = int(input("digite o novo ano:"))
         bd_filmes = altera_filmes(
             bd=bd_filmes,
             indice = (i-1),
             titulo = titulo,
             ano = ano
         )
         print("Filme ALterado!")
     else:
         print(f'opção {op} opção inválida!')

     time.sleep(3)