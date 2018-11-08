#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:53:25 2018

@author: nestIH
"""

class Bankareikningur():
    
    def __init__(self, inneign=0):
        self.inneign = inneign
        
    def leggja_inn(self,upphaed):
        # virkni: leggur upphæð inn á reikning
        # inntak: tala (heil tala) ( upphæðin sem á að leggja inn )
        # úttak: boolean breyta sem lýsir því hvort að 
        # færslan gekk upp eða ekki
        if upphaed < 0:
            return False
        else:
            self.inneign += upphaed
            if self.inneign >=0: return True
            else: return False
            
    def taka_ut(self, upphaed):
        self.inneign -= upphaed
        if self.inneign >= 0:
            return True
        else:
            self.inneign += upphaed
            return False
        
    def saekja_stodu(self):
        if self.inneign < 0:
            raise ValueError('Neikvæð upphæð á reikningi')
        return self.inneign
    
def main():
    print('Það var kallað á main fallið')
    
if __name__ == '__main__':
    main()
else:
    print('klasanum var importað')
    
    