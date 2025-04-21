print("Digite as notas do aluno. Quando quiser parar, digite 24.")

notas = []
while True:
    try:
        nota = float(input("Digite uma nota: "))
        if nota == 24:
            break
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Inválido. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Inválido. Por favor, digite um número.")

if notas:
    media = sum(notas) / len(notas)
    print(f"A média do aluno é: {media:.2f}")
else:
    print("nada foi inserido.")


