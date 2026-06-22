def choice():
    while True:
     print ("(1) to convert currencies")
     print ("(2) to convert temperatures")
     print ("(3) to convert weight")
     print ("(4) to convert distances")
     print ("(5) to exit")
     uchoice = input()
     if uchoice == "1":
         print ("(1)egp->dlr , (2)dlr->egp")
         print ("(3)dlr->ero , (4)ero->dlr")
         print ("(5)egp->ero , (6)ero->egp")
         suii = input()
         if suii == "1":
             egp = float(input("enter the egp pounds: "))
             print (egp * 0.0184500)
         elif suii == "2":
             dlr = float(input("enter the dlr pounds: "))
             print (dlr * 54.24)
         elif suii == "3":
             dr = float(input("enter the dlr pounds: "))
             print (dr * 0.8665)
         elif suii == "4":
              ero = float(input("enter the ero pounds: "))
              print (ero * 1.1540)
         elif suii == "5":
             eg = float(input("enter the egp ponds: "))
             print (eg * 0.016)
         elif suii == "6":
             er = float(input("enter the ero pounds: "))
             print (er * 62.54)
         else:
             print("sorry you you enterd wrong number")
     elif uchoice == "2":
           print ("(1)c->k , (2)c->f")
           print ("(3)k->c , (4)k->f")
           print ("(5)f->c , (6)f->k")
           sui = input()
           if sui == "1":
               cel = float(input("enter the cel temp: "))
               print (cel + 273.25)
           elif sui == "2":
               cl = float(input("enter the cel temp: "))
               print (1.8 * cl + 32)
           elif sui == "3":
               kel = float(input("enter the kelven temp: "))
               print (kel - 273.15)
           elif sui == "4":
               kl = float(input("enter the kelven temp: "))
               print ((kl - 273.15) * 1.8 + 32)
           elif sui == "5":
               fh = float(input("enter the fh temp: "))
               print ((fh - 32) / 1.8)
           elif sui == "6":
               fhr = float(input("enter the fh temp: "))
               print ((fhr - 32) / 1.8 + 273.15)
           else:
               print("sorry you enterd wrong number")
     elif uchoice == "3":
           print ("(1)g->kg , (2)g->tn")
           print ("(3)kg->g , (4)kg->tn")
           print ("(5)tn->g , (6)tn->kg")
           mt = input()
           if mt == "1":
               gram = float(input("enter the gram wieght: "))
               print (gram / 1000)
           elif mt == "2":
               gr = float(input("enter the gram wieght: "))
               print (gr / 1000000)
           elif mt == "3":
               kg = float(input("enter the kg wieght: "))
               print (kg * 1000)
           elif mt == "4":
               kilo = float(input("enter the kg wieght: "))
               print (kilo / 1000)
           elif mt == "5":
               ton = float(input("enter the tonne wieght: "))
               print (ton * 1000000)
           elif mt == "6":
               tn = float(input("enter the tonne wieght: "))
               print (tn * 1000)
           else:
               print("sorry you entered wrong number")
     elif uchoice == "4":
           print ("(1)cm->m , (2)cm->km")
           print ("(3)m->cm , (4)m->km")
           print ("(5)km->cm , (6)km->m")
           metter = input()
           if metter == "1":
               cm = float(input("enter the cm: "))
               print (cm / 100)
           elif metter == "2":
               cmet = float(input("enter the cm: "))
               print (cmet / 100000)
           elif metter == "3":
               metr = float(input("enter the metters: "))
               print (metr * 100)
           elif metter == "4":
               mt = float(input("enter the metters: "))
               print (mt / 1000)
           elif metter == "5":
               kil = float(input("enter the kilometters: "))
               print (kil * 100000)
           elif metter == "6":
               kelo = float(input("enter the kilometters: "))
               print (kelo * 1000)
           else:
               print("sorry you entered wrong number")
     elif uchoice == "5":
         break
     else:
         print("sorry you entered wrong number")
choice()