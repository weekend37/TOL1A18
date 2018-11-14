#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Tímadæmi 11 (wow)
@author: helgi

Lausnaraðferð við dæmi eins og dæmi 2: 
0. skiljum hvað fallið gerir
1. endurskrifum endurkvæma fallið með forlykkju
2. pössum okkur að klára allan kóðann inni í forlykkjunni
3. skrifum eina línu á forminu
    def <function(n)> : [<skipun> if (<skilyrði>) else <skipun> for i in range(<>)]


Æfum okkur!
Skrifum eftirfarandi kóða í einni línu:
    
    def howOldAreYou(age,i):
    if i<=0:
        print('YAY vá hvað þú ert gamall!')
    else:
        print(age-i+1)
        howOldAreYou(age,i-1)
        
"""

# ---------- Endurkvæmni ----------- #

#def howOldAreYou(age,i):
#    if i<=0:
#        print('YAY vá hvað þú ert gamall!')
#    else:
#        print(age-i+1)
#        howOldAreYou(age,i-1)
#        
#howOldAreYou(15,15)

# ----------- Forlykkja ------------ #
        
#def howOldAreYou(age):
#    for i in range(age+1): 
#        if (i < age):
#            print(i+1)
#        else:
#            print("YAY vá hvað þú ert gamall!")
#       
#howOldAreYou(15)

# --------- Einlínuforrit ---------- #
            
#def howOldAreYou(age): [print(i+1) if (i < age) else print('YAY vá hvað þú ert gamall') for i in range(age+1)]
#
#howOldAreYou(15)        
