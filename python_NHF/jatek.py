import curses
import random
import time
import fajlkezeles
import megjelenites
import os
from curses.textpad import Textbox, rectangle


def nyeremeny(szint,menu):
	stdscr = curses.initscr()
	hossz, szeleseg = stdscr.getmaxyx()
	for i, sor in enumerate(menu):
		x = szeleseg//2 - len(sor) + 59
		y = hossz//2 + len(menu)//2 - i
		if i == szint:
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(y, x, sor)
			stdscr.attroff(curses.color_pair(1))
		else:
			stdscr.addstr(y, x, sor)
	stdscr.refresh()
	
def aktualis_menu(y,x,lista,betu):
	stdscr = curses.initscr()
	stdscr.refresh()
	stdscr.attron(curses.color_pair(1))
	stdscr.addstr(y,x,lista)
	stdscr.addstr(y,x-len(betu),betu)
	stdscr.attroff(curses.color_pair(1))
	rectangle(stdscr,y-1,x-3,1+(y-1)+1,x+len(lista))

def valasztasi_lehetosegek(aktualis_sor,aktualis_oszlop,ABCD,felezo,kozonseg,felezo_tomb):
	stdscr = curses.initscr()
	if felezo_tomb[0]==1:
		if 0 == aktualis_sor and 0 == aktualis_oszlop:
				aktualis_menu(16,20,ABCD[0],"A:")
		else:
				stdscr.addstr(16,20,ABCD[0])
				stdscr.addstr(16,18,"A:")
				rectangle(stdscr,15,17,1+15+1,20+len(ABCD[0]))       
	if felezo_tomb[1]==1:
		if 0 == aktualis_sor and 1 == aktualis_oszlop:
				aktualis_menu(16,70,ABCD[1],"B:")
		else:
				stdscr.addstr(16,70,ABCD[1])
				stdscr.addstr(16,68,"B:")
				rectangle(stdscr,15,67,1+15+1,70+len(ABCD[1]))
	if felezo_tomb[2]==1:
		if 1 == aktualis_sor and 0 == aktualis_oszlop:
				aktualis_menu(20,20,ABCD[2],"C:")
		else:
				stdscr.addstr(20,18,"C:")
				stdscr.addstr(20,20,ABCD[2])
				rectangle(stdscr, 19,17 ,1+19+1,20+len(ABCD[2]))
	if felezo_tomb[3]==1:
		if 1 == aktualis_sor and 1 == aktualis_oszlop:
				aktualis_menu(20,70,ABCD[3],"D:")

		else:
				stdscr.addstr(20,68,"D:")
				stdscr.addstr(20,70,ABCD[3])
				rectangle(stdscr,19,67,1+19+1,70+len(ABCD[3]))

	if felezo == 0:
		if 2 == aktualis_sor and 0 == aktualis_oszlop:
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(26,19,"Felező")
			stdscr.attroff(curses.color_pair(1))
		else:
			stdscr.addstr(26,19,"Felező")

	if kozonseg == 0:
		if 2 == aktualis_sor and 1 == aktualis_oszlop:
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(26,28,"Közönség segítsége")
			stdscr.attroff(curses.color_pair(1))
		else:
			stdscr.addstr(26,28,"Közönség segítsége")

def kerdes_generator(szint,kerdesek):
	felso_index=-1
	also_index=0
	for i in range(len(kerdesek)):
		if kerdesek[i].szint<=szint:
			felso_index+=1
		if kerdesek[i].szint <szint:
			also_index+=1
	k_index=random.randint(also_index,felso_index)
	return k_index

def segitseg_felezo(index,valaszok,kerdesek,felezo):     
	stdscr = curses.initscr()
	helyes_valasz_idx=0
	abcd=["A","B","C","D"]
	rossz_valaszok=0
	elso_rossz=-1
	for i in range(4):     
		if abcd[i]==valaszok[index].helyes:
			helyes_valasz_idx=i
	while rossz_valaszok!=2:
		masik=random.randint(0,3)
		if masik!=helyes_valasz_idx and elso_rossz != masik:
			rossz_valaszok+=1
			if elso_rossz == -1:
				elso_rossz=masik
			felezo[masik]=0
	return felezo

def segitseg_kozonseg(helyes):
	stdscr = curses.initscr()
	abcd = ["A","B","C","D"]
	kozonseg = 10 #<-100%
	helyes_valasz = random.randint(5,kozonseg)
	kozonseg -= helyes_valasz
	masik_1 = random.randint(0 ,kozonseg)
	kozonseg -= masik_1
	masik_2 = random.randint(0 ,kozonseg)
	masik_3 = kozonseg - masik_2 #maradek
	for i in range(len(abcd)):
		if helyes == abcd[i]:
			abcd[i] = helyes_valasz
	for i in range(len(abcd)):
		if abcd[i] in ["A","B","C","D"] and masik_1 != -1:
			abcd[i] = masik_1
			masik_1 =-1
		if abcd[i] in ["A","B","C","D"] and masik_2 != -1:
			abcd[i] = masik_2
			masik_2 =-1
		if abcd[i] in ["A","B","C","D"] and masik_3 != -1:
			abcd[i] = masik_3
			masik_3 =-1
	if abcd[0] > 0:
		rectangle(stdscr, 25-abcd[0] ,98 , 1+24+1  ,100)
	if abcd[1] > 0:
		rectangle(stdscr, 25-abcd[1] ,101 , 1+24+1  ,103)
	if abcd[2] > 0:
		rectangle(stdscr, 25-abcd[2] ,104 , 1+24+1  ,106)
	if abcd[3] > 0:
		rectangle(stdscr, 25-abcd[3] ,107 , 1+24+1  ,109)
	stdscr.addstr(26,99,"A")
	stdscr.addstr(26,102,"B")
	stdscr.addstr(26,105,"C")
	stdscr.addstr(26,108,"D")
	stdscr.addstr(27,96,"Közönség szavazatai")

def jatekos_neve():
	stdscr = curses.initscr()
	kuldes = False
	while not kuldes:
		stdscr.clear()
		hossz, szeleseg = stdscr.getmaxyx()
		x = szeleseg // 2 - 10
		y = hossz//2 - 7
		megjelenites.ablak_szoveg("Kérem adja meg a nevét")
		curses.curs_set(True)
		editwin = curses.newwin(1,y+10, y+1,x+1)
		rectangle(stdscr, y,x ,1+y+1,x+20)
		stdscr.refresh()
		box = Textbox(editwin)
		box.edit()
		if curses.KEY_ENTER or key in [10, 13]:
				kuldes = True
	nev = box.gather()
	curses.curs_set(False)
	return nev

def kerdes_kozepre(kerdesek,index):
	stdscr = curses.initscr()
	hossz, szeleseg = stdscr.getmaxyx()
	x = szeleseg//2 - len(kerdesek[index].kerdes) //2 -9
	y = hossz//2 
	y -= 5
	stdscr.addstr(y,x,kerdesek[index].kerdes,curses.A_REVERSE)
	
def mentes(nev,ido_kezdete,Nyeremeny,nyeremeny_szint,elhasznalt_segitseg,nehezseg):
	ido_vege=time.time()
	eltelt_ido=ido_vege-ido_kezdete
	nyert_osszeg = Nyeremeny[nyeremeny_szint]
	fajlkezeles.mentes_fajlba(nehezseg,nev,Nyeremeny[nyeremeny_szint],eltelt_ido,elhasznalt_segitseg)
	return nyert_osszeg

def keretek():
	stdscr = curses.initscr()
	stdscr.refresh()
	rectangle(stdscr, 7,110 ,1+22+1,119)
	rectangle(stdscr, 25,18 ,1+25+1,25)
	rectangle(stdscr, 25,27 ,1+25+1,46)

def jatek_menet(nev,nehezseg):
	stdscr = curses.initscr()
	os.system("mode con cols=120 lines=30")
	ido_kezdete = time.time()
	kerdes = True
	jatek_fut = True
	helyes = False
	kerdesek = list()
	valaszok = list()
	fajlkezeles.beolvas_loim(kerdesek,valaszok)
	elhasznalt_segitseg = 0
	felezo = 0
	kozonseg = 0
	nyeremeny_szint = 0
	valasztott = ""
	if nehezseg == 1: #nehez = 1 | könnyü =0
		szint = 5
	else:
		szint = 1
	Nyeremeny = ['0','1000', '3000', '6000', '12000', '25000', '50000', '100000', '200000', '400000', '800000', '1500000', '3000000', '6000000', '12500000', '25000000']
	while jatek_fut:
		stdscr.clear()
		felezo_tomb = [1,1,1,1]
		if helyes:
			kerdes = True
			helyes = False
		ABCD = list()
		index = kerdes_generator(szint,kerdesek)
		sor = 0
		oszlop=0
		ABCD.append(valaszok[index].a)
		ABCD.append(valaszok[index].b)
		ABCD.append(valaszok[index].c)
		ABCD.append(valaszok[index].d)
		while kerdes:
			if valasztott not in ["K","F"]:
				stdscr.clear()
			keretek()
			megjelenites.ablak_szoveg("Legyen ön is milliomos")
			kerdes_kozepre(kerdesek,index)
			valasztasi_lehetosegek(sor,oszlop,ABCD,felezo,kozonseg,felezo_tomb)
			nyeremeny(nyeremeny_szint,Nyeremeny)
			key = stdscr.getch()
			if key == curses.KEY_UP and sor > 0:
				sor -= 1
			elif key == curses.KEY_DOWN and   sor != 2:
				sor += 1
			elif key == curses.KEY_RIGHT and  oszlop != 1:
				oszlop +=1
			elif key == curses.KEY_LEFT and oszlop > 0:
				oszlop -=1 
			if felezo_tomb[0] == 0 and  felezo_tomb[3]==0:#feltelek kezdete a mozgasra
				if oszlop == 1:
					sor =0
				if oszlop == 0:            
					sor = 1
			if felezo_tomb[1] == 0 and felezo_tomb[2]==0:
				if oszlop == 0:
					sor = 0
				if oszlop == 1:
					sor = 1
			if felezo_tomb[0] == 0 and felezo_tomb[1]==0:
				if oszlop == 0:
					sor =1
				if oszlop == 1:
					sor = 1
			if felezo_tomb[2]== 0 and felezo_tomb[3]==0:
				if oszlop ==0:
					sor =0
				if oszlop ==1:
					sor =0
			if felezo_tomb[1]==0 and felezo_tomb[3]==0:
				if oszlop==1:
					oszlop=0
			if felezo_tomb[0]==0 and felezo_tomb[2]==0:
				if oszlop ==0:
					oszlop =1
			if 0 in felezo_tomb:
				if sor == 2:
					sor = 1
			if felezo == 1 and kozonseg == 0:
				if oszlop == 0 and sor == 2:
					oszlop +=1
			if felezo == 0 and kozonseg ==1:
				if oszlop == 1 and sor == 2:
					sor -=1
			if felezo == 1 and kozonseg == 1:
				if sor == 2:
					sor =1 #feltelek vege a mozgasra
			if valasztott == "K" and 2 == sor and 1 == oszlop:
				sor -= 1
			if valasztott =="K" and 2 == sor and 0 == oszlop: #egyszere ketto segítseget ne lehessen hasznaéni
				sor -= 1
			elif key == curses.KEY_ENTER or key in [10, 13]:
				if 0 == sor and 0 == oszlop:
					valasztott = "A"
				elif 0 == sor and 1 == oszlop:
					valasztott = "B"
				elif 1 == sor and 0 == oszlop:
					valasztott = "C"
				elif 1 == sor and 1 == oszlop:
					valasztott = "D"
				elif 2 == sor and 0 == oszlop and felezo == 0:
					stdscr.clear()
					valasztott = "F"
					felezo += 1
					elhasznalt_segitseg += 1
					stdscr.attron(curses.color_pair(1))
					stdscr.addstr(26,19,"Felező")
					stdscr.attroff(curses.color_pair(1))
					segitseg_felezo(index,valaszok,kerdesek,felezo_tomb)
				elif 2 == sor and 1 == oszlop and kozonseg == 0 and valasztott !="F":
					valasztott = "K"
					kozonseg += 1
					elhasznalt_segitseg += 1
					segitseg_kozonseg(valaszok[index].helyes)
				if szint >= 10 and nehezseg == 1:
					szint = 9
				if valasztott == valaszok[index].helyes:
					nyeremeny_szint += 1
					szint += 1
					kerdes = False
					helyes = True
				if valasztott != valaszok[index].helyes and valasztott!="K" and valasztott != "F" and valasztott !="":
					kerdes = False
					jatek_fut = False
					return mentes(nev,ido_kezdete,Nyeremeny,nyeremeny_szint,elhasznalt_segitseg,nehezseg)
				if nyeremeny_szint == 15:
					return mentes(nev,ido_kezdete,Nyeremeny,nyeremeny_szint,elhasznalt_segitseg,nehezseg)