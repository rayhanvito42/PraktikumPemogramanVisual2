print ('--------------------------------------------')
print ('program mencari volume bangun ruang')
print ('--------------------------------------------')

def volume_tabung() :
    print ('--------------------------------------------')
    print (' ' )
    print (' ' )
    print ('--------------------------------------------')
    print ('program mencari volume tabung')
    print ('--------------------------------------------')
    tinggi=int(input("Masukan Tinggi : "))
    jari=int(input("Masukan Jari-jari Lingkaran : "))
    phi=22/7
    luas=int(2*phi*jari*(tinggi+jari))
    volume=int((phi*(jari*jari))*tinggi)
    print (' ' )
    print ("Luas tabung = ", luas)
    print ("Volume tabung = ", volume)
    

def volume_balok () :
    print ('--------------------------------------------')
    print (' ' )
    print (' ' )
    print ('--------------------------------------------')
    print ('program mencari volume balok' )
    print ('--------------------------------------------')
    p = int(input("masukan panjang balok: "))
    l = int(input("masukan lebar balok: "))
    t = int(input("masukan tinggi balok: "))
    volume=int(p*l*t)
    print (' ' )
    print ("Volume balok = ", volume)
              
def volume_prismasegitiga () :
    print ('--------------------------------------------')
    print (' ' )
    print (' ' )
    print ('--------------------------------------------')
    print (' program mencari volume prisma segitiga ')
    print ('--------------------------------------------')
    tinggi_prisma = int(input("Tinggi Prisma : "))
    alas_segitiga = int(input("Alas Segitiga : "))
    tinggi_segitiga = int(input("Tinggi Segitiga : "))
    volume = ( 1/2 * alas_segitiga * tinggi_segitiga ) * tinggi_prisma
    print ('')
    print("Volume Prisma : %.0f" % (volume))

         
pil = int(input('pilihannya adalah : \n 1.tabung \n 2.balok \n 3.prisma segitiga \n masukkan pilihan yang anda inginkan: '))
if pil == 1 :
    volume_tabung ()
    
elif pil==2 :
    volume_balok()

elif pil==3:
    volume_prismasegitiga()
    
else :
    print (' ' )
    print ('anda salah dalam melakukan input ')