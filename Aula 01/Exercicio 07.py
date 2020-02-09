pow2 = [2 ** x for x in range(10)]

pow2 = []

for x in range(10):
    pow2.append(2 ** x)

pow2 = [2 ** x for x in range(10) if x > 5]
odd = [x for x in range(20) if x % 2 == 1]
conc = [x+y for x in ['Python ', 'C '] for y in 
['Language', 'Programing']]

print(pow2)
print(odd)
print(conc)


