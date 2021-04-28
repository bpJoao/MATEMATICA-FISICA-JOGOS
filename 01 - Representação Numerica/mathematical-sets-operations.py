'''
Forum Question: Implemente as operações entre conjuntos usando sua linguagem favorita (de preferência, hehehe).
'''

A = [2,4,6,8]
B = [3,6,9]

print("Union [AUB]:")
print(A + B)

print("")

print("Intersection [A∩B]:")
for i in A:
    for j in B:
        if(i==j):
            print(i)
            
print("")

print("Subtraction [A-B]:")
subtracionResult = A
for i in A:
    for j in B:
        if(i==j):
            subtracionResult.remove(i)
print(subtracionResult)

print("")

print("Cartesian Product [AXB]:")
cartesianProductResult = []
for i in A:
    for j in B:
        cartesianProductResult.append((i,j))
print(cartesianProductResult)

