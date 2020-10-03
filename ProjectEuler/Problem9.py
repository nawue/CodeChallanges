# a + b + c = 1000
# a² + b² = c²
# a < b < c
import math
import
impor

a=0
b=0
c = 0
for c in range(3,997):
    for b in range(2, 996):
        for a in range(1,995):
            if a+b+c == 1000 and pow(a,2)+pow(b,2) == pow(c,2):
                if a < b and b < c:
                    print("a: {} b: {} c: {}".format(a,b,c))

