#https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2020/formula_od_2015/informatyka/MIN-R2_1P-202.pdf
from sympy import isprime
file=open("przyklad.txt", "r")
pairs=list(map(str.strip, file))
pairs = [item.split(" ") for item in pairs]
#4.1
numbers=[]
for pair in pairs:
    numbers.append(pair[0])
numbers1=[]
for i in numbers:
    if int (i)>4 and float(i)%2==0:
        numbers1.append(i)
for i in numbers1:
    for n in range(int(i)+1):
        if isprime(n) and isprime(int(i)-n):
            print(i, n, int(i)-n)
            break
#4.2
words=[]
for pair in pairs:
    words.append(pair[1])
print(words)
for word in words:
    counter = 1
    biggest= 0
    b=0
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            counter+=1
        else:
            if counter>biggest:
                biggest=counter
                b=i-1
            counter=1
    print(biggest, word[b])
#4.3
