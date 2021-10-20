# author : @Syhrularv_
# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

banner = """
{}         _memek_{}        _________________
{}        KONTOLLLLLL{}      |                 |
{}       @p~qp~~qMb{}   ._| {}Bash Obfuscator {}|
{}       M{}({}@{})({}@{}) {}M|{}  /  |_________________|
{}       @,{}----.{}JM|{}_/
{}      JS^{}\__/{}  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM    {}Dibuat Oleh {}: {}NYXKONTOL
{}   FqM            MMMM    {}GITHUB       {}: {}NYX095
{} __|'\ .        |\{}dS qML
{} |    `.       | `' \{}Zq
{}_)      \.{}___.{},|     .'
\____   ){}MMMMMP{}|   .'
     `-'       `--'
""".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)

banner2 = """
   {}[{}wibubawang{}]{} Encript      {}[{}kpopler{}]{} Decrypt
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "Nama Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Hasil Nama" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (sukses + "Nah Dah Bisa Kontol..")

   except KeyboardInterrupt:
       print (eror + " Script Berhenti!")
   except IOError:
       print (eror + " File Tidak Ditemukan!")

def enkrip():
   try:
       script = raw_input(ask + W + "Nama Script " + G + "> " + W)
       output = raw_input(ask + W + "Hasil Nama " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + "Done..")
   except KeyboardInterrupt:
       print (eror + " Script Berhentu")
   except IOError:
       print (eror + " File Tidak Ditemukan!")


takok = raw_input(W + "Anda Memilih Tim" + G + " > ")

if takok == "wibubawang" or takok == "1":
   enkrip()
elif takok == "kpopler" or takok == "2":
   dekrip()
else:
   print (eror + " Wrong input")
