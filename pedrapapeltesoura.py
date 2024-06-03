from random import randint 

esc=['tesoura','papel','pedra']
cont=0
jogo=0
computador= 0

for c in range(0,3):
  
  computador=randint(0,2)
  com=esc[computador]
  
  jogador=str(input('Pedra,Papel ou Tesoura: ')).lower()
  if jogador == 'tesoura' and com == 'papel':
    jogo+=1
    print('Escolha da maquina: {}'.format(com))
    
  elif jogador == 'tesoura' and com == 'pedra':
    computador+=1
    print('Escolha da maquina: {}'.format(com))    
  elif jogador == 'tesoura' and com == 'tesoura':
    jogo+=1
    computador+=1
    print('Escolha da maquina: {}'.format(com))
    
  elif jogador == 'pedra' and com == 'tesoura':
    jogo+=1
    print('Escolha da maquina: {}'.format(com))
    
  elif jogador == 'pedra' and com == 'papel':
    computador+=1
    print('Escolha da maquina: {}'.format(com))
    
  elif jogador == 'pedra' and com == 'pedra':
    computador+=1
    jogo+=1
    print('Escolha da maquina: {}'.format(com))
    
  elif jogador == 'papel' and com == 'pedra':
    jogo+=1
    print('Escolha da maquina: {}'.format(com))
    
  elif jogador == 'papel' and com == 'tesoura':
    computador+=1
    print('Escolha da maquina: {}'.format(com))
    
  elif jogador == 'papel' and com == 'papel':
    computador+=1
    jogo+=1
    print('Escolha da maquina: {}'.format(com))
    
print('Jogador: {}'.format(jogo))
print('Computador: {}'.format(computador))
