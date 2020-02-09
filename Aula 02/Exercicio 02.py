#Recebe uma string e devolve invertida

print('Digite sua String:')
n = input()

def string(n):
    if n == '':
        return n 
    return n[-1] + string(n[:-1]) 

print(string(n)) 