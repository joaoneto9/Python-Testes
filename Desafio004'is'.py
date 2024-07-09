n = input('Digite  algo:')

print(type(n)) #string, certeza

print('Essa string eh alfabetico?', n.isalpha())
print('Essa string eh numerico?', n.isnumeric())
print('Essa string eh alfanumerico?', n.isalnum())
print('Essa string eh decimal?', n.isdecimal())
print('Essa string eh um digito?', n.isdigit())
print('Essa string eh', n.isidentifier())
print('Essa string esta em minuscula', n.islower())
print('Essa string esta em maiuscula?', n.isupper())
print('Essa string ', n.isprintable())
print('Essa string tem espaco?', n.isspace())
print('Essa string eh capitalizada?', n.istitle()) #maiusculas e minusculas




