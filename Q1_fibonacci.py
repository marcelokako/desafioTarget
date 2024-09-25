# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def procura_num_fibonacci(num):
    fibonacci = [0,1]
    for n in fibonacci:
        if n == num:
            return True
        
    while True:
        novo_termo = fibonacci[-1] + fibonacci[-2]
        if novo_termo == num:
            return True # Numero encontrado
        elif novo_termo > num:
            return False # Numero procurado que novo termo, nunca será encontrado
        
        fibonacci.append(novo_termo)

def main():
    num_entrada = 20
    
    mensagem_retorno = "Número encontrado" if procura_num_fibonacci(num_entrada) else "Número não encontrado"
    print(mensagem_retorno)

main()