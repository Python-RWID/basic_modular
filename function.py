"""
program menghitung luas setiga dengan rumus fungsi
"""
#manual
alas = 7
tinggi = 5
luas_setiga = alas * tinggi / 2
print(f'setiga dengan alas={alas} dan tinggi = {tinggi} memiliki luas {luas_setiga}')

alas = 3
tinggi = 5
luas_setiga = alas * tinggi / 2
print(f'setiga dengan alas={alas} dan tinggi = {tinggi} memiliki luas {luas_setiga}')

#dengan def function
def hitung_luas_segita(alas,tinggi):
    luas_setiga = alas * tinggi / 2
    return luas_setiga
#print(f'berikut hasil menggunakan dengan def function {}')
print (f'hasilnya ={hitung_luas_segita(10,11)}')
print (f'hasilnya = {hitung_luas_segita(5,10)}')