#!/bin/bash/python
 
import time
import sys
 
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
 
#variabel
 
nama  =  ("\033[31;1m SELAMAT DATANG DI MENU ADMIN") 
print (nama)
print ("")
 
#input output
 
halo = ("\033[32m SILAHKAN LOGIN DULU")
print (halo)
email = input ("\033[36;1m Masukkan Username : \033[33;1m ")
psw = input ("\033[36;1m Masukkan Password : \033[33;1m ")
 
# Hasil
 
time.sleep (2)
if psw in ('zufar'):
   print ("\033[32m LOGIN BERHASIL")
else :
   print("\033[31m MAAF PASSWORD SALAH")
 
# Berakhir
 
print ("")
time.sleep (2)
print ("\033[33;1m SELAMAT DATA ANDA BERHASIL SAYA CURI:v")
print ("\033[33;1m --------------------------------------------------")
