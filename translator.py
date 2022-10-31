import math as m 
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
class generator(object):
    def __init__(self, word=None, num=None):
        self.w = word
        self.n = num
    def num(self):
        al_list = list(self.w)
        n = 0
        j = len(al_list)-1
        try:
            for i in al_list:
                n = n + (alphabet.index(i.capitalize())+1)*(100**(j))
                j = j-1
            return(n)
        except ValueError():
            pass

    def num_slicer(self):
        num_list = []
        i = m.floor(m.log(self.n)/m.log(100))
        while i >= 0:
            num_list.append(self.n//(100**i))
            self.n = self.n % (100**i)
            i = i - 1
        return(num_list)

    def word(self):
        al_list = []
        i = m.floor(m.log(self.n)/m.log(100))
        while i >= 0:
            al_list.append(m.floor(self.n//(100**i)))
            self.n = self.n % (100**i)
            i = i - 1
        text = ''
        for char in al_list:
            text = text + alphabet[char-1]
        return(text)
