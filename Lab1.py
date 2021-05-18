import math

# ????
def fn(x):
    # return math.sin(x)+math.cos(x)
    return x ** 2

# Метод прямоугольников
def rect_integral(f,xmin,xmax,n):
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*f(x)
        x+=dx
    return area

# Метод трапеций
def tr_integral(f,xmin,xmax,n):
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*(f(x)+f(x+dx))/2
        x+=dx
    return area

# Метод симпсона
def simpsons_( ll, ul, n ):
    # Расчет значения h
    h = ( ul - ll )/n
    # Список для хранения значений x и f (x)
    x = list()
    fx = list()  
    # Расчет значений x и f (x)
    i = 0
    while i<= n:
        x.append(ll + i * h)
        fx.append(fn(x[i]))
        i += 1
    # Расчет результата
    res = 0
    i = 0
    while i<= n:
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res    



lower_limit = 0   # Нижний предел
upper_limit = 2 # Верхний предел
n = int(1e6) #Номер интервала

# print("simpson = {0:.5f}".format(simpsons_(lower_limit, upper_limit, n)))
# print("rect_integral = {0:.5f}".format(rect_integral(fn, lower_limit,upper_limit, n)))
# print("tr_integral = {0:.5f}".format(tr_integral(fn, lower_limit, upper_limit, n)))