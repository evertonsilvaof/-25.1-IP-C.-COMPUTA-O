conta = int(input("Digite o número da sua conta: "))
saldo = float(input("Digite o Saldo:"))
debito = float(input("Digite o Débito:"))
credito = float(input("Digite o Crédito:"))

s_atual = (saldo - debito) + credito
if s_atual >= 0:
 print("Saldo Positivo")

elif s_atual < 0:
 print("Saldo Negativo")

