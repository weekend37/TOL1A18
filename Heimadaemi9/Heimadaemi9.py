#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heimadæmi 9
Möguleg lausn á Bankareikningsverkefninu
@author: helgi
"""

# Ath að bankareikningsklasinn er sóttur úr skrá sem ég nefndi bankareikningurFile.py
# Hún er vistuð í sömu möppu og þessi skrá
from bankareikningurFile import Bankareikningur

class Bankavidskipti:
    
    def __init__(self, reikningur, str= ''):
        self.reikningur = reikningur
        self.str = str

    def Inn_reikning(self):
        # virkni: leggur inn á reikning (sem er eiginleiki hlutsins)
        # inntak: ekkert (nema hluturinn sjálfur)
        # úttak: ekkert
        while(True):
            try:
                upphaed=int(input('Já sæll hvað viltu leggja inn? '))
                try:
                    reikn_svar= self.reikningur.leggja_inn(upphaed)
                    if reikn_svar==True: 
                        print('Innlögn tókst! upphæð:',upphaed,'kr.')
                    elif reikn_svar==False and upphaed<0: 
                        print('Ekki hægt að leggja inn neikvæða upphæð!')
                    else: 
                        print('Villa! Það var neikvæð innistaða á reikningnum :O')
                except:
                    print('ó nei! Villa í reikningsklasa :O')
                    break
                self.str= input('Viltu leggja inn meira? (j/n) ')
                if self.str == 'n': 
                    return
            
            except:
                print('ó nei! villa í notendainnslætti')
                break

    def takaUt_reikning(self):
        # virkni: tekur út af eiginleikanum reikningur
        # inntak: ekkert (nema hluturinn sjálfur)
        # úttak: ekkert
        while(True):
            try:
                upphaed= int(input('Já sæll hvað viltu taka mikið út? '))
                try:
                    reikn_svar= self.reikningur.taka_ut(upphaed)
                    if reikn_svar==True: 
                        print('Úttekt tókst! upphæð:',upphaed,'kr. Go nuts ;)')
                    elif reikn_svar==False:
                        print('Villa! Ekki er næg innistæða :O')
                except:
                    print('ó nei! Villa í reikningsklasa :O')
                    break
                self.str= input('Viltu taka meira út? (j/n) ')
                if self.str == 'n': 
                    return
            except:
                print('ó nei! villa í notendainnslætti')
                break
    
    def saekjaStodu_reikning(self):
        # Virkni: Sækir og birtir stöðu reikningsins (eiginleiki hlutsins)
        # inntak: ekkert
        # úttak: ekkert
        try: 
            stada = self.reikningur.saekja_stodu()
            print("Staða reikningsins er",stada,"kr.")
        except:
            print('ó nei! Villa í reikningsklasa :O')
        return
            

def main():
    reikningur = Bankareikningur()
    vskipti = Bankavidskipti(reikningur)
    
    print("Halóhaló velkomin í bankann minn")
    print("Hér þýðir I=Innlögn, U=Uttekt, S=Staða og H=Hætta")
    
    adgerd = 'EINHVER STRENGUR sem er ekki "H"' # Bara til þess að While-lykkjan keyri
    while adgerd!="H":
        adgerd = input("Hvaða aðgerð má bjóða þér? (I/U/S/H): ")
        if adgerd=="I":
            vskipti.Inn_reikning()
        elif adgerd=="U":
            vskipti.takaUt_reikning()
        elif adgerd=="S":
            vskipti.saekjaStodu_reikning()
        elif adgerd=="H":
            pass
        else:
            print("vúps! Vitlaust slegið inn..reyndu aftur :)")
        
    print("---------------------------------------")
    print("Þú valdir að hætta, takk og bless :)")      
         
if __name__ == '__main__':
    main() 