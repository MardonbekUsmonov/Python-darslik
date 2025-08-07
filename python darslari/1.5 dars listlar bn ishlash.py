# listlar( ro'yhatlar) [ ] (matn, son, aralash holatda bo'lishi mumkin)
a = 5
ism = "Abdulloh"
mevalar = [ "olma" , "behi" , "anor" , "gilos" , "shaftoli" , "banan" ]
narhlar = [ 1200, 1400,700, 2500, 9000,15000]
sonlar = [ "bir" , 2 , "uch", 4 , "besh" , 6]
ismlar = [ ]

#print("meva nomi : " , mevalar[0], "meva narxi : " , narhlar[4], "so'm", "tartib raqami : ", sonlar[0])
#print(narhlar[-2])
#print(sonlar[-3])
#print(narhlar[0] + narhlar[-1])
#print("eng kichik qiymati " , min(narhlar))
#print("eng katta qiymat " , max(narhlar) )
#print("umumiy yig'indisi : " , sum(narhlar))

#append() - ro'yhatni oxiriga qiymat qo'shadi
#insert() - ro'yhatni istalgan joyiga index bo'yicha qiymat qo'shadi
#del - ro'yhatni indexsi bo'yicha o'chiradi
# remove() - ro'yhatni qiymati bo'yicha o'chiradi
ismlar.append("olim")
ismlar.append("zokir")
ismlar.append("nodir")
mevalar.append("uzum")
#print(ismlar)
#print(mevalar)
narhlar.insert(0, 500)
mevalar.insert(1,"nok")
#print(narhlar)
#print(mevalar)
del mevalar[-1]
del mevalar[0]
sonlar.remove("bir")
mevalar.remove("behi")
print(mevalar)
print(sonlar)
