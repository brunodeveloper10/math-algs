
'''num = input("Digite um numero para verificar se e primo: ")

if not isinstance(num, int):
    print('O número precisa ser um inteiro')
    exit(1)

print(f"o numero é {num}")
'''

#para descobrir se é primo podemos utilizar o criterio de divisibilidade
#eliminando a possibilidade de todos os seus multiplos
def verifica_primo(num) -> bool:
    
    for x in [2,3,4,5,6,7,num]:
        print(x)


def verify_primer_with_attempts(num) -> tuple:
    primer = True
    result = 1

    if num <= 1:
        return False, result
    
    
    for x in range(2, num):
        result = num % x
        if result == 0:
            primer = False
            result = x
            break
    
    return primer, result