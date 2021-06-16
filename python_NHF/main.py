import fajlkezeles
import jatek
import megjelenites
import curses
import os

def jatek_inditasa(nehezseg): 
	stdscr = curses.initscr()               
	stdscr.clear()
	nev = jatek.jatekos_neve()
	stdscr.clear()
	nyert_osszeg = jatek.jatek_menet(nev,nehezseg)
	megjelenites.vegeredmeny(stdscr,nev,nyert_osszeg)

def main(stdscr):
	os.system("mode con cols=120 lines=30")
	menu = ['Új játék', 'Legjobb 5', 'Kilépés']
	Legjobb = ['Legjobb 5 (könnyű)', 'Legjobb 5 (nehéz)','Vissza']
	nehezseg_menu = ['Könnyű', 'Nehéz', 'Vissza']
	vissza_gomb = ['Vissza']
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
	stdscr.bkgd( curses.color_pair(3))
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
	kilepes = False
	dicsoseg_listak = True
	uj_jatek = True
	jelenlegi_sor = 0
	nehezseg = 0
	megjelenites.menu(stdscr, jelenlegi_sor,menu)
	while not kilepes:
		megjelenites.ablak_szoveg("Legyen ön is milliomos")
		key = stdscr.getch()
		if key == curses.KEY_UP and jelenlegi_sor > 0:
			jelenlegi_sor -= 1
		elif key == curses.KEY_DOWN and jelenlegi_sor < len(menu)-1:
			jelenlegi_sor += 1
		elif key == curses.KEY_ENTER or key in [10, 13]:
			if jelenlegi_sor == 0:#Uj jatek
				stdscr.clear()
				while uj_jatek:
					stdscr.clear()
					megjelenites.ablak_szoveg("Válasz nehézségi szintet!")
					megjelenites.menu(stdscr,nehezseg,nehezseg_menu)
					key = stdscr.getch()
					if key == curses.KEY_UP and nehezseg > 0:
						nehezseg -= 1
					elif key == curses.KEY_DOWN and nehezseg < len(nehezseg_menu)-1:
						nehezseg += 1
					elif key == curses.KEY_ENTER or key in [10, 13]:
						if nehezseg == 0: #konnyu
							jatek_inditasa(nehezseg)
							uj_jatek = False                    
						if nehezseg == 1: #nehez
							jatek_inditasa(nehezseg)
							uj_jatek = False
						if nehezseg == 2: #Vissza
							stdscr.clear()
							uj_jatek = False
						megjelenites.ablak_szoveg("Válasz nehézségi szintet!")
						megjelenites.menu(stdscr,nehezseg,nehezseg_menu)	
				nehezsge=0
				uj_jatek = True
			if jelenlegi_sor == 1:#dicsoseg istak
				jelenlegi_sor = 0
				stdscr.clear()
				while dicsoseg_listak:
					megjelenites.ablak_szoveg("Dicsőség listák")
					megjelenites.menu(stdscr, jelenlegi_sor,Legjobb)
					key = stdscr.getch()
					if key == curses.KEY_UP and jelenlegi_sor > 0:
						jelenlegi_sor -= 1
					elif key == curses.KEY_DOWN and jelenlegi_sor < len(Legjobb)-1:
						jelenlegi_sor += 1
					elif key == curses.KEY_ENTER or key in [10, 13]:
						if jelenlegi_sor == 0:
							megjelenites.toplista_hiba_kezeles(stdscr,fajlkezeles.beolvas_dicsoseg("dicsosegKonnyu.txt"),vissza_gomb)
						if jelenlegi_sor == 1:
							megjelenites.toplista_hiba_kezeles(stdscr,fajlkezeles.beolvas_dicsoseg("dicsosegNehez.txt"),vissza_gomb)
						if jelenlegi_sor == 2:
							dicsoseg_listak=False
					stdscr.clear()
					megjelenites.menu(stdscr, jelenlegi_sor,Legjobb)
				jelenlegi_sor=0
				dicsoseg_listak=True
			if jelenlegi_sor == 2:
				kilepes = True
		stdscr.clear()
		megjelenites.ablak_szoveg("Legyen ön is milliomos")
		megjelenites.menu(stdscr, jelenlegi_sor,menu)
curses.wrapper(main)
