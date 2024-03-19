#Primeiro, vamos criar uma função onde terá um loop que reconhecerá o valor Fibonacci e executará a crescente

def sequencia_fibonacci(numero):
    #Aqui temos o valor da Fibonacci em lista, possibilitando realizar a crescente
    fibonacci = [0,1]
    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

#Nessa função, vamos verificar se a sequencia fibonacci está executando corretamente
def listar_sequencia_fibonacci(numero):
    fibonacci = sequencia_fibonacci(numero)

    if numero in fibonacci:
        return True
    else:
        return False
    
# Vamos fazer uma interação com o usuario para adquirirmos o valor que deseja
numero_usuario = int(input('Digite um numero: '))

if listar_sequencia_fibonacci(numero_usuario):
    print(f'Esse numero: {numero_usuario} está incluído na Sequencia Fibonacci')
else:
    print(f'Esse numero: {numero_usuario} NÃO está incluído na Sequencia Fibonacci')

#Explicando o código, criei uma Lista chamada FIBONACCI na primeira função, onde ela armazena uma lista com valores inteiros, após isso, criei um laço de loop onde adiciona uma soma no proprio numero, depois criei uma função que verifica se o numero realmente está na tabela. Após isso, criei uma interação com o usuário para obter o valor desejado, e uma condição para obter a resposta se o valor está ou não incluso na sequencia.
    
    
#\______________/
#__/__|______|__\__
#/⭕⭕_______⭕⭕\
#|__/__PadovaN__\__|
#\©©__|_|_|_|_|__©©/