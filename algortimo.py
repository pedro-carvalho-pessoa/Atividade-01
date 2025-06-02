def primoo(n):

    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True

def entrada_valida():
    while True:
        try:
            numero = int(input("Me informe um valor maior que 01: "))
            if numero > 1:
                return numero
            else:
                print("Número errado, deve ser maior que 01!")
        except ValueError:
            print("Erro: entrada inválida. Tente outro número.")

def primoss(n):
 
    print(f"Números primos menores que {n}: ")
    for i in range(2, n):
        if primoo(i):
            print(i, end=' ')
    print()

def main():
    numero = entrada_valida() 
    primoss(numero)

if _name_ == "_main_":
    main()
