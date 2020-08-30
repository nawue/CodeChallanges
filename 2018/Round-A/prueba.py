#1
#5
#axpaj apxaj dnrbt pjxdn abd
# a  a  50 1 1 1 30
# S1 S2 N  A B C D
# xi = ( A * xi-1 + B * xi-2 + C ) modulo D.

S1 = 'a'
S2 = 'a'
N = 50
A=1
B=1
C=1
D=30

x = []
s = []
x.append(ord(S1))
x.append(ord(S2))
s.append(S1)
s.append(S2)

for i in range(2,50):
    x.append((A*x[i-1] + B * x[i-2] + C) % D)
    s.append(chr('a' + x[i]%26))
