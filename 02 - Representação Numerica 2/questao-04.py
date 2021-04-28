'''
QUESTÃO 4 – Crie um programa que receba (1) uma base numérica b>1 e um inteiro não- negativo ib na base b e imprima o valor de i na base decimal.
'''

def reverse_string(x):
  return x[::-1]

print('Numeric Conversion [Generic Base -> Decimal]')
print('')

i = int ( input('Type an non negative number on a non decimal base.') )
b = int ( input('Type the numeric base of typed number.') )

