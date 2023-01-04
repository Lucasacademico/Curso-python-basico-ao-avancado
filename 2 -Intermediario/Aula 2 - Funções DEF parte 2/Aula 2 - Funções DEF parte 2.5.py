
def f(var):
    print(var)

def dumb():
    return f

var = dumb()('Colocar o valor aqui')
print(type(var))