class DicsosegLista:
    def __init__(self,nev,penz,ido,elhasznalt_segitseg):
        self.nev=nev
        self.penz=str(penz)
        self.elhasznalt_segitseg=elhasznalt_segitseg
        self.ido=ido
    def __lt__(self,other):
        if self.penz==other.penz and self.elhasznalt_segitseg==other.elhasznalt_segitseg:
            return self.ido<other.ido
        if self.penz==other.penz:
            return self.elhasznalt_segitseg<other.elhasznalt_segitseg  
        return int(self.penz) > int(other.penz)      
            
def beolvas_dicsoseg(txt_nev):
    try:
        lista=list()
        with open(txt_nev, "r",encoding="utf-8") as f:
            for sor in f:
                szetvag=sor.rstrip().split("\t")
                lista.append(DicsosegLista(szetvag[0],szetvag[1],szetvag[2],szetvag[3] ))
                lista.sort()
        return lista
            
    except:
        open(txt_nev,"w",encoding="utf-8")

class Kerdesek:
    def __init__(self,szint,kerdes):
        self.kerdes=kerdes
        self.szint=int(szint)

class Valaszok:
    def __init__(self,a,b,c,d,helyes):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.helyes=str(helyes)

def beolvas_loim(kerdesek,valaszok):
    #szint alapján sorba rendezve töltöm fel a 2 classt
    for i in range(1,16):
        f = open("loim.txt", "r",encoding="utf-8")
        for sor in f:
                szetvag=sor.rstrip().split("\t")
                if szetvag [0]=="Nehézség":
                    continue
                if int(szetvag[0])==i:
                    kerdesek.append(Kerdesek(szetvag[0],szetvag[1]))
                    valaszok.append(Valaszok(szetvag[2],szetvag[3],szetvag[4],szetvag[5],szetvag[6]))
    f.close()
    
def ido_txtbe(sec):
    return str(round(sec,0))

def mentes_fajlba(nehezseg,nev,Nyeremeny,eltelt_ido,elhasznalt_segitseg):
        if nehezseg == 1:
            with open("dicsosegNehez.txt","a",encoding="utf-8") as dicsosegListaNehez:
                dicsosegListaNehez.write("{}\t{}\t{}\t{}\n".format(nev,Nyeremeny,elhasznalt_segitseg,ido_txtbe(eltelt_ido)))                
        if nehezseg == 0:
            with open("dicsosegKonnyu.txt","a",encoding="utf-8") as dicsosegListaKonnyu:
                dicsosegListaKonnyu.write("{}\t{}\t{}\t{}\n".format(nev,Nyeremeny,elhasznalt_segitseg,ido_txtbe(eltelt_ido)))
