#dados de entrada - lista de valores que serao analisados
valores = [8.5, 7.3, 9.0, 6.8, 7.5]

# ordena os valores em ordem crescente
valores_ordenados = sorted(valores)

#mostra os valores ordenados
print(valores_ordenados)

# calcula o total de valores na lista
n = len (valores_ordenados)

#print(n)

#  Operador para pegar somente a parte inteira da divisao
meio = n // 2

#print (meio)

# operador para pegar o resto da divisao %
# teste se o numero total de valores eh par ou impar
if n % 2 == 0:
  mediana = (valores_ordenados[meio-1]+valores_ordenados[meio])/2
else:
  mediana = valores_ordenados[meio]

print (mediana)
