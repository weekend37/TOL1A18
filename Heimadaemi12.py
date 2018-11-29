#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heimadæmi 12 *official*
@author: helgi
heh89@hi.is
"""

import operator # til að raða dictionary 

def makeFile(fileName):
    # inntak: skráarheiti
    # úttak: ekki neitt
    # virkni: tekur inn strengi á skipanalínu á forminu "X atriði"
    # þar sem X er forgangsnúmer (heiltala) og atriði er prófaundirbúningsverkefni
    
    # opna skrá
    skra=open(fileName, 'w+')
    
    # leiðbeiningar
    print('Skrifaðu forgang og forgangsatriði:\n')
    
    # Skrifa skránna
    for i in range(3):
        try:
            atridi = input('forgangsatriði> ')
            try: 
                int(atridi.split()[0])
            except:
                print("error! Fyrst verður að koma tala og svo bil!! reyndu aftur:")
                atridi = input('forgangsatriði> ')
        except:
            print("error við að slá inn")
        # hér ætti að vera tékkað hvort að input frá notandanu sé OK
        skra.write(atridi + '\n')
        
    # loka skrá
    skra.close()
    
def sortFile(fileName):
    # virkni: Raða innihaldi skráarinnar í raðaðan lista
    # inntak: skráarheiti
    # úttak: raðaður listi af innihalda skráarinnar
     
    # lesa inn skrá
    skra=open(fileName, 'r+')
    
    # Röðum línunum í skránni í ditctionary
    unSortedDict = {}
    for line in skra:
        words = line.split() 
        forgangur = int(words[0])
        atridi =  " ".join(words[1:])
        unSortedDict[atridi] = forgangur
        
    # Röðum dictionary-inu    
    sortedList = sorted(unSortedDict.items(), key=operator.itemgetter(1))
    
    # loka skránni
    skra.close()
    return sortedList


def printSortedList(sortedList):
    # virkni: prenta raðaða listann fallega
    # inntak: raðaður listi
    # útta: ekkert
    for atridi in sortedList:
        print(atridi[1],atridi[0])

def main():
    fileName = 'Profaundirbuningur.txt'
    # Lesa inn inntak og skrifa skrá:
    makeFile(fileName)
    # lesa inn skrána sem var skrifuð og raða í lista 
    mySortedList = sortFile(fileName)
    # prenta raðaða listann
    printSortedList(mySortedList)

if __name__=='__main__':
    main()