'''Faça uma sub-rotina que receba um valor inteiro e verifique se ele é positivo ou negativo.'''


#minha assinatura 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def sub_rotina(n):
    if n > 0:
        print("Esse número é positivo")
    elif n == 0:
        print("Esse número é neutro")
    else:
        print("Esse número é negativo")

n = int(input("Insira um número: "))
sub_rotina(n)