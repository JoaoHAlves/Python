
#1
#idade = 0
#altura = 0
#peso = 0
#nome = str(input('Digite o nome: '))
#idade = int(input('Digite a idade: '))
#altura = float(input('Digite a altura: '))
#peso = float(input('Digite o peso: '))
#if(idade >= 18) and (altura >= 1.70) and (peso >= 70):
#    print('Você está apto para o exercito')
#else:
#    print('Você não está apto')

#########################################################
#########################################################
#2
#frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
#print('O inverso da frase é {}'.format(inverso))
#if inverso == junto:
#    print('Temos um palíndromo')
#else:
#    print('Esta frase não é um palíndromo')
#########################################################
#########################################################
#3
#dias = int(input("Dias: "))
#horas = int(input("Horas: "))
#minutos = int(input("Minutos: "))

#segdias = ((24 * dias) * 3600)
#seghoras = ((horas * 60) * 60)
#segminutos = (minutos * 60)
#total_segundos = (segdias + segminutos + seghoras)

#print('A quantidade de segundos em {} dia é: {} segundos '.format(dias, segdias))
#print('A quantidade de segundos em {} horas é: {} segundos '.format(horas, seghoras))
#print('A quantidade de segundos em {} minutos é: {} segundos '.format(minutos, segminutos))
#print('A quantidade total de segundos é de {} segundos'.format(total_segundos))
#########################################################
#########################################################
#4
#distancia = int(input('Digite a distancia em km: '))
#velocidademedia = int(input('Digite a velocidade media em km/h: '))

#tempo = distancia // velocidademedia
#x = (distancia // velocidademedia)
#tempo_m = int(((distancia / velocidademedia) - x) * 60)
#print('O tempo dessa viagem é de {} horas e {} minutos'.format(tempo, tempo_m))
#########################################################
#########################################################
#5
#velocidade_c = int(input('Digite a velocidade do veículo: '))

#if(velocidade_c > 80):
#    multa = (5 * velocidade_c)
#    print('Você foi multado, valor da multa {}'.format(multa))

#########################################################
#########################################################
#6
#valor_c = float(input('Digite o valor do imóvel: '))
#salario = float(input('Digite o valor do salario: '))
#anos_p = int(input('Digite a quantidade de anos a pagar: '))
#numero_m = (anos_p * 12)
#prestacao_m = (valor_c / numero_m)

#if(prestacao_m >= (salario * 0.30)):
#    print('O emprestimo foi negado, valor das parcelas superior a 30%')
#else:
#    print('Emprestimo aprovado!')
#########################################################
#########################################################
#7

#while True:
#    tabuada = int(input('Digite o valor para gerar a tabuada: '))
#    for c in range(0,10):
#        print(f'{tabuada} * {c} = {tabuada*c}')
#########################################################
#########################################################
#8
#dividendo = int(input("Dividendo: "))
#divisor = int(input("Divisor: "))
#quociente = 0
#x = dividendo
#while x >= divisor:
#    x = x - divisor
#    quociente = quociente + 1
#resto = x
#print(f"O resto de {dividendo} / {divisor} é {resto}")

#########################################################
#########################################################
#9
#lado_a = int(input('Insira o primeiro lado: '))
#lado_b = int(input('Insira o segundo lado: '))
#lado_c = int(input('Insira o terceiro lado: '))

#if(lado_a == lado_b) and (lado_b == lado_c) and (lado_a == lado_c):
#    print('O triangulo é equilátero!')
#if(lado_a == lado_b) or (lado_b == lado_c) or (lado_a == lado_c):
#    print('O triangulo é isóceles!')
#if(lado_a != lado_b) and (lado_b != lado_c) and (lado_a != lado_c):
#    print('O triangulo é escaleno!')
#########################################################
#10
#numero = int(input('Digite o numero: '))
#numero = str(numero)

#print(numero[::-1])
#########################################################
#########################################################
#11
#vogais = str(input('Digite uma palavra ou frase: '))
#vogal = 0
#for i in vogais:
#      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#            vogal = vogal+1
#print("O numero de vogais é: {}".format(vogal))
#########################################################
#########################################################
#12

# Não consegui fazer


#print('O caractere mais frequente é {}, aparecendo {} vezes')

#########################################################
#########################################################
#13
#frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
#if inverso == junto:
#    print('{} é um palíndromo')
#else:
#    print('Esta palavra não é um palíndromo')




