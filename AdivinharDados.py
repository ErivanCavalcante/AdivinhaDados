import random

#valores dos dados
dado1 = 0
dado2 = 0

#soma da aposta
somaAposta = 0

#resposta do player
resposta = 0

def rolarDados():
    valor1 = random.randint(1, 6)
    valor2 = random.randint(1, 6)
    return valor1, valor2

while True:
    print("Vamos Jogar?")
    print("1)Sim \n0)Nao ")
    
    resposta = int(input())
    
    if resposta == 0:
        break
   
    #comeca o jogo
    print("Digite a soma da sua aposta")
   
    somaAposta = int(input())
   
    print("Rolando os dados...")
    
    dado1, dado2 = rolarDados()
    
    print("Dado 1 = ", dado1, "Dado 2 = ", dado2)
    
    print("Soma dos dados = ", str(dado1 + dado2))
    
    if somaAposta != dado1 + dado2:
        print("Voce perdeu!")
    else:
        print("Parabens! Voce ganhou")

