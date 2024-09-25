# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

def contador_char(char, string):
    contador = 0
    for c in string:
        if char.upper() == c.upper():
            contador += 1
    return contador

def main():
    string_entrada = "FRase ALEaToriA"
    qtd_char = contador_char('a', string_entrada)
    
    if qtd_char > 0:
        print(f"Foram encontrados {qtd_char} vezes na string {string_entrada}")
    else:
        print(f"O char dado não foi encontrado na string {string_entrada}")


main()