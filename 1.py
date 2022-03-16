print ('--------------------------------------------')
print ('program mencari luas-luas bangun datar')
print ('--------------------------------------------')

def luas_persegi() :
    print ('--------------------------------------------')
    print (' ' )
    print (' ' )
    print ('--------------------------------------------')
    print ('program mencari luas persegi')
    print ('--------------------------------------------')
    x= float(input ('panjang sisi : '))
    luasp= x*x
    print (' ' )
    print ('luas perseginya adalah : ' , luasp , 'cm2')

def luas_segitiga () :
    print ('--------------------------------------------')
    print (' ' )
    print (' ' )
    print ('--------------------------------------------')
    print ('program mencari luas segitiga' )
    print ('--------------------------------------------')
    x= float(input('masukkan alas segitiga : '))
    y= float(input('masukkan tinggi segitiga :'))
    a=0.5*x*y
    print (' ' )
    print ('luas segitiganya adalah : ' , a, 'cm2')
              
def luas_jg () :
    print ('--------------------------------------------')
    print (' ' )
    print (' ' )
    print ('--------------------------------------------')
    print (' program mencari luas jajaran genjang ')
    print ('--------------------------------------------')
    x= float(input('masukkan tinggi jajaran genjang : '))
    y= float (input('masukkan alas jajaran genjang :' ))
    luas = x*y
    print ('')
    print ('luas jajaran genjang adalah : ' , luas , 'cm2')

         
pil = int(input('pilihannya adalah : \n 1.persegi \n 2.segitiga \n 3.jajaran genjang \n masukkan pilihan yang anda inginkan: '))
if pil == 1 :
    luas_persegi ()
    
elif pil==2 :
    luas_segitiga()

elif pil==3:
    luas_jg()
    
else :
    print (' ' )
    print ('anda salah dalam melakukan input ')