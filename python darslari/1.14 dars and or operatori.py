kun = input("kunni kiriting : " )
harorat = float(input("haroratni kiriting : "))
#if kun.lower() =='yakshanba' and harorat>=30:
  #  print("basseynga cho'milgani boramiz ! ")
#else:
#    print("dam olamiz uyda")

if ( kun.lower() == 'shanba' or kun.lower()=='yakshanba') and harorat >=30:
    print( "dachaga boramiz ")
elif ( kun.lower() == 'shanba' or kun.lower()=='yakshanba') and harorat <=30:
    print("saunaga boramiz !")
else:
    print("ish kuni")
