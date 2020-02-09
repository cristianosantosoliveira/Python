kind = "blank"
 
def test_kind():
    print("Test Kind:", kind)
 
class Dog:
    kind = 'canine'
 
    def __init__(self, name):
        self.name = name
 
    def what_kind(self):
        print("Name:", self.name)
        print("Geral:", kind)
        print("Self:", self.kind)
 
# Testes...
d = Dog('Fido')
e = Dog('Buddy')
 
test_kind()
print('-' * 40)

d.kind = 'Teste Ok'
d.what_kind()
print('-' * 40)
e.what_kind()
print('-' * 40)
 
print(Dog)
print(Dog.what_kind)
print(e)
print(e.what_kind)