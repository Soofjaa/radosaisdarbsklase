import math
import rinkis
import trijsturis
import cetrsturis

figura = int(input("Ar kādu figūru gribi darboties? Riņķis(1), četrstūris(2), trīsstūris (3)?"))
if figura == 1:
  figurarek = int(input("Ko gribi rekināt, laukumu(11), radiusu(12) vai rinķa līnijas garumu(13)"))

  if figurarek == 11:
    rad = float(input("ievadi riņķa rādiusu!"))
    print("laukums riņķim ir", rinkis.rinkislaukums(rad) , "!")

  if figurarek == 13:
    rad = float(input("ievadi riņķa rādiusu!"))
    print("riņķa līnijas garums ir", rinkis.rinkislinijagarums(rad) , "!")

  if figurarek == 12:
    radapr = float(input("Caur kādu lielumu rēķināsim, riņķa līnijas garumu(121) vai riņķa laukumu(122)!"))

    if radapr == 121:
      radlin = float(input("ievadi riņķa līnijas garumu!"))
      print("riņķa radiuss ir", rinkis.radiussnolinijas(radlin) , "!")

    if radapr == 122:
      radlauk = float(input("ievadi riņķa laukumu!")) 
      print("riņķa radiuss ir", rinkis.radiussnolaukumaa(radlauk) , "!")


if figura == 2:
  figurarek = int(input("Ko gribi rekināt, laukumu(21), diagonāli(22) vai perimetru(23)?"))
   if 


if figura == 3:
    figurarek = int(input("Ko gribi rekināt, laukumu(31), augstumu(32) vai perimetru(33)?"))
  