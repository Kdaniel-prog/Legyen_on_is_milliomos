import curses

def menu(stdscr, jelenlegi_sor,menu):
	hossz, szeleseg = stdscr.getmaxyx()
	for i, sor in enumerate(menu):
		x = szeleseg//2 - len(sor)//2
		y = hossz//2 - len(menu)//2 + i
		if i == jelenlegi_sor:
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(y, x, sor)
			stdscr.attroff(curses.color_pair(1))
		else:
			stdscr.addstr(y, x, sor)
	stdscr.refresh()
	
def toplista_nevek(lista):
	stdscr = curses.initscr()
	hossz, szeleseg = stdscr.getmaxyx()
	x = szeleseg//2 - len("Név\t\t\t\t\tNyeremény")
	y = hossz//2 - 9
	stdscr.addstr(y,x,"Név\t\t\t\t\tNyeremény",curses.A_REVERSE)
	x = szeleseg // 2
	y += 2
	for i in range(5):
		stdscr.addstr(y+i,x+25,lista[i].penz,curses.A_REVERSE)
		stdscr.addstr(y+i,x-17,lista[i].nev,curses.A_REVERSE)
		stdscr.addstr(y+i,x+25+len(lista[i].penz),"Ft",curses.A_REVERSE)

def toplista(lista,vissza_gomb):
	nehez = False
	jelenlegi_sor= 0
	stdscr = curses.initscr()
	while not nehez:
		stdscr.clear()
		toplista_nevek(lista)
		menu(stdscr, jelenlegi_sor,vissza_gomb)
		key = stdscr.getch()
		if key == curses.KEY_ENTER or key in [10, 13]:
			if jelenlegi_sor == 0:
				nehez = True
		menu(stdscr, jelenlegi_sor,vissza_gomb)

def ablak_szoveg(szoveg):
	stdscr = curses.initscr()
	hossz, szeleseg = stdscr.getmaxyx()
	x = szeleseg//2 - len(szoveg) //2 
	y = (hossz//2) - 12
	stdscr.addstr(y,x,szoveg,curses.A_REVERSE)

def toplista_hiba_kezeles(stdscr,lista,vissza_gomb):
	jelenlegi_sor = 0
	stdscr.clear()
	vissza = False
	try:
		toplista(lista,vissza_gomb)
	except:
		while not vissza:
			stdscr.clear()
			ablak_szoveg("Játsz/játszatok többet! nincs elég adat a toplistához!")
			menu(stdscr, jelenlegi_sor,vissza_gomb)
			key = stdscr.getch()
			if key == curses.KEY_ENTER or key in [10, 13]:
				if jelenlegi_sor == 0:
					vissza = True
		menu(stdscr, jelenlegi_sor,vissza_gomb)

def vegeredmeny(stdscr,nev,nyert_osszeg):
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
	stdscr.bkgd( curses.color_pair(3))
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
	eredmeny = True
	jelenlegi_sor = 0
	vissza_menube = ["Vissza a főmenübe"]
	while eredmeny:
		stdscr.refresh()
		stdscr.clear()
		if int(nyert_osszeg) < 25000000:
			stdscr.addstr(7,50,"vesztettél!",curses.A_REVERSE)
		else:
			stdscr.addstr(7,50,"Gratulálok nyertél!",curses.A_REVERSE)
		stdscr.addstr(8,50,nev,curses.A_REVERSE)
		stdscr.addstr(9,50,"Nyereményed: ",curses.A_REVERSE)
		stdscr.addstr(9,62,nyert_osszeg,curses.A_REVERSE)
		stdscr.addstr(9,62+len(nyert_osszeg),"Ft",curses.A_REVERSE)
		menu(stdscr, jelenlegi_sor,vissza_menube)
		key = stdscr.getch()
		if key == curses.KEY_ENTER or key in [10, 13]:
			if jelenlegi_sor == 0:
				stdscr.refresh()
				stdscr.clear()
				eredmeny = False
