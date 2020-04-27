%Approximate ln(x)
import math

def ln_ex(n):
    x = n - 1
    i = 1
    Sum = 0
    while True:
        add = (pow(-1,i+1)*pow(x,i))/i
        if abs(add) < 1e-6:
            break
        Sum += add
        i += 1
        
    return Sum


def get_b(n):
    i=1
    while True:
        i+=1
        if (pow(2,i)>n):
            break
    return i


def la_ln(n):

    b=get_b(n)

    a=n/(pow(2,b))

    ln_2=ln_ex(2)
    ln_a=ln_ex(a)

    rslt=ln_a+b*ln_2

    return rslt

val_inp = float(input("Enter number: "))

n=val_inp
ln=la_ln(n)
print("ln=", ln)

