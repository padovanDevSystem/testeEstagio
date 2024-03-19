#Vamos criar uma função para inverter esse valor
def inverter_string(valor):
    valor_invertida = ''

    for i in range(len(valor) -1, -1, -1):
        valor_invertida += valor[i]
    return valor_invertida

valor_normal = input('Digite um valor para inverter: ')
string_invertida = inverter_string(valor_normal)
print(f'VALOR ORIGINAL: {valor_normal} \n VALOR INVERTIDO: {string_invertida}')

#\______________/
#__/__|______|__\__
#/⭕⭕_______⭕⭕\
#|__/__PadovaN__\__|
#\©©__|_|_|_|_|__©©/