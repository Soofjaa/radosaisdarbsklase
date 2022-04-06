import math
figura = int(input("Ar kādu figūru gribi darboties? Riņķis(1), četrstūris(2), trīsstūris (3)"))
if figura == 1:
  figurarek = int(input("Ko gribi rekināt, laukumu(11), radiusu(12) vai rinķa līniju(13)"))

  if figurarek == 11:
    rad = float(input("ievadi riņķa rādiusu!"))
    laukrink = (math.pi*rad*rad)
    print("laukums riņķim ir", laukrink , "!")

  if figurarek == 13:
    rad = float(input("ievadi riņķa rādiusu!"))
    rinklin = (math.pi*2*rad)
    print("riņķa līnijas garums ir", rinklin , "!")

  if figurarek == 12:
    radapr = float(input("Caur kādu lielumu rēķināsim, riņķa līnijas garumu(121) vai riņķa laukumu(122)!"))
    if radapr == 121:
      radlin = float(input("ievadi riņķa līnijas garumu!"))
      radgar = (radlin//2*math.pi)
      print("riņķa radiuss ir", radgar , "!")
    if radapr == 122:
      radlauk = float(input("ievadi riņķa laukumu!"))
      radgarr = (math.sqrt(radlauk//math.pi))
      print("riņķa radiuss ir", radgarr , "!")