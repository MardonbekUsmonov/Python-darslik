# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 17:35:25 2025

@author: user

FUNKSIYA NIMA?
Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.
Biz shu paytgacha bir nechta tayyor funksiyalardan foydalanib keldik.
Misol uchun print() funksiyasi konsolga matn chiqarish uchun,
range() funksiyasi esa ma'lum oraliqdagi sonlarni yaratish uchun ishlatiladi.  
"""
# def salom_ber():
#     """ Salom beruvchi funksiya """
#     print("Assalomu aleykum ! ")
# salom_ber()

# -----------------------------------------------------------------------------

"""FUNKSIYAGA QIYMAT UZATISH
Avvalgi sodda funksiyamiz foydalanivchidan hech qanday qiymat olmaydi
 va barchaga birday "Assalomu alaykum!" deb javob qiladi.
 Keling funksiyaga o'zgartirish kiritamiz, funksiya foydalanuvchi
 ismini qabul qilib, unga ismi bilan murojat qilsin. Buning uchun funksiya
 nomidan keyin, qavs ichida foydalanuvchi berishi kerak bo'lgan qiymatni 
 ko'rsatamiz."""
 
# def salom_ber(ism,familya):
#     """Fodyalanuvchi ismini va familyasini qabul qilib, unga salom beruvchi funksiya"""
#     print("Assalomu alaykum, hurmatli ", ism.title(), familya.title())
# salom_ber("Anvar", "Qosimov")

# -----------------------------------------------------------------------------

"""DOCSTRING
Avval aytganimizdek, funksiya yaratganda, funksiya qanday ishlashi 
haqida qisqacha ma'lumot berib ketish o'zimiz uchun ham, kelajakda
 bizni funksiyamizni ishlatadigan boshqa dasturchilar uchun ham juda 
 foydali bo'ladi. Quyidagi funksiyaning 2-qatorda biz funksiya haqida
 ma'lumot berdik. Bu qator docstring deyiladi. Murakkab funksiyalar uchun
 docstringni bir necha qatorga bo'lib yozishingiz mumkin """
 
# def salom_ber(ism):
#       """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#       print("Assalomu alaykum, hurmatli ", ism.title())
# salom_ber("Anvar")

 
# print(salom_ber.__doc__)
# print(print.__doc__)
# print(range.__doc__)



#  ----------------------------------------------------------------------------


"""ARGUMENT VA PARAMETER
Funksiya yaratishda, qavs ichida berilgan, funksiya to'g'ri ishlashi uchun
uzatiladigan qiymat parameter deb ataladi. Yuqoridagi misolda ism bu
salom_ber funksiyasining parametri. 

Foydalanuvchi funksiyaga murojat qilishda funksiyaga uzatgan qiymat
esa argument deb ataladi. salom_ber('hasan') kodida 'hasan' bu argument."""

"""FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH
Shunday funksiyalar bor, bir emas bir nechta parameter talab qilishi mumkin,
foydalanuvchi esa o'z navbatida bir nechta argumentlar taqdim qilishi kerak.
Funksiyaga argument uzatishning bir necha usuli bor, keling ular bilan 
birma bir tanishamiz. """

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism('obid','tursunov')














# Amaliyot 

"""Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi
funksiya yozing."""

# def kv_kub(son):
#     """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print("sonning kvadrati : ", son**2, "sonning kubi : ", son**3)

# kv_kub(11)

# -----------------------------------------------------------------------------

"""Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi 
funksiya yozing. """

def juftmi(son):
    """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son%2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")

juftmi(28)
juftmi(99)

# -----------------------------------------------------------------------------

"""Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi
funksiya yozing. 
Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring."""

# def solishtir(x,y):
#     """Ikki sonni solishtiruvchi funksiya"""
#     if x>y:
#         print(f"{x}>{y}")
#     elif x<y:
#         print(f"{y}>{x}")
#     else:
#         print(f"{x}={y}")

# solishtir(10,20)
# solishtir(-9,12)
# solishtir(15,15)

 
