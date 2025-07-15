print('hello')
a='hello'
b='class'
print(a+b)

x=10
y=x
y+=1
print (x)
#xnot change

a=[1,2,[3,4]]
import copy
b=a.copy()
b[0]=99
b[2][0]=42
print(a)
#change element in b, a also changes (hard copy)

#copy everything:
c=copy.deepcopy(a)
c[2][0]=100
print(a)

numbers = [1,2,3,4]
squares= [x**2 for x in numbers]
print(squares)

set_a={1,2,3}
set_b={3,4,5}
print(f"Union: {set_a| set_b}")

student = {"name": "Alice", "id": 12345, "major": "CS"}
student["major"] = "Computer Science" # Modify
student["year"] = 4 # Add
print(f"Student Name: {student['name']}")
print(f"Keys: {list(student.keys())}")

ids = {101, 102, 103, 101, 104} # {101, 102, 103, 104}
ids.add(105)
ids.remove(101)
print(f"Set: {ids}")
print(f"Is 102 in set? {102 in ids}")

x = 43
print(f"Value is {x}")
bdata = b"bytes"

A = [1, 2, 30, 4]
A.append(5)
A[2] = 3
A.sort()

point = (10.5, 20.3)
red_color = (255, 0, 0, "RED")
print(f"Point X: {point[0]}")

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Union: {set_a | set_b}") # {1, 2, 3, 4, 5}
print(f"Intersection: {set_a & set_b}")

total = 0
for value in [2, 3, 19]:
    for weight in [3, 2, 1]:
        total += value*weight
print(f'Total is: {total}')

from concurrent.futures import ProcessPoolExecutor
def cube(x):
    return x**3
with ProcessPoolExecutor(max_workers = 3) as executor:
    results = list(executor.map(cube, [1, 2, 3, 4]))
print(results)