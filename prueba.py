from numeroscomplejos import *
import random
def main():
    casos=0
    while casos<10:
        numero1=(random.randrange(-10,-1),random.randrange(1,10))
        numero2=(random.randrange(1,10),random.randrange(-10,-1))
        print(suma(numero1,numero2))
        print(suma(numero1, numero2))
        print(producto(numero1, numero2))
        print(division(numero1, numero2))
        print(modulo(numero1, numero2))
        print(conjugado(numero1, numero2))
        print(polar(numero1,numero2))
        print(fase(numero1,numero2))
        casos+=1
                                            
main()
