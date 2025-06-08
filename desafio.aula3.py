import math

A = 2
B = 7
C = 3.5
L = False
V = True

conta1 = (B == A * C) and (L or V)
print("cálculo 1:",conta1)

conta2 = (B > A) or (B == pow(A, A))
print("cálculo 2:",conta2)

conta3 = (L and (B // A >= C)) or (not (A <= C))
print("cálculo 3:",conta3)

conta4 = (not L) or (V and math.sqrt(A + B) >= C)
print("cálculo 4:",conta4)

conta5 = (B / A == C) or (B / A != C)
print("cálculo 5:",conta5)

conta6 = L or (pow(B, A) <= (C * 10 + A * B))
print("cálculo 6:",conta6)