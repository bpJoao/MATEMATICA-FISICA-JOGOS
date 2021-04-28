'''
QUESTÃO 6 – Com base nos programas anteriores, escreva um programa de que converta
números entre duas bases numéricas.
'''

def reverse_string(x):
  return x[::-1]

print('Numeric Conversion [Generic Base -> Decimal]')
print('')

i = int ( input('Type an non negative number on a non decimal base.') )
b = int ( input('Type the numeric base of typed number.') )
ob = int( input('Type a base to convert the typed number.'))

