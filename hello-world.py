#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 22:47:51 2022

@author: zavharbek
"""
#lesson 2

#print("Hello world!")

#lesson 3
 
#print("Hayrli tong!")
#print ("Men \"Dell\" markasidagi komputer sotib oldim")
#print(15/4)
#print(15//4)
#print("To'qizning kvadrati", 9**2, "ga teng")
#print('"Nexia", "Tico", \'Damas\' ko\'rganlar qilar havas')
#print(22%4)

#lesson 4

#ism="Abdulloh"
#yosh=25
#print(ism)
#print(yosh)

#ism="Abdullok"
#print(ism)
#ism="Muhammad"
#print(ism)

#a=6
#b=7
#c=(a+b)**2
#print(c)

#a ="Hello World"
#print(a)

#xabar ="He is the best programmer in the world"
#print(xabar)
#xabar = "He also helps everyone everyday"
#print(xabar)

#radius = 5
#pi = 3.14159
#aylana_yuzi = pi * radius**2
#print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

# Lesson 5

# ism="Zavharbek"
# shahar = "Pop"
# viloyat = "Namangan"
# matn ="Men yangi 🎸 sotib oldim"
# smaylik ="😃"
# print(matn)

#string ustida amallar

# ism = 'Abror'
# familiya = 'Anvarov'
# print(ism + familiya)
# print(ism + ' ' + familiya)

#f-string

# ism="Abror"
# familiya='Anvarov'
# ism_sharf=f"{ism} {familiya}"
# print(ism_sharf)

# ism='Ahad'
# familiya='Qayum'
# ism_sharif=f"{ism} {familiya}"
# print(ism_sharif)

# ism="James"
# familiya="Bond"
# print(f"Salom, mening ismim {ism}. {ism} {familiya}!")

# Maxsus belgilar

# print("Hello World!")
# print("Hello \tWorld!")
# print('Hello \nWorld!')

#String metodlari

# ism='james'
# familiya='bond'
# ism_sharf=f"{ism} {familiya}"
# ism_sharif = ism_sharf.upper()
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())

# meva = "     meva     "
# print(meva)
# print("Men "+ meva.lstrip()+ "yaxshi ko'raman")
# print("Men" + meva.rstrip()+ " yaxshi ko'raman")
# print("Men" + meva.strip()+ " yaxshi ko'raman")
# print("Men" + meva + " yaxshi ko'raman")

#INPUT

# ism = input("Ismingiz nima?")
# print("Assalomu alaykum, " + ism)

# ism = input("Ismingiz nima?\n>>>")
# print("Assalomu alaykum, " + ism.title())

#Homework

# kocha ="Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(kocha + " ko'chasi", mahalla + " mahallasi", tuman + " tumani", viloyat + " viloyati")

#kocha = input("Ko'cha nomini kiriting")
#print(kocha)

#lesson 6 Sonlar

# a=20
# b=5.5
# temp=36.6 
# # print(type(a))
# aholi_soni=7_594_376_567
# print("Aholi soni:", aholi_soni)

# x,y,z = 10, 5.5, -56

# c=a*b
# print(c)
# d=100//2
# print(d)

# radius = 20
# PI=3.14159
# diameter = 2*radius
# print("Aylananing uzunligi=", PI*diameter)

# ism="Abror"
# yosh = 28
# # yosh = str(yosh)
# xabar = ism + " " + str(yosh) + " yoshda"
# print(xabar)

# t_yil=int199(input("Tug'ilgan yilingizni kiriting: "))
# yosh=2023-t_yil
# print("Siz", yosh, " yosh ekansiz" )

# a=int("10")
# b=float("10")
# temp=str(36.6)

# lesson 7 LIST (RO'YXAT')

# mevalar=['olma', 'anjir', 'shaftoli', "o'rik"] #mevalar ro'yxati(matnlar)
# narxlar=[1200, 13000, 14000, 17000] #narxlar ro'yxati
# sonlar= ['bir', 'ikki', 3, 4,5] #sonlar va matnlar aralash ro'yxati
# ismlar=[] #bo'sh ro'yxat

#print(mevalar[2])
#print(mevalar[-1]) #oxirgi elementni console ga chiqaradi

#mevalar.append() #oxiriga yangi meva nomini qo'shadi
#mevalar.insert(3, "ananas") #bunda nechinchi tartibga ekanligi va nomini kiritiladi

# cars =[]
# cars.append("Genta")
# cars.append("Cobalt")
# cars.append("Spark")
# cars.append("Malibu")
#print(cars)

#del cars[0] #ro'yxatdan bitta elementni o'chiradi
#print(cars)

#cars.insert(0,"Nexia 3") #1 chi tartibga yangi element qo'shadi
#print(cars)

#cars.remove("Malibu") #element index tartibini bilmaganimizda ishlatamiz
#print(cars)

# hayvonlar =["it", "mushuk", "sigir", "qo'y", "quyon", "mushuk"]
# hayvonlar.remove("mushuk") #Ro'yxatda ikkita mushuk bor, ulardan birinchisini o'chirib yuboradi
# print(hayvonlar)

# bozorlik =["yog'", "un", "piyoz", "banan", "go'sht"]
# mahsulot = bozorlik.pop(3) #Ro'yxardan bananni sug'urib oladi
# print("Men " + mahsulot+ " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

#Ro'yxatlar bilan ishlash

# cars =["bmw", "mercedence benz", "volvo","general motors","tesla","audio"]
# cars.sort() # alfabetik tartibda tartiblab beradi
# print(cars)

### Katta va kichik harf
# cars =["Bmw", "mercedence benz", "volvo","general motors","tesla","audio"] #sort qilganimizda katta harflar kichik harflardan oldin keladi
# cars.sort()
# print()

#Teskari tartib 
cars =["bmw", "mercedence benz", "volvo","general motors","tesla","audio"]
cars.sort(reverse=True)
print(cars)






            




