'''
[kubus] [balok] [tabung] [kerucut] [prisma segi-n] [limas segi-n] [bola]
[persegi] [persegi panjang] [lingkaran] [segi n]
'''

import math as m 

class cube():
    def __init__(self, r):
        self.r = r
    @property
    def volume(self):
        return((self.r)**3)
    @property
    def area_surface(self):
        return(6*(self.r)**2)

class block():
    def __init__(self, p, l, t):
        self.p = p
        self.l = l
        self.t = t
    @property
    def volume(self):
        return(self.p*self.l*self.t)
    @property
    def area_surface(self):
        return(2*(self.p*self.l + self.l*self.t + self.t*self.p))

class tube():
    def __init__(self, r, t):
        self.r = r
        self.t = t
    @property
    def volume(self):
        return((self.r**2)*self.t*m.pi)
    @property
    def area_surface(self):
        return(2*((self.r**2)*m.pi) + (2*m.pi*self.r*self.t))

class cone():
    def __init__(self, r, t):
        self.r = r
        self.t = t
    @property
    def volume(self):
        return((self.r**2)*self.t*m.pi/3)
    @property
    def area_surface(self):
        return(self.r*m.pi*(m.sqrt(self.r**2 + self.t**2)) + m.pi*self.r**2)

class prism():
    def __init__(self, r, t, n):
        self.r = r
        self.t = t
        self.n = n
    @property
    def volume(self):
        A_alas = self.n*self.r**2*m.sin(m.pi*2/self.n)/2
        return(self.t*A_alas)
    @property
    def area_surface(self):
        A_alas = self.n*self.r**2*m.sin(m.pi*2/self.n)/2
        s = 2*self.r*m.sin(m.pi/self.n)
        return(2*A_alas + self.n*self.t*s)

class pyramid():
    def __init__(self, n, r, t):
        self.r = r
        self.t = t
        self.n = n
    @property
    def volume(self):
        A_alas = self.n*self.r**2*m.sin(m.pi*2/self.n)/2
        return(self.t*A_alas/3)
    @property
    def area_surface(self):
        A_alas = self.n*self.r**2*m.sin(m.pi*2/self.n)/2
        s = 2*self.r*m.sin(m.pi/self.n)
        a = m.sqrt(self.t**2 + self.r**2 - (s/2)**2)
        return(A_alas + self.n*s*a/2)

class ball():
    def __init__(self, r):
        self.r = r
    @property
    def volume(self):
        return(4*m.pi*self.r**3/3)
    @property
    def area_surface(self):
        return(4*m.pi*self.r**2)

class square():
    def __init__(self, s):
        self.s = s
    @property
    def area(self):
        return(self.s**2)
    @property
    def perimeter(self):
        return(4*self.s)

class rectangle():
    def __init__(self, p, l):
        self.p = p
        self.l = l
    @property
    def area(self):
        return(self.p*self.l)
    @property
    def perimeter(self):
        return(2*(self.p + self.l))


class segi_n():
    def __init__(self, r, n):
        self.r = r
        self.n = n
    @property
    def area(self):
        return(self.n*(self.r**2)*m.sin(2*m.pi/self.n)/2)
    @property
    def perimeter(self):
        return(self.n*2*self.r*m.sin(m.pi/self.n))

class lingkaran():
    def __init__(self, r):
        self.r = r
    @property
    def area(self):
        return(m.pi*self.r**2)
    @property
    def perimeter(self):
        return(2*m.pi*self.r)
