class X: pass
class Y: pass
class Z: pass
class A(X,Y):pass
class B(Y, Z):pass
class M(A, B, Z):pass

print(M.__mro__)
 