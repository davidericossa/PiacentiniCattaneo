

class Polynomial:
    def __init__(self, coefficients=[]):
        self.coefficients=coefficients
    
    def plus(self,p):
        z=Polynomial(self.coefficients)
        for k, v in enumerate(p.coefficients):
            z.coefficients[k]+=v
        return z



    def conv_term(self, x, y, ithterm):
        y=y[:(ithterm+1)]
        addends=[x[ithterm-k]*v for k, v in enumerate(y)]
        return sum(addends)


    def multiplied(self, y):
        a=self.coefficients
        b=y.coefficients
        if len(b)>len(a):
            temp=a
            a=b
            b=temp
        d=len(a) + len(b) -2
        while len(a)<d+1:
            a.append(0)

        while len(b)<len(a):
            b.append(0)

        z=Polynomial([0]*(d+1))
        for i in range(d+1):
            z.coefficients[i]=self.conv_term(a,b,i)
        
        return z

    def divided(self, y):
        quotient=Polynomial([])
        reminder=Polynomial([])
        