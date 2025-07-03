import random

angka_rahasia = random.randint(1, 100)
ronde = 0
max_ronde = 8

print("======== TEBAK ANGKA =========")
print("saya telah memilih suatu angka neng/kang, dari 1-100")
print("Kau tebak angka itu, kau punya "+ str(max_ronde)+"kesempatan")
while(ronde < max_ronde):
    tebakan= int(input("Masukan tebakan mu: ")) 
    ronde +=1

    if(tebakan < angka_rahasia):
        print("Tebakan terlalu kecil")
    elif(tebakan > angka_rahasia):
        print("Tebakan terlalu besar")
    else:
        print("Wow jago eug ketang si eta otak n encer")
        exit(0)
    print("Kesempatan tersisa: "+str(max_ronde - ronde))
    print("______________________________________________")
print("Tos akhh lewih ti batas")
print("Angka rahasia nya adalah => "+ str(angka_rahasia))