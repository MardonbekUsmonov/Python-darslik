# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 16:03:11 2025

@author: user
"""
# Savol 
""" x,y haqiqiy sonlari berilgan. Ularning kichigini 
sonlar yig’indisining yarmiga, kattasini ko’paytmasining 
ikkilanganiga almashtiruvchi programma tuzilsin.
 Agar sonlar teng bo'lsa, o'zgarishsiz qoldirilsin."""
 
x,y = map(float, input("ikita son kiriting : ").split())
if x<y :
    print((x+y)/2)
elif x>y:
    print(x*y*2)
else:
    print(x,y)