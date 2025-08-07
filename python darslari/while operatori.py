# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Muallif : Mardonbek Usmonov
sana : 07.12.2023
Mavzu : While sikli
while so'zi ingiz tilidan "toki" yoki "-gacha" deb tarjima qilinadi.
"""

# a = 1 # son ga 1 qiymatini beramiz
# while a<=100: # toki son 5 dan kichik yoki teng ekan...
#     print(a, end=" ") # son ni konsolga chiqaramiz,
#     a = a+2 # songa 1 qo'shamiz.






# # n gacha bo'lgan sonlarni yig'indisi topish dasturi
# n = int(input("  sonini kiriting : "))
# sum = 0
# i = 1
# while i <= n :
#     sum = sum + i
#     i = i + 1
      
# print(f"yig'indi {sum} ga teng")





# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing):"
# a = ''
# while a != 'exit':
#     a = input("Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing):")
#     if a != 'exit':
#         print(int(a)**2)
# print("Dastur tugadi")


# Break operatori yordamida ma'lum bir shartni
 # tekshirish va while tsikli bajarilishini to'xtatib qo'yish mumkin. 


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(int(qiymat)**3)



# Continue operatori esa aksincha, ma'lum bir shart bajarilganda qadam tashlab o'tish uchun mo'ljallangan.

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 1: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning 10 - darajasi {son**3} ga teng")


# WHILE YORDAMIDA RO'YXATNI TO'LDIRISH

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break


# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())


# WHILE YORDAMIDA LUG'ATNI TO'LDIRISH

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# RO'YXAT ELEMENTLARINI O'CHIRISH

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)



# RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH



# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho