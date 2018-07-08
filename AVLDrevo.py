class Vozlisce:

    def __init__(self, kljuc=None):
        ''' Ustvari vozlišče drevesa:
        - Vozlisce() ustvari prazno vozlišče
        - Vozlisce(kljuc) ustvari vozlišče z danim podatkom ključ
        '''
        self.kljuc = kljuc
        self.levi = None
        self.desni = None
        self.dvojnik = False

    def prazno(self):
        ''' Vrne True, če je drevo prazno, sicer vrne False. '''
        return self.kljuc is None

class AVLDrevo:

    def __init__(self):
        ''' Ustvari prazno AVL drevo. '''
        self.koren = None
        self.visina = -1
        self.ravnotezje = 0
        self.dvojnik = False
        self.brisanje = 0

    def __repr__(self, zamik=''):
        if self.prazno():
            return 'AVLDrevo()'.format(zamik)
        elif self.koren.levi.prazno() and self.koren.desni.prazno():
            return 'AVLDrevo({1})'.format(zamik, self.koren.kljuc)
        else:
           return 'AVLDrevo({1},\n{0}      levo = {2},\n{0}      desno = {3})'.\
               format(
                   zamik,
                   self.koren.kljuc,
                   self.koren.levi.__repr__(zamik + '             '),
                   self.koren.desni.__repr__(zamik + '              ')
               )

    def prazno(self):
        ''' Vrne True, če je drevo prazno, sicer vrne False. '''
        return self.koren is None

    def pravilno(self, mini=-float("inf"), maxi=float("inf")):
        ''' vrne True, če je dvojiško drevo AVL drevo in False, če ni '''
        if self.prazno():
            return True
        if self.koren.kljuc < mini or self.koren.kljuc > maxi:
            return False
        return self.koren.levi.pravilno(mini, self.koren.kljuc-1) and \
               self.koren.desni.pravilno(self.koren.kljuc+1, maxi) and abs(self.ravnotezje) <= 1

##    def pravilno(self):
##        if self.prazno():
##            return True
##        lh = self.koren.levi.visina
##        dh = self.koren.desni.visina
##        if abs(lh-dh) <= 1 and abs(self.ravnotezje) <= 1:
##            return True
##        return False
##  
    def vstavi(self, kljuc):
        ''' vstavi nov podatek na ustrezno mesto v AVL drevesu '''
        if self.prazno():
            self.koren = Vozlisce(kljuc)
            self.koren.levi = AVLDrevo()
            self.koren.desni = AVLDrevo()
        elif kljuc < self.koren.kljuc:
            self.koren.levi.vstavi(kljuc)
        elif kljuc > self.koren.kljuc:
            self.koren.desni.vstavi(kljuc)
        elif kljuc == self.koren.kljuc:
            if self.dvojnik is False:
                self.koren.levi.vstavi(kljuc)
                self.koren.levi.dvojnik = True
                self.dvojnik = True
            else:
                self.koren.desni.vstavi(kljuc)
                self.koren.desni.dvojnik = False
                self.dvojnik = False
        self.visina = max(self.koren.levi.visina, self.koren.desni.visina) + 1
        self.ravnotezje = self.koren.levi.visina - self.koren.desni.visina
        self.popravi()


    def najdi(self, podatek):
        return self.je_v_drevesu(podatek, self.koren)

    def je_v_drevesu(self,podatek, vozlisce):
        """Poisce podatek v drevesu oz. vrne False"""
        if vozlisce is None:
            return False
        elif podatek == vozlisce.kljuc:
            return True
        if podatek < vozlisce.kljuc:
            return self.je_v_drevesu(podatek, vozlisce.levi.koren)
        elif podatek > vozlisce.kljuc:
            return self.je_v_drevesu(podatek, vozlisce.desni.koren)


    def minimum(self, vozlisce=None):
        """Vrne najmanjši element v AVL drevesu"""
        if self.prazno():
            return "Drevo je prazno"
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.levi.prazno:
            return vozlisce.kljuc
        return self.minimum(vozlisce.levi)

    def maksimum(self, vozlisce = None):
        """Vrne najvecji element v AVL drevese"""
        if self.prazno():
            return "Drevo je prazno"
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.desni.prazno:
            return vozlisce.kljuc
        else:
            return self.maksimum(vozlisce.desni)

    def prednik(self,koren):
        """poišče prednika s vozliscem koren"""
        if koren.levi.prazno():
            return None
        else:
            return self.maksimum(koren.levi.koren)

    def naslednik(self, koren):
        if koren.desni.prazno():
            return None
        else:
            return self.minimum(koren.desni.koren)

    def izbrisiNaslednik(self, podatek, vozlisce=None):
        if self.prazno():
            return
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.prazno():
            return
        if podatek < vozlisce.kljuc:
            vozlisce.levi.koren = self.izbrisiNaslednik(podatek,vozlisce.levi.koren)
        elif podatek > vozlisce.kljuc:
            vozlisce.desni.koren = self.izbrisiNaslednik(podatek,vozlisce.desni.koren)
        else:
            if vozlisce.levi.prazno():
                trenutni = vozlisce.desni.koren
                vozlisce.desni.popravi_visine()
                vozlisce.desni.popravi_ravnotezja()
                vozlisce.desni.popravi()
                vozlisce = None
                self.visina = max(self.koren.levi.visina, self.koren.desni.visina) + 1
                self.ravnotezje = self.koren.levi.visina - self.koren.desni.visina
                self.popravi()
                return trenutni
            elif vozlisce.desni.prazno():
                trenutni = vozlisce.levi.koren
                vozlisce.levi.popravi_visine()
                vozlisce.levi.popravi_ravnotezja()
                vozlisce.levi.popravi()
                vozlisce = None
                self.visina = max(self.koren.levi.visina, self.koren.desni.visina) + 1
                self.ravnotezje = self.koren.levi.visina - self.koren.desni.visina
                self.popravi()
                return trenutni
            trenutni = self.naslednik(vozlisce)
            vozlisce.kljuc = trenutni
            vozlisce.desni.koren = self.izbrisiNaslednik(trenutni,vozlisce.desni.koren)
            vozlisce.desni.popravi_visine()
            vozlisce.desni.popravi_ravnotezja()
            vozlisce.desni.popravi()
        return vozlisce

    def izbrisiPrednik(self, podatek, vozlisce=None):
        if self.prazno():
            return
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.prazno():
            return
        if podatek < vozlisce.kljuc:
            vozlisce.levi.koren = self.izbrisiPrednik(podatek,vozlisce.levi.koren)
        elif podatek > vozlisce.kljuc:
            vozlisce.desni.koren = self.izbrisiPrednik(podatek,vozlisce.desni.koren)
        else:
            if vozlisce.levi.prazno():
                trenutni = vozlisce.desni.koren
                vozlisce.desni.popravi()
                vozlisce = None
                return trenutni
            elif vozlisce.desni.prazno():
                trenutni = vozlisce.levi.koren
                vozlisce.levi.popravi()
                vozlisce = None
                return trenutni
            trenutni = self.prednik(vozlisce)
            vozlisce.kljuc = trenutni
            vozlisce.levi.koren = self.izbrisiPrednik(trenutni,vozlisce.levi.koren)
            vozlisce.levi.popravi_visine()
            vozlisce.levi.popravi_ravnotezja()
            vozlisce.levi.popravi()
        return vozlisce

    def izbrisi(self,podatek):
        if not self.najdi(podatek):
            return ("Podatka ni v drevesu")
        if self.brisanje%2 == 0:
            print("Brišem PRED")
            self.izbrisiPrednik(podatek)
        else:
            self.izbrisiNaslednik(podatek)
            print("Brišem NASL")
        self.visina = max(self.koren.levi.visina, self.koren.desni.visina) + 1
        self.ravnotezje = self.koren.levi.visina - self.koren.desni.visina
        self.popravi()
        self.brisanje += 0
        return
   
    def leva_rotacija(self):
        a = self.koren
        b = a.desni.koren
        c = b.levi.koren
        self.koren = b
        b.levi.koren = a
        a.desni.koren = c

    
    def desna_rotacija(self):
        a = self.koren
        b = a.levi.koren
        c = b.desni.koren
        self.koren = b
        b.desni.koren = a
        a.levi.koren = c

    def popravi_visine(self):
        if self.koren:
            if self.koren.levi:
                self.koren.levi.popravi_visine()
            if self.koren.desni:
                self.koren.desni.popravi_visine()
            self.visina = max(self.koren.levi.visina, self.koren.desni.visina) + 1
        else:
            self.visina = -1  
    
    def popravi_ravnotezja(self):
        if self.koren:
            if self.koren.levi:
                self.koren.levi.popravi_ravnotezja()
            if self.koren.desni:
                self.koren.desni.popravi_ravnotezja()
            self.ravnotezje = self.koren.levi.visina - self.koren.desni.visina
        else:
            self.ravnotezje = 0
    
    def popravi(self):
        if self.ravnotezje > 1:
            if self.koren.levi.ravnotezje < 0:
                self.koren.levi.leva_rotacija()
            self.desna_rotacija()
            self.popravi_visine()
            self.popravi_ravnotezja()
        elif self.ravnotezje < -1:
            if self.koren.desni.ravnotezje > 0:
                self.koren.desni.desna_rotacija()
            self.leva_rotacija()
            self.popravi_visine()
            self.popravi_ravnotezja()



import random as ra
#import analizaAVL as analiza

a = AVLDrevo()
for i in [9, 2, 7, 2, 2, 8, 1, 8, 2, 10]:
    a.vstavi(5)



b = AVLDrevo()

b.vstavi(1)
b.vstavi(2)
b.vstavi(3)



    
