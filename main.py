
def print_hi(name):

    print(f'Oi, {name}')
    print('Oi, ' + name)

def calcular_area_retangulo(largura,comprimento):
    return largura * comprimento

def calcular_area_quadrado(lado):
    return lado * lado

def calcular_area_triangulo(base,altura):
    return (base * altura) / 2

def contagem_progressiva(fim):
    for numero in range(fim): #repetir o bloco de zero até o fim
        print(numero)

def apoiar_candidato(nome,vezes):
    for numero in range(vezes):
        #contador = numero + 1
        #print(f'{contador} - {nome}')
        if numero <= 8:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
                print(numero + 1, '-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0 or numero == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))


if __name__ == '__main__':
    print_hi('Lucas')

    #chamar a função de cálculo de retângulo
    resultado = calcular_area_retangulo(3,4)
    print(f'A área do retângulo é de {resultado} m²')

    # chamar a função de cálculo de quadrado
    resultado2 = calcular_area_quadrado(6)
    print(f'A área do quadrado é de {resultado2} m²')

    # chamar a função de cálculo de triangulo
    resultado3 = calcular_area_triangulo(3,7)
    print(f'A área do triangulo é de {resultado3} m²')

    #executar uma contagem progressiva
    contagem_progressiva(10)

    #exibir o nome do candidato
    apoiar_candidato('Indefinido',3)

    #brincar de pin
    brincar_de_plim(100)