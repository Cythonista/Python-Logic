class Logic(object):
    def AND(self, a, b):
        if(bool(a) and bool(b)):
            y = 1
        else:
            y = 0
        return y

    def TAND(self, a, b, c):
        # 3入力 1出力 AND
        if(bool(a) and bool(b) and bool(c)):
            y = 1
        else:
            y = 0
        return y

    def OR(self, a, b):
        if(bool(a) or bool(b)):
            y = 1
        else:
            y = 0
        return y

    def TOR(self, a, b, c):
        # 3入力 1出力 OR
        if(bool(a) or bool(b) or bool(c)):
            y = 1
        else:
            y = 0
        return y

    def NOT(self, a):
        if(bool(a)):
            y = 0
        else:
            y = 1
        return y

    def NAND(self, a, b):
        y = self.AND(a, b)
        y = self.NOT(y)
        return y

    def SNAND(self, a):
        # 1入力 1出力 NAND
        # NOTと等価
        y = self.NAND(a, a)
        return y

    def NOR(self, a, b):
        y = self.OR(a, b)
        y = self.NOT(y)
        return y

    def XOR(self, a, b):
        anot = self.NOT(a)
        bnot = self.NOT(b)
        anotb = self.AND(anot, b)
        abnot = self.AND(a, bnot)
        y = self.OR(anotb, abnot)
        return y

    def XNOR(self, a, b):
        y = self.XOR(a,b)
        y = self.NOT(y)
        return y

    def summaryA(self, a, func):
        print(' A | Y')
        for i in range(len(a)):
            print( ' ' + str(a[i]) + ' | ' + str(func(a[i])) )
        print('')

    def summaryAB(self, a, b, func):
        print(' A | B | Y')
        for i in range(len(a)):
            print( ' ' + str(a[i]) + ' | ' + str(b[i]) + ' | ' + str(func(a[i], b[i])) )
        print('')

    def summaryABC(self, a, b, c, func):
        print(' A | B | C | Y')
        for i in range(len(a)):
            print( ' ' + str(a[i]) + ' | ' + str(b[i]) + ' | ' + str(c[i]) + ' | ' + str(func(a[i], b[i], c[i])) )
        print('')
