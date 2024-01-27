#coding:utf-8
import hashlib
import sys
import time
import base64
import datetime
import os
os.system('cls' if os.name == 'nt' else 'clear')

def gecen(baslangic, bitis):
    sonuc = bitis - baslangic
    d= str(sonuc).split(":")
    dd= d[0]+":"+d[1]+":"+d[2][0:2]
    print (r"Program islemi  {}' surede bitirmistir.".format(dd))
    

print ("""
  ___ ___               .__   __________               __                
 /   |   \_____    _____|  |__\______   \______ __ ___/  |_  ___________ 
/    ~    \__  \  /  ___/  |  \|    |  _|_  __ \  |  \   __\/ __ \_  __ \
\    Y    // __ \_\___ \|   Y  \    |   \|  | \/  |  /|  | \  ___/|  | \/
 \___|_  /(____  /____  >___|  /______  /|__|  |____/ |__|  \___  >__|   
       \/      \/     \/     \/       \/                        \/       """)
aks=0
def yazi():
    global aks
    aks +=1
    sys.stdout.write("\r")
    sys.stdout.write(r"Denenen sifre sayisi = {}".format(aks))
    sys.stdout.write("\r")
    sys.stdout.flush()



def kmd5(hashmd5,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya1=open(liste,"r",encoding="UTF-8")
        dosya=dosya1.readlines()
    
        if len(hashmd5)==32 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                sifre1=sifre.encode('utf-8')
                dene=hashlib.md5(sifre1).hexdigest()
                if dene==hashmd5 :
                
                    print (r"---BASARİLİ---")
                    print (r"SİFRE = {}".format(sifre))
                    print (r"{} = {}".format(sifre,dene))
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print (r"\nBulunamadı :(\n")
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print ("Bu md5 değil!")
    except IOError:
        print ("Boyle bir dosya yok. Lutfen dosya adini ve uzantisini dogru gir.")
        sys.exit()
def kmd5salt(hashmd5,salt,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya1=open(liste,"r", encoding="UTF-8")
        dosya=dosya1.readlines()
        if len(hashmd5)==32 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                sifre1=str(salt)+str(sifre)
                dene=hashlib.md5(sifre1.encode('utf-8')).hexdigest()
                if dene==hashmd5 :
                
                    print ("---BASARİLİ---")
                    print (r"SİFRE = {}  ".format(sifre))
                    print (r"{} = {}:{}".format(sifre,dene,salt))
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print ("\nBulunamadi :(\n")
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print ("Bu md5 degil!")
    except IOError:
        print ("Boyle bir dosya yok. Lutfen dosya adini ve uzantisini dogru gir.")
        sys.exit()
def kmd5salt2(hashmd5,salt,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya1=open(liste,"r", encoding="UTF_8")
        dosya=dosya1.readlines()
        if len(hashmd5)==32 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                sifre1=str(sifre)+str(salt)
                dene=hashlib.md5(sifre1.encode('utf-8')).hexdigest()
                if dene.lower()==hashmd5.lower() :
                
                    print ("---KIRILDI---")
                    print ("KIRILAN SİFRE ={}   ".format(sifre))
                    print (r"{} = {} :{}".format(sifre,dene,salt))
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print ("\nBulunamadi :(\n")
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print ("Bu hash md5 degildir.")
    except IOError:
        print ("Boyle bir dosya yok! Lutfen dosya adini ve uzantisini kontrol et.")
        sys.exit()
def ksha224(hashsha224,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya1=open(liste,"r", encoding="UTF-8")
        dosya=dosya1.readlines()
        if len(hashsha224)==56 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                sifre1=sifre.encode('utf-8')
                dene=hashlib.sha224(sifre1).hexdigest()
                if dene==hashsha224 :
                
                    print ("---KIRILDI---")
                    print ("KIRILAN SİFRE = {}   ".format(sifre))
                    print (r"{} = {}".format(sifre,dene))
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print ("\nBulunamadi :(\n")
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print ("Bu hash sha224 degildir.")
    except IOError:
        print ("Boyle bir dosya yok! Lutfen dosya adini ve uzantisini kontrol et.")
        sys.exit()
def ksha1(hashsha1,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya1=open(liste,"r",encoding="UTF-8")
        dosya=dosya1.readlines()
        if len(hashsha1)==40 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                sifre1=sifre.encode('utf-8')
                dene=hashlib.sha1(sifre1).hexdigest()
                if dene==hashsha1 :
                
                    print ("---KIRILDI---")
                    print ("KIRILAN SİFRE = {}   ".format(sifre))
                    print ("\n{} = {}".format(sifre,dene))
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print ("\nBulunamadi :(\n")
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print ("Bu hash sha1 degildir.")
    except IOError:
        print ("Boyle bir dosya yok! Lutfen dosya adini ve uzantisini kontrol et.")
        sys.exit()
def ksha256(hashsha256,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya1=open(liste,"r", encoding="UTF-8")
        dosya=dosya1.readlines()
        if len(hashsha256)==64 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                sifre1=sifre.encode('utf-8')
                dene=hashlib.sha256(sifre1).hexdigest()
                if dene==hashsha256 :
                
                    print ("---KIRILDI---")
                    print ("KIRILAN SİFRE = {}   ".format(sifre))
                    print ("{} = {}".format(sifre,dene))
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print ("\nBulunamadi :(\n")
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print ("Bu hash sha256 degildir.")
    except IOError:
        print ("Boyle bir dosya yok! Lutfen dosya adini ve uzantisini kontrol et.")
        sys.exit()
def ksha384(hashsha384,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya1=open(liste,"r", encoding="UTF-8")
        dosya=dosya1.readlines()
        if len(hashsha384)==96 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                sifre1=sifre.encode('utf-8')
                dene=hashlib.sha384(sifre1).hexdigest()
                if dene==hashsha384 :
                
                    print ("---KIRILDI---")
                    print ("KIRILAN SİFRE = {}   ".format(sifre))
                    print ("{} = {}".format(sifre,dene))
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print ("\nBulunamadi :(\n")
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print ("Bu hash sha348 degildir.")
    except IOError:
        print ("Boyle bir dosya yok! Lutfen dosya adini ve uzantisini kontrol et.")
        sys.exit()
def ksha512(hashsha512,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya1=open(liste,"r", encoding="UTF-8")
        dosya=dosya1.readlines()
        if len(hashsha512)==128 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                sifre1=sifre.encode('utf-8')
                dene=hashlib.sha512(sifre1).hexdigest()
                if dene==hashsha512 :
                
                    print ("---KIRILDI---")
                    print ("KIRILAN SİFRE = {}   ".format(sifre))
                    print ("{} = {}".format(sifre,dene))
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print ("\nBulunamadi :(\n")
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print ("Bu hash sha512 degildir.")
    except IOError:
        print ("Boyle bir dosya yok! Lutfen dosya adini ve uzantisini kontrol et.")
        sys.exit()
def kbase64(hbase64):
    try:
        baslangic=datetime.datetime.now()
        dene=base64.b64decode(hbase64)
        print ("---KIRILDI---")
        print ("{} = {}".format(dene,hbase64))
        bitis=datetime.datetime.now()
        gecen(baslangic,bitis)
        sys.exit()
    except TypeError:
        print ("Bu hash base64 degildir.")

print ("""
 1 = md5 Decrypter
 2 = md5 (salt+md5) Decrypter
 3 = md5 (md5+salt) Decrypter
 4 = sha1   Decrypter
 5 = sha224 Decrypter
 6 = sha256 Decrypter
 7 = sha384 Decrypter
 8 = sha512 Decrypter
 9 = base64 Decrypter
""")

sec=input("Hash tipi seç = ")
if sec =="1":
    hashmd5=input("md5'i paste et = \n")
    liste=input("Wordlist dosyasinin pathini gir = ")
    kmd5(hashmd5,liste)
elif sec == "2":
    hashmd5=input("md5'i paste et = \n")
    salt=input("lutfen salt' i giriniz = \n")
    liste=input("Wordlist dosyasinin pathini gir = ")
    kmd5salt(hashmd5,salt,liste)

elif sec == "3":
    hashmd5=input("md5'i paste et = \n")
    salt=input("lutfen salt' i giriniz = \n")
    liste=input("Wordlist dosyasinin pathini gir = ")
    kmd5salt2(hashmd5,salt,liste)
elif sec == "4":
    hashmd51=input("Hashi paste et = \n")
    liste=input("Wordlist dosyasinin pathini gir = ")
    ksha1(hashmd51,liste)
elif sec == "5":
    hashmd5=input("Hashi paste et = \n")
    liste=input("Wordlist dosyasinin pathini gir = ")
    ksha224(hashmd5,liste)
elif sec == "6":
    hashmd5=input("Hashi paste et = \n")
    liste=input("Wordlist dosyasinin pathini gir = ")
    ksha256(hashmd5,liste)
elif sec == "7":
    hashmd5=input("Hashi paste et = \n")
    liste=input("Wordlist dosyasinin pathini gir = ")
    ksha384(hashmd5,liste)
elif sec == "8":
    hashmd5=input("Hashi paste et = \n")
    liste=input("Wordlist dosyasinin pathini gir = ")
    ksha512(hashmd5,liste)

elif sec == "9":
    hashmd5=input("Hashi paste et = \n")
    kbase64(hashmd5)
