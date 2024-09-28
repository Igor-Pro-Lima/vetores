""" Fazer um problema para ler um numero inteiro positivo N (maximo = 10),
depois ler N numeros quaisquer e armazena-los em um vetor. Em seguida, mostrar
na tela todos os elementos do vetor.
"""


N = int(input("Quantos numeros voce vai digitar? "))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um numero: "))

print() #para saltar uma linha vazia
print("NUMEROS DIGITADOS:")
for i in range(0, N):
    print(f"{vet[i]:.1f}") #formatado com uma casa decimal


