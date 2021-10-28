
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

def exibir_dia_da_semana_if(numero):
    print('Execuçaõ com if')
    if numero == 2:
        print('o dia é segunda')
    elif numero == 3:
        print('O dia é terça')
    elif numero == 4:
        print('O dia é quarta')
    elif numero == 5:
        print('O dia é quinta')
    elif numero == 6:
        print('O dia é sexta')
    elif numero == 7:
        print('O dia é sábado')
    elif numero == 1:
        print('O dia é domingo')
    else:
        print('O dia não existe. Digite um número de 1 a 7')

'''

def exibir_dia_da_semana_match(numero):
    print('Execução com match')
    escolha = 1
    match escolha:
        case 1:
            print('o dia é Domingo')
            exit()
        case 2:
            print('o dia é Segunda')
            exit()
        case 3:
            print('o dia é Terça')
            exit()
        case 4:
            print('o dia é Quarta')
        case 5:
            print('o dia é Quinta')
            exit()
        case 6:
            print('o dia é Sexta')
            exit()
        case 7:
            print('o dia é Sábado')
            exit()
        case_:
            print('O dia não existe. Digite um número de 1 a 7')

'''
def brincar_de_para_ou_continua():
    resposta = 'C' #S aqui significa que continua

    #while resposta == 'C' or 'c':
    while resposta.upper() == 'C':
        resposta = input("Digite C para continuar ou qualquer outro caracter para parar")

    print('Você decidiu parar com a brincadeira')



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

    #exemplo de dia da semana com if - elif - else
    exibir_dia_da_semana_if(' ')

    #exemplo de dia da semana com match - case
    #exibir_dia_da_semana_match(1)

    #exemplo com While - para ou continua
    brincar_de_para_ou_continua()