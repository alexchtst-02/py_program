# counter little fermat theorem dan euler theorem
class RSA_kriptography(object):
    def __init__(self, p=None, q=None, pk=None, sk=None, C=None, M=None):
        self. p = p
        self.q = q
        self.pk = pk
        self.sk = sk
        self.M = M
        self.C = C 
    def encript(self):
        try:
            C = (self.M**self.pk) % (self.p*self.q)
            return(C)
        except ValueError():
            pass
    def descript(self):
        M = (self.C**self.sk) % (self.p*self.q)
        return(M)

class alantouring_1(object):
    def __init__(self, M=None, C=None, pk=None):
        self.M = M
        self.C = C
        self.pk = pk
    def encript(self):
        return(self.M*self.pk)
    def descript(self):
        return(self.C/self.pk)

# counter = algoritma euclid
class alantouring_2(object):
    def __init__(self, M, C, p, pk, sk):
        self.M = M
        self.C = C
        self.p = p
        self.pk = pk
        self.sk = sk
    def encript(self):
        C = self.M*self.pk % self.p
        return(C)
    def descript(self):
        M = self.C*self.sk % self.p
        return(M)