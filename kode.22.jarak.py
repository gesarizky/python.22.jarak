# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput Satuan Jarak
Meter = float(input("Tuliskan Meter: "))

# Mengkonversi
Km  = Meter / 1000
Hm  = Meter / 100
Dam = Meter / 10
Dm  = Meter * 10
Cm  = Meter * 100
Mm  = Meter * 1000
 
# Menampilkan Hasil 
print('%0.2f  Meter sama dengan %0.2f Kilometer' %(Meter,Km))
print('%0.2f  Meter sama dengan %0.2f Hektometer' %(Meter,Hm))
print('%0.2f  Meter sama dengan %0.2f Dekameter' %(Meter,Dam))
print('%0.2f  Meter sama dengan %0.2f Desimeter' %(Meter,Dm))
print('%0.2f  Meter sama dengan %0.2f Centimeter' %(Meter,Cm))
print('%0.2f  Meter sama dengan %0.2f Milimeter' %(Meter,Mm))
