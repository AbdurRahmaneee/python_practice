class A:
    num = 20

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass
print(D.mro())

print(D.num)