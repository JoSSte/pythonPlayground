phi = (1 + 5 ** 0.5) / 2

def getfibonacci(n):
    return round((phi ** n - (-1/phi) ** n)/ 5 ** 0.5)
max = 90 #not over 9999
npadding = 2
if (max > 999):
    npadding = 4
if (max > 99):
    npadding = 3

fpadding = len(str(getfibonacci(max)))

for x in  range (1,max):
    fib = str(getfibonacci(x)).rjust(fpadding)
    n = str(x).rjust(npadding)
    print (f'{n}: {fib}')
