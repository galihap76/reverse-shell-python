"""
print(""buah yang tersedia
1. jeruk = 2000
2. apel = 3000
3. anggur = 5000
4. manggis = 3000
5. melon = 4000
"")
"""

bilangan = int(input('Masukkan : '))

if bilangan % 2 == 0:
    print('Adalah bilangan genap')
else:
    print('Bilangan ganjil')







"""
n = int(input('Tolong masukkan harga buah yang tersedia misal untuk membeli jeruk masukkan harga 2000 rupiah : '))

def total(barang, barang2):
    return barang + barang2

if n != 2000 and n != 3000 and n != 5000 and n != 3000 and n != 4000 and n > 4000:
    print('Anda harus memasukkan harga yang sesuai dengan buah yang tersedia!')
if n == 2000 or n == 3000 or n == 5000 or n == 3000 or n == 4000:    
    nanya = input('Mau pilih lagi? : ')
    if nanya == 'y' or nanya == 'Y':
        n_2 = int(input('Masukkan harga buah yang tersedia lagi : '))
        if n_2 != 2000 and n_2 != 3000 and n_2 != 5000 and n_2 != 3000 and n_2 != 4000 and n_2 > 4000:
            print('Anda harus memasukkan harga yang sesuai dengan buah yang tersedia!')
        else:
            Total = total(n,n_2)
            print('Total : ', Total)
    elif nanya == 'n' or nanya == 'N':
        print('Total : ', n)
        
"""