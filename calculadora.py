n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
operacao = input('Digite a operação: ')

match operacao:
    case '+':
        res = n1 + n2
    case '-':
        res = n1 - n2
    case '*':
        res = n1 * n2
    case '/':
        res = n1 / n2

print(f'Resultado é igual a {res}')