mehmonlar = ['ali', 'vali', 'shoh', 'olim']
ism = input("Ismingizni kiriting: ")
if ism.lower() in mehmonlar:
    print("Hush kelipsiz , ",ism.title())
else:
    print("Sizga kirish mumkin emas.", ism.title())
