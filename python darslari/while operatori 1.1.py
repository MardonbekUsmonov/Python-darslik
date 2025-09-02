# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 18:34:38 2025

@author: user

while TSIKLI BILAN TANISHAMIZ
Biz avvalroq for tsikli bilan tanishgan edik. for tsikli ma'lum bir
 ro'yxatni olib, ro'yxat ichidagi qiymatlar tugaginga qadar biror kodni
 takrorlar edi. while ham takrorlash operatori bo'lib, for dan farqli ravishda,
 toki ma'lum bir shart to'g'ri (True) bo'lsa, kodni takrorlayveradi.  
 ------------------------------------------------------------------------------
 while so'zi ingiz tilidan "toki" yoki "-gacha" deb tarjima qilinadi.
 ------------------------------------------------------------------------------
"""
# son = 1
# while son<=100: #toki son 10 dan kichik yoki teng bo'lguncha bajar
#     print(son, end=" ")
#     son+=2 # son = son + 1 
# print("\ndastur tugadi")


# print("\t\t\t...Istalgan sonni kvadratini qaytaruvchi dastur...")
# savol = "Istalgan sonni kiriting : \n (Dasturni to'xtatish uchun 'exit' deb yozing )"
# qiymat = ' '
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("dastur tugadi !")


# BREAK OPERATORI
# Break operatori yordamida ma'lum bir shartni tekshirish va while tsikli
 # bajarilishini to'xtatib qo'yish mumkin. 
 
print("\t\tKiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting \n(dasturni to'xtatish uchun 'exit' deb yozing) "

while True: # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # tsiklni to'xtatish
    else:
        print(float(qiymat)**3)
print("dastur tugadi")

