try:
    valor = int(input('Digite um valor: '))
    print(valor / 0)
except ZeroDivisionError as log_error:
    print('Não é possível dividir por zero')
except ValueError as log_error:
    print('Apenas números')
finally:
    print('operação foi cancelada')