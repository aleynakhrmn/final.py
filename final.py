#1.SORU
import datetime
content = input(" TARİH GİRİŞİNİZİ YAPINIZ: ")
gün,ay,yıl = content.split("-")
aylar={
    '1':'Ocak',
    '2':'Şubat',
    '3':'Mart',
    '4':'Nisan',
    '5':'Mayıs',
    '6':'Haziran',
    '7':'Temmuz',
    '8':'Ağustos',
    '9':'Eylül',
    '10':'Ekim',
    '11':'Kasım',
    '12':'Aralık'
}
if ay=="1":
    print(gün,aylar["1"],yıl)
elif ay=="2":
    print(gün,aylar["2"],yıl)
elif ay=="3":
    print(gün,aylar["3"],yıl)
elif ay=="4":
    print(gün,aylar["4"],yıl)
elif ay=="5":
    print(gün,aylar["5"],yıl)
elif ay=="6":
    print(gün,aylar["6"],yıl)
elif ay=="7":
    print(gün,aylar["7"],yıl)
elif ay=="8":
    print(gün,aylar["8"],yıl)
elif ay=="9":
    print(gün,aylar["9"],yıl)
elif ay=="10":
    print(gün,aylar["10"],yıl)
elif ay=="11":
    print(gün,aylar["11"],yıl)
elif ay=="12":
    print(gün,aylar["12"],yıl)
else:
    print("YANLIŞ BİLGİ GİRİŞİ MEVCUT")








#2.soru

def durum1(x)
    fact=1;
    for i in range(1,(3*x)+1):
        fact=fact*i
        return fact












#4.SORU

A = 1
L = 13

print(A, "ile" ,L, "arasındaki asal sayılar:")

for sayi in range(A,L + 1):
    if sayi > 1:
        for i in range(2, sayi):
            if (sayi % i) == 0:
                break
        else:
            print(sayi)


