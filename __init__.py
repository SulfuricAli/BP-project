from time import time
import math
class LCG:

    def __init__(self , seed= None):
        self.a = 214013# a = ((343FD)16 ,
        self.m = 2**32# Microsoft Visual C++
        self.c = c = 0
        self.x0 = seed
        self.x_previous = self.x_previous = (self.a * self.x0 + self.c) % self.m


    def int_generator(self , range=None):
        self.x_previous = (self.a * self.x_previous + self.c) % self.m

        if range is None:
            return self.x_previous
        else:
            return int((self.x_previous / (self.m - 1)) * (range[1] - range[0]) + range[0])


    def float_generator(self , range=None , decimal=None):
        self.x_previous = (self.a * self.x_previous + self.c) % self.m

        try:
            if decimal is None:
                return (self.x_previous / (self.m - 1)) * (range[1] - range[0]) + range[0]
            else:
                return round((self.x_previous / (self.m - 1)) * (range[1] - range[0]) + range[0] , decimal)

        except TypeError:
            print("Error : Range is required")


    def normal_genarator(self ,mean , variance , seed=None):

        if seed is None:
            num = LCG(seed=time())
            n1 = num.float_generator([0, 1])
            n2 = num.float_generator([0, 1])
            R = math.sqrt((-2) * math.log(n1, 10))
            theta = 2 * math.pi * n2
            X = R * math.cos(theta)

        else:
            num = LCG(seed)
            n1 = num.float_generator([0,1])
            n2 = num.float_generator([0,1])
            R = math.sqrt((-2)* math.log(n1,10))
            theta = 2* math.pi * n2
            X = R *math.cos(theta)

        return (X * (math.sqrt(variance))) + mean


num = LCG(seed=100)
print(num.normal_genarator(100,1000))
print(num.int_generator([0,7]))#sample x.int_generator([lower_bound , upper bound]) #upper bound not included
print(num.float_generator([0 , 7] , 2))
print(num.normal_genarator(0 , 1))
