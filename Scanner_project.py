#Mengimport modul pyfiglet
import pyfiglet
#Mengimport semua konstanta, data, dan method
from socket import *

#Membuat font art banner ddengan nama "Scanner Project" menggunakan pyfiglet 
result = pyfiglet.figlet_format('Scanner Project', font='banner3-D')
print(result)
print('*By Hafid,Zaka,Cahyo')


#Membuat sebuah fungsi dengan nama scanSocket 
def scanSocket(host, port):
   try:
      s = socket(AF_INET, SOCK_STREAM)
      setdefaulttimeout(1)
      #Return indicator open dan closed
      s.connect((host, port))
      print('port %d ---------> OPEN SUCCESS !!! '% port)
      s.close()
   except:
      print('port %d is closed'% port)
  

#Membuat sebuah fungsi dengan nama portScan untuk mendefinisikan target
def portScan(host, ports):
   try:
      #Merubah hostname menjadi IPv4
      IP = gethostbyname(host)
      print('Hasil scanning host : %s' %IP)
   except:
      print('Tidak dapat menemukan : %s'% host)
      return
   for port in ports:
      scanSocket(host, int(port))

if __name__ == '__main__':
   #Membuat variable inputan data yang akan di scan
   host = input("Masukkan hostname : ")
   awal = int(input("Masukkan port awal scanning : "))
   akhir = int(input("Masukkan port akhir scanning : "))
   #Membuat variable "P" untuk menyimpan data list range nilai port yang diinputkan
   P = list(range(awal,akhir+1))
   #Menjalankan program dengan menggunakan fungsi portScan
   portScan(host, P)
