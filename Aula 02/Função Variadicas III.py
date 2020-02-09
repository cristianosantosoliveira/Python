list(range(3,6))

args= [3,6]

lista = list(range(*args))

print(args)
print(lista)

#######################################
def soma(x,y,z):
    x= [1,2]
    y= [3,4]
    z= [5,6]

    resultado = (x+y+z)

    print("A lista concatenada é: ", resultado)

