#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:09:50 2018
@author: helgi
"""

class Islendingur:
    
    # smiðurinn okkar
    def __init__(self, n='', h=0, m=0):
        # eiginleikar skilgreindir inni í smiðnum:
        self.nafn = n
        self.haed = h
        self.thyngd = m
            
    # aðferðir hlutarins skilgreindar með föllum
    def væla(self,vælHlutur):
        print('****það var kallað á fallið (eða aðferðina) "væla"****')
        if vælHlutur == 'þyngd':
            print(self.nafn,':,,oh af hverju er ég svona þungur?')
            print(self.thyngd, 'kg er alltof mikið"')
        elif vælHlutur == 'hæð':
            print(self.nafn,':,,oh ég er svo lítill"')
        
    def monta(self):
        print('****það var kallað á fallið (eða aðferðina) "monta"****')
        if self.haed > 180:
            print(self.nafn,':,,haha ég er svo stór"')
        elif self.haed <= 180:
            # getum látið aðferð kalla á aðra aðferð
            self.væla('hæð')
        
def main():    
    ### búum til hlut með klasanum Islendingur
    
    # hluturinn Helgi búinn til:
    Helgi = Islendingur()
    
    # B-breyturnar (eiginleikar) hans settar (ath smiðinn __init__)
    Helgi.nafn = 'Helgi'
    Helgi.haed = 185
    Helgi.thyngd = 86

    # látum hann væla yfir þyngd:
    Helgi.væla('þyngd')
    # látum hann monta sig:
    Helgi.monta()
    
    print('\n')
    
    ### Gerum einn íslending í viðbót, á aðeins öðruvísi hátt:
    # hluturinn Gunnar búinn til og breyturnar hans settar á sama tíma
    Gunnar = Islendingur('Gunnar',170,70)
    
    # látum hann væla yfir þyngd:
    Gunnar.væla('þyngd')
    # látum hann monta sig: 
    # (hann er samt svo lítill að hann endar á að væla)
    Gunnar.monta()
    

if __name__ == '__main__':
    main()