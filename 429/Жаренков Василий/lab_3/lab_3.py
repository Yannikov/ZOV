#print(len("ЖаренковВасилийАндреевич")%5)
import numpy as np
import matplotlib.pyplot as plt
import math
    
# метод простой итерации

def f(x):
        return 2*np.sin(x)-math.atan(x)+x
def iter(x, e, it):
    temp =x
    x = f(x)
    it=it + 1
    if abs(temp - x) > e:
        iter(x, e, it)    
    else:
        print("Результат: x= ",x,"Кол-во итераций=", it )
e = float(input("Введите точность вычисления:"))
it=0
x=2.6
it=1
iter(x, e, it)
