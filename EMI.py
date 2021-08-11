p=float(input('Enter the Principle Value: '))

r=float(input('Enter the rate (in % p.a.): '))

n=float(input('Enter Time Period in years: '))

r=r/(12*100)

n=n*12

emi=(p*r*(1+r)**n)/((1+r)**n -1)

print("EMI per month is: ",emi)