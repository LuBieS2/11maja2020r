#https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2020/formula_od_2015/informatyka/MIN-R2_1P-202.pdf
from sympy import isprime
file=open("przyklad.txt", "r")
pairs=list(map(str.strip, file))
pairs = [item.split(" ") for item in pairs]
print(pairs)
numbers=[]
for pair in pairs:
    numbers.append(pair[0])
print(numbers)
numbers1=[]
for i in numbers:
    if int (i)>4 and float(i)%2==0:
        numbers1.append(i)
print(numbers1)
for i in numbers1:
    for n in range(i+1):
        if isprime(n)==True:
            print(i, n, int(i)-n)