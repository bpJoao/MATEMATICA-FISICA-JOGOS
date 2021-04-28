'''
QUESTÃO 5 – Escreva um programa que converta um número decimal d para uma base
numérica b>0.
'''

def reverse_string(x):
  return x[::-1]

print('Numeric Conversion.')
print('')

b = int ( input('Type numeric base.') )
i = int ( input('Type an non negative number on decimal base .') )

m = i % b
q = int ( i / b ) 
result = ''

while (q > b):

  q = int (i / b) 
  m = i % b
  result += str(m)
  i = q

result += str(q)

result = reverse_string(result)

print('The typed number in numeric base' + str(b) + 'is equals to:' + result  )

