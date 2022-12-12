from math import * # * - kõik funktsioonid moodulist
from random import *
from stringprep import c22_specials
#import math          math.funktsioonid()
#12/12/22
#1
print("Puu läbimõõdu arvutamine")
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peae puu läbimõõdu.
C=float(input("Anna ümbermõõd: "))
d=round(C/pi,2)

print(f"Puu läbimõõt = {d}")
#2
print("Ristkülikukujulise maatüki diagonaal pikk")
N=float(input("Sisesta N: "))
M=float(input("Sisesta M: "))
d=round(sqrt(N**2+M**2),2)
print("Ristkülikukujulise maatüki diagonaal pikk: ", round(d,2))

#3 
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")

#4
A1=int(input("Esimene arv: "))
A2=int(input("Teine arv: "))
A3=int(input("Kolmas arv: "))
A4=int(input("Neljas arv: "))
A5=int(input("Viies arv: "))
K=(A1+A2+A3+A4+A5)/5
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