import random

def sayi_tahmin():
    tutulan_say = random.randint(1,100)
    tahmin_hakki = 4
    while tahmin_hakki > 0:
        sayi= int(input("1-100 'e kadar sayı giriniz:"))

        if tutulan_say == sayi:
            print("Tebrikler kazandın")
        elif sayi < tutulan_say:
            print("Tekrar dene !")
        elif sayi > tutulan_say:
            print("Tekrar dene !")
        else :
            print("Hata !!!")
        tahmin_hakki -= 1
    print(f'Hakkın bitti, tutulan sayı :',tutulan_say)    

sayi_tahmin()

