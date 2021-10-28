
def print_hi(name):

    print(f'Oi, {name}')
    #print('Oi, ' + name)

def calcular_area_retangulo(largura,comprimento):
    #return largura * comprimento
    resultado = largura * comprimento
    print(f'A área do retângulo é de {resultado} m²')

def calcular_area_quadrado(lado):
    #return lado * lado
    resultado2 = lado * lado
    print(f'A área do quadrado é de {resultado2} m²')

def calcular_area_triangulo(base,altura):
    #return (base * altura) / 2
    resultado3 = (base * altura) / 2
    print(f'A área do triangulo é de {resultado3} m²')

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

def sair():
    print('Obrigado e Volte Sempre')


if __name__ == '__main__':

    resposta = "C"

    while resposta.upper() != 'Z':

        print('#########################################')
        print('#                                       #')
        print('#       M E N U D E O P Ç Õ E S         #')
        print('#            1 - Olá Mundo              #')
        print('#            2 - Área do Retângulo      #')
        print('#            3 - Área do Quadrado       #')
        print('#            4 - Área do Triângulo      #')
        print('#            5 - Contagem Progressiva   #')
        print('#            6 - Apoiar Candidato       #')
        print('#            7 - Brincar de Plim        #')
        print('#                                       #')
        print('#            Z - Sair                   #')
        print('#                                       #')
        print('#########################################')

        resposta = input("Escolha sua opção: ")
        print(f'A sua escolha foi: {resposta}')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('José')
            elif resposta == '2':
                calcular_area_retangulo(8,7)
            elif resposta == '3':
                calcular_area_quadrado(4)
            elif resposta == '4':
                calcular_area_triangulo(4,5)
            elif resposta == '5':
                contagem_progressiva(6)
            elif resposta == '6':
                apoiar_candidato('Lula',4)
            elif resposta == '7':
                brincar_de_plim(4)
            else:
                print('Você digitou um número que não está entre 1 e 7')
        else:
            print("Você escolheu sair, volte sempre!")
