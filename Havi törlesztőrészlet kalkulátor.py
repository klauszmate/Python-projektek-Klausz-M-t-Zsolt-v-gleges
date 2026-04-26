toke=int(input("Kérem adja meg a befektetni kívánt tőkéjét! (Ft)\n"))
kamatlab=int(input("Kérem adja meg a kamatlábat! (%)\n"))
ev=int(input("Kérem adja meg az befektetés időtartamát! (év)\n"))

n = ev * 12
r=kamatlab/100/12
#A kalkulátor

havi_torleszto_reszlet= toke * r * (1+r)**n / ((1 + r)**n -1)

print(f"A havi törlesztőrészlete így: \n"
      f"{round(havi_torleszto_reszlet,2)} Ft lesz ennyi hónapra")
