#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mín beinagrind fyrir Heimadæmi 12
@author: helgi

tips
- passa að vera í réttu directory-i
- nota operator til að raða dictionary (ef þið viljið gera það þannig)
- muna eftir virkni, inntak, úttak
- " ".join(words[1:]) sameinar öll orðin í listanum words (nema fremsta) og setur í setningu
- ef þið verðið þreytt á að þurfa alltaf að slá inn inputin aftur og aftur til að testa forritið:
    * skrifa hjálparfall sem skrifar skránna (hjá mér heitir það makeFile)
    * nota það til að skrifa skrána og staðfesta að það virki (sjá að skráin er skrifuð í möppunni)
    * kommenta fallið út úr mainfallinu (og nota bara skrána sem var skrifuð)
    * en muna svo að skila verkefninu með ócommentuðu hjálparfalli!
- happy hacking
"""

import operator # gott til að raða dictionary 

def makeFile(fileName):
    pass

    # opna skrá
    
    # Skrifa skránna (t.d. while eða for)
        # taka inn input
        # hér ætti að vera tékkað hvort að input frá notandanu sé OK  
        # skrifa línu í skrá
        
    # loka skrá
    
def sortFile(fileName):    
    pass

    # lesa inn skrá
    
    # Raða línunum í skránni í ditctionary
    
    # Röðum dictionary-inu  (t.d. með fallinu sorted og pakkanum operator)  
    
    # loka skránni

    return sortedList


def printSortedList(sortedList):
    # virkni: prenta raðaða listann fallega
    pass


def main():
    
    fileName = 'forgangur.txt'
    
    # Lesa inn inntak og skrifa skrá:
    makeFile(fileName)
    
    # lesa inn skrána sem var skrifuð og raða í lista 
    sortedList = sortFile(fileName)
    
    # prenta raðaða listann
    printSortedList(sortedList)

if __name__=='__main__':
    main()