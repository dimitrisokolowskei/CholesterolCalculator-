print('Lipidograma: ')

jejum = str(input('Encontra-se em jejum?'))

triglicerideos = float(input('Qual o valor de triglicerideos?'))

def my_function(triglicerideos):
    return triglicerideos / 5

if jejum == 'sim' and triglicerideos <150:
    print('O valor de VLDL é: ' + str(my_function(triglicerideos)) + ' mg/dL')

elif jejum == 'sim' and triglicerideos > 150:
    print('O valor de VLDL é: ' + str(my_function(triglicerideos)) + ' mg/dL')
    print('Valor de triglicerideos acima do desejável')

elif jejum == 'não' and triglicerideos <175:
    print('O valor de VLDL é: ' + str(my_function(triglicerideos)) + ' mg/dL')

elif jejum == 'não' and triglicerideos > 175:
    print('O valor de VLDL é: ' + str(my_function(triglicerideos)) + ' mg/dL')
    print('Valor de triglicerideos acima do desejável')


HDL = float(input('Qual o valor de HDL?'))
if HDL < 40:
    print('Valor de HDL abaixo do desejado')

CT = float(input('Qual o valor de Colesterol total?'))
if CT > 190:
    print('Valor de Colesterol total acima do desejado')


VLDL = my_function(triglicerideos)

def my_function(CT, HDL, VLDL):
    return CT -(HDL + VLDL)

print('O valor de LDL é: ' + str(my_function(CT, HDL, VLDL)) + ' mg/dL')

nHDL = CT - my_function(CT, HDL, VLDL)

print('O valor de Colesterol não HDL é: ' + str(nHDL) + ' mg/dL')
