#!/usr/bin/env python

import os
import sys
import mechanize
import time

os.system('clear')

def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" # Blue aqua
     BB = "\033[34;1m" # Blue light
     YY = "\033[33;1m" # Yellow light
     GG = "\033[32;1m"  # Green Light
     RR = "\033[31;1m" # Red light
     CC = "\033[36;1m" # Cyan light
     B = "\033[34m"    # Blue
     Y = "\033[33;1m"    # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"     # White
     R = "\033[31m"    # Red
     C = "\033[36;1m"    # Cyan
print ()

def cover():
    print (""


            "")
    runntek(GL+"             Assalamu'alaikum.  Gaess")
    time.sleep(1)
    print (" ")
    print (GG+"  +============================================+")
    print (RR+"  +   **********  HACK FACEBOOK  ***********   +")
    print (GG+"  +============================================+")
    print (GL+"  +             MOD BY : ZUFAR AL              +")
    print (YY+"  +             BACALAH BASMALLAH              +")
    print (B+ "  +            FACEBOOK : Zufar AL             +")
    print (Y+ "  +            INSTAGRAM: zufar_al             +")
    print (G+ "  +--------------------------------------------+")
    print (C+ "  +   ********  LIFE OF PROGRAMER  *********   +")
    print (R+ "  +--------------------------------------------+")
    print (GG+"  +============================================+")
    print (RR+"  +   **********  HACK FACEBOOK  ***********   +")
    print (GG+"  +============================================+")
    time.sleep(1)

cover()

#variabel

nama  =  ("     \033[31;1m SELAMAT DATANG DI MENU HACK FB") 
print (nama)
print ("")

#input output

halo = ("     \033[32;1m SILAHKAN LOGIN DULU")
print (halo)
email = input ("     \033[36;1m Masukkan Username :\033[33;1m ")
psw = input ("     \033[36;1m Masukkan Password :\033[33;1m ")

#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'

login = 'https://www.facebook.com/login.php?login_attempt=1'

# Hasil

time.sleep (2)
if psw in ('zufar'):
    print ("     \033[32;1m BERHASIL LOGIN")
else :
    print("     \033[31;1m PASSWORD SALAH")

# Berakhir

print ("")
time.sleep (2)
if psw in ('zufar'):
    runntek ("      \033[33;7mSELAMAT DATA ANDA BERHASIL SAYA CURI:v")
else :
    print ("      \033[31;1mSILAHKAN COBA LAGI")
