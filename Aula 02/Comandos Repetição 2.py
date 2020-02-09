for n in range(2,10):
    for x in range(2,n):
        if n % x ==0:
            print(n, 'igual a', x, '*', n // x)
            break  ##se nao dar Break no for ele entra no else

        else: 
            print(n, 'é número primo')


