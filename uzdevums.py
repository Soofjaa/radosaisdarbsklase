
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
  figurarek2 = int(input("Ko gribi rekināt, laukumu(21), diagonāli(22) vai perimetru(23)?"))

  if figurarek2 == 21: 
       a,b = float(input("ievadi četrstūra malu garumus!"))
       print("četrstūra laukums  ir", cetrsturis.laukums(a,b) , "!")

  if figurarek2 == 22:
        a,b = float(input("ievadi četrstūra malu garumus!"))
        print("četrstūra diagonāļu garums ir", cetrsturis.diagonalesgarums(a,b) , "!")

  if figurarek2 == 23:
        a,b = float(input("ievadi četrstūra malu garumus!"))
        print("četrstūra parimetrs  ir", cetrsturis.perimetrs(a,b) , "!")


if figura == 3:
  figurarek3 = int(input("Ko gribi rekināt, laukumu(31), augstumu(32) vai perimetru(33)?"))

  if figurarek3 == 31:
        laukveid = int(input("Kā gribi rekināt, caur Hērona teorēmu(311) vai caur augstumu?(312)"))

        if laukveid == 311: 
         a,b = float(input("ievadi trīsstūra malas un augstuma garumus!"))   
         print("trīsstūra laukums ir", trijsturis.laukums(a,b) , "!")

        if laukveid == 312:
            a,b,c = float(input("ievadi trīsstūra malas garumus!"))
            print("trīsstūra perimetrs ir", trijsturis.laukumstrissturis1(a,b,c) , "!")

  if figurarek3 == 32:
        a,b,c = float(input("ievadi trīsstūra malas garumus!"))
        print("trīsstūra perimetrs ir", trijsturis.perimetrstrissturis(a,b,c) , "!")

  if figurarek3 == 33:
         a,p = float(input("ievadi trīsstūra malu un perimetru!"))   
         print("trīsstūra austums ir", trijsturis.augstumstrissturis(a,p) , "!")

  