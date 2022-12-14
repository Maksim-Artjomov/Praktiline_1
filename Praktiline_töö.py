from ast import If
from math import *
from operator import ifloordiv # * - kõik funktsioonid moodulist
from random import *
from stringprep import c22_specials
#import math          math.funktsioonid()
#14/12/22
#Ülesanne "Ema robot".
print("Ema: mis hinde sa koolis said? ")
a=input("Sisesta: ")
print(a.isalpha(), a.isdigit())
if a.isdigit() and int(a)>0 and int(a)<=5:
    a=int(a)
    if a==5:
        pass
    elif a==4:
        pass
    elif a==3:
        pass
    elif a==2 or a==1:
        pass
else:
    print("Sa valesti vasta!")





#12/12/22
#1
print("Puu läbimõõdu arvutamine")
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peae puu läbimõõdu.
try:
    C=float(input("Anna ümbermõõd: "))
    if C<0:
    
        d=round(C/pi,2)
        print(f"Puu läbimõõt = {d}")
    else:
        print("C peab olema suurem kui 0")
except:
    print("Andmetüüp on vale")

#2
print("Ristkülikukujulise maatüki diagonaal pikk")
try:
    N=float(input("Sisesta N: "))
    M=float(input("Sisesta M: "))
    if M<0 and N<0:
        d=round(sqrt(N**2+M**2),2)
        print("Ristkülikukujulise maatüki diagonaal pikk: ", round(d,2))
except:
    print("M ja N vaja sisestada float formaadis")

#3 
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    if aeg>0 and teepikkus>0:
        kiirus = teepikkus / aeg
except:
    print("aeg ja teepikkus vaja sisestada float formaadis")
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#4
A1=int(input("Esimene arv: "))
A2=int(input("Teine arv: "))
A3=int(input("Kolmas arv: "))
A4=int(input("Neljas arv: "))
A5=int(input("Viies arv: "))
if A1>0 and A2>0 and A3>0 and A4>0 and A5>0:
    K=(A1+A2+A3+A4+A5)/5
else: 
    print("aeg ja teepikkus vaja sisestada float formaadis")
print(f"Keskmine on {K}")

#5
print("     @..@")
print("    (----)")
print("   ( \__/ )")
print('   ^^ "" ^^ ')

#6
a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
P=a+b+c
print(f"Ümbermõõt on {P}")

#7
P=randint(1,6)
summa=(12.90*1.1)/P
print(f"{P}-st, Igaüks maksab {summa} ")

#8
print("Kütusekili arvutamine")
l=float(input("Kütuse liitride: "))
km=float(input("Läbitud kilomeetrid: "))
kulu=(l/km)*100
print(f"Kütusekulu {kulu}")

#9
print("Rulluisutajad")
M=int(input("minutid: "))
M=M/60
tee=M*29.9
print(f"Jõuab {tee} km")

#10
print("Ajateisendus")
M=int(input("Sisetajad aja minutid: ")) #1h=60min
H=M//60 #h
M=M%60 #min
print(f"{H}:{M}")