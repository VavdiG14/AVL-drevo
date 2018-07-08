from AVLDrevo import AVLDrevo
import math as m

def min_globina(drevo):
    drevo = drevo.koren
    if drevo.prazno():
        return 0
    if drevo.levi.prazno() and drevo.desni.prazno():
        return 1
    if drevo.levi.prazno():
        return min_globina(drevo.desni)+1
    if drevo.desni.prazno():
        return min_globina(drevo.levi)+1
    return min(min_globina(drevo.levi), min_globina(drevo.desni))+1

def max_globina(drevo):
    if drevo.prazno():
        return 0
    else:
        levo = max_globina(drevo.koren.levi)
        desno = max_globina(drevo.koren.desni)

        if levo > desno:
            return levo + 1
        else:
            return desno + 1

def globina_listov(drevo, g=1):
    '''Vrne vsoto globin vseh listov v drevesu '''
    if drevo.prazno():
        return 0
    if drevo.koren.levi.prazno() and drevo.koren.desni.prazno():
        return g
    return globina_listov(drevo.koren.levi, g+1) + globina_listov(drevo.koren.desni, g+1)


def stevilo_listov(drevo):
    ''' vrne število listov v drevesu '''
    if drevo.prazno():
        return 0
    if drevo.koren.levi.prazno() and drevo.koren.desni.prazno():
        return 1
    return stevilo_listov(drevo.koren.levi) + stevilo_listov(drevo.koren.desni)


def povprecna_globina(drevo):
    '''Vrne povprečje globin listov v drevesu '''
    if drevo.prazno():
        return 0
    return round(globina_listov(drevo)/stevilo_listov(drevo), 2)


def opt_min_globina(s):
    return m.floor(m.log(s+1, 2))


def opt_max_globina(s):
    return m.ceil(m.log2(s+1))

def opt_povprecna_globina(s):
    poln = m.floor(m.log2(s+1))
    stevilo_listov = 2**(poln - 1) + m.floor((s - 2**poln + 1)/2)
    return round(((2**(poln - 1) - m.ceil((s - 2**poln + 1)/2)) * poln + (poln+1)*(s - 2**poln + 1))/
                 stevilo_listov, 2)

def st_vozlisc(drevo):
    if drevo.prazno():
        return 0
    return st_vozlisc(drevo.koren.levi) + st_vozlisc(drevo.koren.desni) + 1
    
