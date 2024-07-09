a = input('insira o valor de a:')
b = input('insira o valor de b:')
c = input('insira o valor de c:')

a = int(a)
b = int(b)
c = int(c)

delta = b**2 - 4*a*c

x1 = (-b + delta ** 0.5)/2*a
x2 = (-b - delta ** 0.5)/2*a

print(x1, x2)